from pathlib import Path
from io import BytesIO
from typing import Literal, Union

from fastapi.responses import StreamingResponse

class FireballLoader:
    def __init__(self):
        pass

    def save_csv(
        self,
        data: BytesIO,
        mode: Literal["file", "response"] = "file",
        filename: str = "fireballs.csv"
    ) -> Union[None, StreamingResponse]:
        """
        Saves the CSV file to disk or returns a downloadable HTTP response.

        :param data: CSV Data in bytes
        :param mode: "file" to write to disk, "response" to return an HTTP response
        :param filename: name of the file
        """
        if mode == "file":
            output_path = Path("output")
            output_path.mkdir(parents=True, exist_ok=True)
            full_path = output_path / filename
            with open(full_path, "wb") as f:
                f.write(data.getvalue())
            print(f"CSV saved to {full_path}")
            return None

        if mode == "response":
            return StreamingResponse(
                content=data,
                media_type="text/csv",
                headers={"Content-Disposition": f"attachment; filename={filename}"}
            )

class CADLoader:
    def __init__(self):
        pass

    def save_csv(
        self,
        data: BytesIO,
        mode: Literal["file", "response"] = "file",
        filename: str = "cad_records.csv"
    ) -> Union[None, StreamingResponse]:
        """
        Saves the CSV file to disk or returns a downloadable HTTP response.

        :param data: CSV Data in bytes
        :param mode: "file" to write to disk, "response" to return an HTTP response
        :param filename: name of the file
        """
        if mode == "file":
            output_path = Path("output")
            output_path.mkdir(parents=True, exist_ok=True)
            full_path = output_path / filename
            with open(full_path, "wb") as f:
                f.write(data.getvalue())
            print(f"CSV saved to {full_path}")
            return None

        if mode == "response":
            return StreamingResponse(
                content=data,
                media_type="text/csv",
                headers={"Content-Disposition": f"attachment; filename={filename}"}
            )
