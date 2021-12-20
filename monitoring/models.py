import logging
from datetime import datetime
from . import db, Base, session_db


class MonitoringPrice(Base):
    __tablename__ = 'monitoring_price'
    id = db.Column(db.BigInteger, primary_key=True)
    created = db.Column(db.TIMESTAMP)
    last_updated = db.Column(db.TIMESTAMP)
    city = db.Column(db.String)
    shop_name = db.Column(db.String)
    shop_type = db.Column(db.String)
    shop_category = db.Column(db.String)
    provider = db.Column(db.String)
    product_name = db.Column(db.String)
    product_unit = db.Column(db.String)
    package = db.Column(db.String)
    thermal_state = db.Column(db.String)
    product_price = db.Column(db.Numeric)
    stationary_view = db.Column(db.String)
    composition = db.Column(db.String)
    channel = db.Column(db.String)

    def save(self):
        try:
            session_db.add(self)
            session_db.commit()
        except Exception as e:
            logging.exception(e)
            session_db.rollback()

    @classmethod
    def get_today_data_count(cls, shop_name):
        try:
            s = cls.query.filter(cls.shop_name == shop_name, cls.created == datetime.now().date()).count()
            return s
        except Exception as e:
            logging.exception(e)
            session_db.rollback()
