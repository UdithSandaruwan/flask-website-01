from sqlalchemy import create_engine, text

db_connection_string="mysql+pymysql://6e1dhbkd0qfnhdiiweuw:pscale_pw_XYWMqZtPxlcUU4feH09QZZGyfu2JpOSaDBYI35faVCX@gcp.connect.psdb.cloud/flaskwebsiteone?charset=utf8mb4"
engine = create_engine(db_connection_string,
                      connect_args={
                        "ssl":{
                          "ssl_ca":"/etc/ssl/cert.pem"
                        }
                      })

with engine.connect() as conn:
  result=conn.execute(text("select * from jobs"))
  print(type(result.all()))