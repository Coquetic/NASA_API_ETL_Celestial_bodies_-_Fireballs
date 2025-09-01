from pydantic import BaseModel
from typing import Dict, Optional, List
from datetime import datetime

class CADRecord(BaseModel):
    des: str
    orbit_id: str
    jd: float
    cd: str
    dist: float
    dist_min: float
    dist_max: float
    v_rel: float
    v_inf: float
    t_sigma_f: str
    body: str
    h: float
    diameter: Optional[float] = None
    diameter_sigma: Optional[float] = None

class CADRecords(BaseModel):
    data: List[CADRecord]
    metadata: datetime

class StatBlock(BaseModel):
    count: int
    min: Optional[float] = None
    max: Optional[float] = None
    average: Optional[float] = None
    median: Optional[float] = None

class CADStatsResponse(BaseModel):
    total_approaches: int
    bodies_count: int
    distance: StatBlock
    v_rel: StatBlock
    v_inf: StatBlock
    magnitude: StatBlock

class MonthCount(BaseModel):
    month: str
    count: int

class MonthCountsResponse(BaseModel):
    data: List[MonthCount]

class ClosestApproach(BaseModel):
    body: str
    des: str
    cd: str
    dist_min: float

class ClosestApproachesResponse(BaseModel):
    data: Dict[str, List[ClosestApproach]]
