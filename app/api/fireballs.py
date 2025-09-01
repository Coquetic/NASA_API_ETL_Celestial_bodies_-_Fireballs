from fastapi import APIRouter, Query
from typing import Optional, List
from datetime import date
from app.models.fireball_model import FireballRecord, FireballStatsResponse, RegionCountsResponse, YearCountsResponse
from app.controller.fireballs_controller import FireballsController

router = APIRouter(tags=["Fireballs"])

controller = FireballsController()

@router.get(
    "/",
    response_model=List[FireballRecord],
    summary="Get fireballs (optional date filter)",
    description="Returns a list of fireball events. You can optionally filter by start and/or end date (inclusive)."
)
def get_fireballs(
    start_date: Optional[date] = Query(None),
    end_date: Optional[date] = Query(None),
):
    return controller.get_fireballs(start_date=start_date, end_date=end_date)

@router.get(
    "/top",
    response_model=List[FireballRecord],
    summary="Get top fireballs by energy",
    description="Returns the N most energetic fireballs detected over the last X years. "
                "By default, returns the top 20 fireballs over the last 5 years."
)
def get_top_fireballs(
    years: int = Query(5, ge=1, description="Number of past years to consider."),
    limit: int = Query(20, ge=1, description="Maximum number of results to return.")
    ):
    return controller.get_top_fireballs(years=years, limit=limit)

@router.get(
    "/stats",
    response_model=FireballStatsResponse,
    summary="Get global fireball statistics",
    description="Returns statistical aggregates (mean, min, max, std) on energy, altitude and velocity "
                "of all fireball events."
)
def get_fireball_stats():
    return controller.get_fireball_stats()

@router.get(
    "/year-counts",
    response_model=YearCountsResponse,
    summary="Get yearly fireball counts",
    description="Returns a dictionary where keys are years and values are the number of fireballs detected that year."
)
def get_fireballs_per_year():
    return controller.get_fireballs_per_year()

@router.get(
    "/by-continents",
    response_model=RegionCountsResponse,
    summary="Get fireball counts by region",
    description="Returns a dictionary of fireball counts by region (continent), "
                "based on their geographical coordinates."
)
def get_fireballs_by_region():
    return controller.get_fireballs_by_region()

@router.get(
    "/download",
    summary="Download all fireballs as CSV",
    description="Returns a downloadable CSV file containing all fireball data currently available."
)
def download_csv():
    return controller.download_csv()
