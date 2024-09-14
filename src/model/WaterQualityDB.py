import sqlite3
from src.model.WaterQualityParams import WaterQualityParams

class WaterDataBase:
    table_name = "waterParams"
    db_name = 'water_quality.db'

    @staticmethod
    def _open_db():
        # Abre la base de datos y crea la tabla si no existe
        connection = sqlite3.connect(WaterDataBase.db_name)
        cursor = connection.cursor()
        cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {WaterDataBase.table_name}(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                device_id TEXT,
                latitude REAL,
                longitude REAL,
                date TEXT,
                hour TEXT,
                conductivity REAL,
                oxygen REAL,
                ph REAL,
                tds REAL,
                temperature REAL,
                turbidity REAL,
                sample_origin TEXT,
                it_rained TEXT,
                upload_state INTEGER,
                lote_id INTEGER
            )
        ''')
        connection.commit()
        return connection

    @staticmethod
    def insert(water_quality_params: WaterQualityParams):
        conn = WaterDataBase._open_db()
        cursor = conn.cursor()
        cursor.execute(f'''
            INSERT INTO {WaterDataBase.table_name} 
            (name, device_id, latitude, longitude, date, hour, conductivity, oxygen, ph, tds, temperature, turbidity, sample_origin, it_rained, upload_state, lote_id)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            water_quality_params.name,
            water_quality_params.device_id,
            water_quality_params.latitude,
            water_quality_params.longitude,
            water_quality_params.date,
            water_quality_params.hour,
            water_quality_params.conductivity,
            water_quality_params.oxygen,
            water_quality_params.ph,
            water_quality_params.tds,
            water_quality_params.temperature,
            water_quality_params.turbidity,
            water_quality_params.sample_origin,
            water_quality_params.it_rained,
            water_quality_params.upload_state,
            water_quality_params.lote_id
        ))
        conn.commit()
        conn.close()

    @staticmethod
    def get_water_quality_params() -> list[WaterQualityParams]:
        conn = WaterDataBase._open_db()
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {WaterDataBase.table_name} ORDER BY id DESC")
        rows = cursor.fetchall()
        conn.close()

        params_list = []
        for row in rows:
            params = WaterQualityParams(
                id=row[0], name=row[1], device_id=row[2], latitude=row[3], longitude=row[4],
                date=row[5], hour=row[6], conductivity=row[7], oxygen=row[8], ph=row[9],
                tds=row[10], temperature=row[11], turbidity=row[12], sample_origin=row[13],
                it_rained=row[14], upload_state=row[15], lote_id=row[16]
            )
            params_list.append(params)
        return params_list

    @staticmethod
    def update_upload_state(id: int, new_state: int):
        conn = WaterDataBase._open_db()
        cursor = conn.cursor()
        cursor.execute(f'''
            UPDATE {WaterDataBase.table_name}
            SET upload_state = ?
            WHERE id = ?
        ''', (new_state, id))
        conn.commit()
        conn.close()