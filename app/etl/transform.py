import csv
from io import BytesIO, StringIO

from app.models.fireball_model import FireballRecords
from app.models.cad_model import CADRecords


class FireballTransformer:
    def __init__(self, records: FireballRecords):
        self.records = records

    def to_csv_bytes(self) -> BytesIO:
        output = StringIO()
        writer = csv.writer(output)

        # Header
        writer.writerow([
            "date", "energy", "impact-e",
            "lat", "lat-dir", "lon", "lon-dir",
            "alt", "vel"
        ])

        for record in self.records.data:
            writer.writerow([
                record.date,
                record.energy,
                record.impact_e,
                record.lat,
                record.lat_dir,
                record.lon,
                record.lon_dir,
                record.alt,
                record.vel
            ])

        byte_output = BytesIO()
        byte_output.write(output.getvalue().encode("utf-8"))
        byte_output.seek(0)
        return byte_output


class CADTransformer:
    def __init__(self, records: CADRecords):
        self.records = records

    def to_csv_bytes(self) -> BytesIO:
        output = StringIO()
        writer = csv.writer(output)

        # Header
        writer.writerow([
            "des", "orbit_id", "jd", "cd",
            "dist", "dist_min", "dist_max",
            "v_rel", "v_inf", "t_sigma_f",
            "body", "h", "diameter", "diameter_sigma"
        ])

        for record in self.records.data:
            writer.writerow([
                record.des,
                record.orbit_id,
                record.jd,
                record.cd,
                record.dist,
                record.dist_min,
                record.dist_max,
                record.v_rel,
                record.v_inf,
                record.t_sigma_f,
                record.body,
                record.h,
                record.diameter,
                record.diameter_sigma
            ])

        byte_output = BytesIO()
        byte_output.write(output.getvalue().encode("utf-8"))
        byte_output.seek(0)
        return byte_output
