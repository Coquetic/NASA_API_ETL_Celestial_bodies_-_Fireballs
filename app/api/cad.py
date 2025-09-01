from fastapi import APIRouter, Query
from typing import Optional, List
from datetime import date

from app.controller.cad_controller import CADController
from app.models.cad_model import (
    CADRecord,
    CADStatsResponse,
    MonthCountsResponse,
    ClosestApproachesResponse
)

router = APIRouter(tags=["CAD"])

controller = CADController()

@router.get(
    "/",
    response_model=List[CADRecord],
    summary="Get CAD (Close-Approach Data) records",
    description="Returns a list of close-approach events for asteroids/comets. You can optionally filter by start and/or end date (inclusive)."
)
def get_cad(
    start_date: Optional[date] = Query(None),
    end_date: Optional[date] = Query(None),
):
    """
    Returns CAD data, filtered on a date range if specified.
    """
    return controller.get_cad(start_date=start_date, end_date=end_date)

@router.get(
    "/stats",
    response_model=CADStatsResponse,
    summary="Get global CAD statistics",
    description="Returns global statistics: total approaches, number of distinct bodies, "
                "stats on distance, speed and magnitude."
)
def get_stats():
    return controller.get_stats()

@router.get(
    "/by-month",
    response_model=MonthCountsResponse,
    summary="Get CAD counts by month",
    description="Returns the number of approaches aggregated by month (YYYY-MM)."
)
def get_by_month():
    return controller.get_by_month()

@router.get(
    "/closest-approaches",
    response_model=ClosestApproachesResponse,
    summary="Get closest approaches per body",
    description="Returns the N closest approaches per celestial body (sorted by dist_min)."
)
def get_closest_approaches(
    limit: int = Query(3, ge=1)
):
    return controller.get_closest_approaches(limit=limit)

@router.get(
    "/download",
    summary="Download all CAD records as CSV",
    description="Returns a downloadable CSV file containing all CAD data currently available."
)
def download_csv():
    return controller.download_csv()
