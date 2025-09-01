from collections import Counter, defaultdict
import statistics
from typing import Any, Dict, List, Optional
from datetime import datetime

from app.etl.extract import CADAPI
from app.etl.load import CADLoader
from app.etl.transform import CADTransformer
from app.models.cad_model import (
    CADRecord, CADRecords,
    CADStatsResponse, StatBlock,
    MonthCountsResponse, MonthCount,
    ClosestApproachesResponse, ClosestApproach
)

class CADController:
    def __init__(self):
        # Loads data on startup
        self.records_container: CADRecords = CADAPI().fetch_data()
        self.all_records: List[CADRecord] = self.records_container.data

    def get_cad(self, start_date: Optional[datetime.date] = None, end_date: Optional[datetime.date] = None) -> List[CADRecord]:
        filtered = self.all_records
        if start_date:
            filtered = [
                r for r in filtered
                if datetime.strptime(r.cd, "%Y-%b-%d %H:%M").date() >= start_date
            ]
        if end_date:
            filtered = [
                r for r in filtered
                if datetime.strptime(r.cd, "%Y-%b-%d %H:%M").date() <= end_date
            ]
        return filtered

    def get_stats(self) -> CADStatsResponse:
        dists = [r.dist for r in self.all_records if r.dist is not None]
        v_rels = [r.v_rel for r in self.all_records if r.v_rel is not None]
        v_infs = [r.v_inf for r in self.all_records if r.v_inf is not None]
        mags = [r.h for r in self.all_records if r.h is not None]
        bodies = {r.body for r in self.all_records if r.body}

        def build_statblock(values: List[float]) -> StatBlock:
            if not values:
                return StatBlock(count=0)
            return StatBlock(
                count=len(values),
                min=min(values),
                max=max(values),
                average=statistics.mean(values),
                median=statistics.median(values),
            )

        return CADStatsResponse(
            total_approaches=len(self.all_records),
            bodies_count=len(bodies),
            distance=build_statblock(dists),
            v_rel=build_statblock(v_rels),
            v_inf=build_statblock(v_infs),
            magnitude=build_statblock(mags),
        )

    def get_by_month(self) -> MonthCountsResponse:
        month_counts = Counter()
        for r in self.all_records:
            try:
                dt = datetime.strptime(r.cd, "%Y-%b-%d %H:%M")
                month = dt.strftime("%Y-%m")
                month_counts[month] += 1
            except Exception:
                continue

        sorted_counts = sorted(month_counts.items())
        return MonthCountsResponse(
            data=[MonthCount(month=m, count=c) for m, c in sorted_counts]
        )

    def get_closest_approaches(self, limit: int = 3) -> ClosestApproachesResponse:
        grouped: Dict[str, List[CADRecord]] = defaultdict(list)
        for r in self.all_records:
            if r.dist_min is not None:
                grouped[r.body].append(r)

        result: Dict[str, List[ClosestApproach]] = {}
        for body, recs in grouped.items():
            sorted_recs = sorted(recs, key=lambda r: r.dist_min)[:limit]
            result[body] = [
                ClosestApproach(
                    body=r.body,
                    des=r.des,
                    cd=r.cd,
                    dist_min=r.dist_min
                )
                for r in sorted_recs
            ]

        return ClosestApproachesResponse(data=result)

    def download_csv(self) -> Any:
        transformer = CADTransformer(self.records_container)
        csv_bytes = transformer.to_csv_bytes()
        loader = CADLoader()
        return loader.save_csv(csv_bytes, mode="response", filename="cad.csv")
