from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class FireballRecord(BaseModel):
    date: str
    energy: float
    impact_e: Optional[float] = Field(None, alias='impact-e')
    lat: Optional[float] = None
    lat_dir: Optional[str] = Field(None, alias='lat-dir')
    lon: Optional[float] = None
    lon_dir: Optional[str] = Field(None, alias='lon-dir')
    alt: Optional[float] = None
    vel: Optional[float] = None

class FireballRecords(BaseModel) :
    data: List[FireballRecord]
    metadata : datetime

class StatBlock(BaseModel):
    count: int
    min: Optional[float] = None
    max: Optional[float] = None
    average: Optional[float] = None
    median: Optional[float] = None

class FireballStatsResponse(BaseModel):
    total_fireballs: int
    energy: StatBlock
    altitude: StatBlock
    velocity: StatBlock

class YearCount(BaseModel):
    year: int
    count: int

class YearCountsResponse(BaseModel):
    data: List[YearCount]

class RegionCount(BaseModel):
    region: str
    count: int

class RegionCountsResponse(BaseModel):
    data: List[RegionCount]
