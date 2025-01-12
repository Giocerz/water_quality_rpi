import sqlite3
from src.model.WaterQualityParams import WaterQualityParams
from src.model.LoteModel import LoteModel

class WaterDataBase:
    WATER_TABLE_NAME = "waterParams"
    LOTE_TABLE_NAME = "lotesTable"
    DB_NAME = 'water_quality.db'


    @staticmethod
    def _open_db():
        connection = sqlite3.connect(WaterDataBase.DB_NAME)
        cursor = connection.cursor()
        cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {WaterDataBase.WATER_TABLE_NAME}(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                device_id TEXT NOT NULL,
                latitude REAL,
                longitude REAL,
                date TEXT NOT NULL,
                hour TEXT NOT NULL,
                conductivity REAL,
                oxygen REAL,
                ph REAL,
                tds REAL,
                temperature REAL,
                turbidity REAL,
                battery REAL,
                sample_origin TEXT NOT NULL,
                it_rained TEXT NOT NULL,
                upload_state INTEGER NOT NULL,
                lote_id INTEGER NOT NULL
            )
        ''')
        cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {WaterDataBase.LOTE_TABLE_NAME}(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                creation_date TEXT NOT NULL,
                creation_hour TEXT NOT NULL,
                last_add_date TEXT NOT NULL,
                last_add_hour TEXT NOT NULL,
                description TEXT
            )
        ''')
        connection.commit()
        return connection

    @staticmethod
    def insert(water_quality_params: WaterQualityParams):
        conn = WaterDataBase._open_db()
        cursor = conn.cursor()
        cursor.execute(f'''
            INSERT INTO {WaterDataBase.WATER_TABLE_NAME} 
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
    def get_lotes() -> list[LoteModel]:
        conn = WaterDataBase._open_db()
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {WaterDataBase.LOTE_TABLE_NAME} ORDER BY id DESC")
        rows = cursor.fetchall()
        conn.close()
        params_list = []
        for row in rows:
            params = LoteModel(
                id=row[0], name=row[1], creation_date=[2], creation_hour=[3],
                last_add_date=row[4], last_add_hour=row[5], description=row[6]
            )
            params_list.append(params)
        return params_list
    
    @staticmethod
    def get_lotes_by_id(lote_id:int) -> LoteModel:
        conn = WaterDataBase._open_db()
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {WaterDataBase.LOTE_TABLE_NAME} WHERE id = {lote_id}")
        row = cursor.fetchone()
        conn.close()
        param = LoteModel(
            id=row[0], name=row[1], creation_date=[2], creation_hour=[3],
            last_add_date=row[4], last_add_hour=row[5], description=row[6]
        )
        return param
    
    @staticmethod
    def insert_lote(lote:LoteModel) -> int:
        conn = WaterDataBase._open_db()
        cursor = conn.cursor()
        cursor.execute(f'''
            INSERT INTO {WaterDataBase.LOTE_TABLE_NAME} 
            (name, creation_date, creation_hour, last_add_date, last_add_hour, description)
            VALUES (?, ?, ?, ?, ?, ?)
            ''', (
                lote.name,
                lote.creation_date,
                lote.creation_hour,
                lote.last_add_date,
                lote.last_add_hour,
                lote.description
        ))
        conn.commit()
        conn.close()
        return cursor.lastrowid
    
    @staticmethod
    def update_lote(lote_id:int, date:str, hour:str):
        conn = WaterDataBase._open_db()
        cursor = conn.cursor()
        cursor.execute(f'''
            UPDATE {WaterDataBase.LOTE_TABLE_NAME} 
            SET last_add_date = ?, last_add_hour = ?
            WHERE id = ?
            ''', (
                date,
                hour,
                lote_id
        ))
        conn.commit()
        conn.close()

    @staticmethod
    def delete_lote(lote_id:int):
        conn = WaterDataBase._open_db()
        cursor = conn.cursor()
        cursor.execute(f'''
            DELETE {WaterDataBase.LOTE_TABLE_NAME} 
            WHERE id = ?
            ''', (
                lote_id
        ))
        cursor.execute(f'''
            DELETE {WaterDataBase.WATER_TABLE_NAME} 
            WHERE lote_id = ?
            ''', (
                lote_id
        ))
        conn.commit()
        conn.close()

    
    @staticmethod
    def get_water_quality_params_by_lote(lote_id:int) -> list[WaterQualityParams]:
        conn = WaterDataBase._open_db()
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {WaterDataBase.WATER_TABLE_NAME} WHERE lote_id = {lote_id} ORDER BY id DESC")
        rows = cursor.fetchall()
        conn.close()
        params_list = []
        for row in rows:
            params = WaterQualityParams(
                id=row[0], name=row[1], device_id=row[2], latitude=row[3], longitude=row[4],
                date=row[5], hour=row[6], conductivity=row[7], oxygen=row[8], ph=row[9],
                tds=row[10], temperature=row[11], turbidity=row[12], battery=row[13], sample_origin=row[14],
                it_rained=row[15], upload_state=row[16], lote_id=row[17]
            )
            params_list.append(params)
        return params_list


    @staticmethod
    def get_water_quality_params() -> list[WaterQualityParams]:
        conn = WaterDataBase._open_db()
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {WaterDataBase.WATER_TABLE_NAME} ORDER BY id DESC")
        rows = cursor.fetchall()
        conn.close()

        params_list = []
        for row in rows:
            params = WaterQualityParams(
                id=row[0], name=row[1], device_id=row[2], latitude=row[3], longitude=row[4],
                date=row[5], hour=row[6], conductivity=row[7], oxygen=row[8], ph=row[9],
                tds=row[10], temperature=row[11], turbidity=row[12], battery=row[13], sample_origin=row[14],
                it_rained=row[15], upload_state=row[16], lote_id=row[17]
            )
            params_list.append(params)
        return params_list

    @staticmethod
    def update_upload_state(id: int, new_state: int):
        conn = WaterDataBase._open_db()
        cursor = conn.cursor()
        cursor.execute(f'''
            UPDATE {WaterDataBase.WATER_TABLE_NAME}
            SET upload_state = ?
            WHERE id = ?
        ''', (new_state, id))
        conn.commit()
        conn.close()