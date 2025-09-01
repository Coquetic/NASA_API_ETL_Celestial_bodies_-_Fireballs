from typing import Any, List, Optional, Dict
from collections import Counter, defaultdict
from datetime import datetime, timedelta
from app.etl.extract import FireballAPI
from app.etl.transform import FireballTransformer
from app.etl.load import FireballLoader
from app.tools.fireballs_tools import compute_stats, get_continent, normalize_coordinates

from app.models.fireball_model import (
    FireballRecord, FireballRecords,
    FireballStatsResponse, StatBlock,
    YearCountsResponse, YearCount,
    RegionCountsResponse, RegionCount
)

class FireballsController:
    def __init__(self):
        # Loads data on startup
        self.records_container: FireballRecords = FireballAPI().fetch_data()
        self.all_records: List[FireballRecord] = self.records_container.data
        self.normalized_coordinates_records = normalize_coordinates(self.all_records)

    def get_fireballs(self, start_date: Optional[datetime.date] = None, end_date: Optional[datetime.date] = None) -> List[FireballRecord]:
        filtered = self.all_records
        if start_date:
            filtered = [
                r for r in filtered
                if datetime.fromisoformat(r.date).date() >= start_date
            ]
        if end_date:
            filtered = [
                r for r in filtered
                if datetime.fromisoformat(r.date).date() <= end_date
            ]
        return filtered

    def get_top_fireballs(self, years: int = 5, limit: int = 20) -> List[FireballRecord]:
        now = datetime.now().replace(tzinfo=None)
        past_date = now - timedelta(days=years * 365)

        recent = [
            r for r in self.all_records
            if datetime.fromisoformat(r.date) >= past_date and r.energy is not None
        ]
        sorted_by_energy = sorted(recent, key=lambda r: r.energy, reverse=True)
        return sorted_by_energy[:limit]

    def get_fireball_stats(self) -> FireballStatsResponse:
        energies = [r.energy for r in self.all_records]
        altitudes = [r.alt for r in self.all_records]
        velocities = [r.vel for r in self.all_records]

        return FireballStatsResponse(
            total_fireballs=len(self.all_records),
            energy=StatBlock(**compute_stats(energies)),
            altitude=StatBlock(**compute_stats(altitudes)),
            velocity=StatBlock(**compute_stats(velocities)),
        )

    def get_fireballs_per_year(self) -> YearCountsResponse:
        year_counts = Counter()
        for record in self.all_records:
            try:
                year = datetime.fromisoformat(record.date).year
                year_counts[year] += 1
            except Exception:
                continue
        sorted_counts = sorted(year_counts.items())
        return YearCountsResponse(
            data=[YearCount(year=year, count=count) for year, count in sorted_counts]
        )

    def get_fireballs_by_region(self) -> RegionCountsResponse:
        region_counts = defaultdict(int)
        for r in self.normalized_coordinates_records:
            region = get_continent(r.lat, r.lon)
            region_counts[region] += 1
        return RegionCountsResponse(
            data=[RegionCount(region=region, count=count) for region, count in region_counts.items()]
        )

    def download_csv(self) -> Any:
        transformer = FireballTransformer(self.records_container)
        csv_bytes = transformer.to_csv_bytes()
        loader = FireballLoader()
        return loader.save_csv(csv_bytes, mode="response", filename="fireballs.csv")
