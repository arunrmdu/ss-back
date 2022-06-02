
from datetime import datetime
import email
from marshmallow import Schema, fields


update_address_schema={
    'type': 'object',
    'properties': {
       "id":{'type': 'string'},
       "address":{'type': 'array'}
    },
    'required': ["id","address"]
}



update_profile_schema={
    'type': 'object',
    'properties': {
       "id":{'type': 'string'},
       "address_primary":{'type': 'array'},
       "password":{'type': 'string'},
       "email":{'type': 'string'},
        "phone":{'type': 'string'},
         "city":{'type': 'string'},
       "state":{'type': 'string'},
       "zip":{'type': 'string'}
    },
    'required': ["id"]
}




user_schema={
      'type': 'object',
    'properties': {
       "username":{'type': 'string'},
       "password":{'type': 'string'},
       "email":{'type': 'string'},
       "category":{'type': 'string'},
       "phone":{'type': 'string'},
       "address_primary":{'type': 'string'},
       "city":{'type': 'string'},
       "state":{'type': 'string'},
       "zip":{'type': 'string'},
       "status":{'type': 'string'},
       "address_alt":{'type': 'array'},
       "active":{'type': 'string'},
    },
    'required': ["username","password","email","phone","address_primary","city","state","zip"]
}




insert_schema= Schema.from_dict(
   {
  "username":fields.Str(),
  "password":fields.Str(),
  "email":fields.Str(),
  "category":fields.Str(default='member',missing='member'),
  "phone":fields.Str(),
  "address_primary":fields.Str(),
  "city":fields.Str(),
  "state":fields.Str(),
  "zip":fields.Str(),
  "status":fields.Str(default='1',missing='1'),
  "insert_ts":fields.Str(default=str(datetime.strftime(datetime.now(),"%Y-%m-%d")),missing=str(datetime.strftime(datetime.now(),"%Y-%m-%d"))),
  "update_ts":fields.Str(default=str(datetime.strftime(datetime.now(),"%Y-%m-%d")),missing=str(datetime.strftime(datetime.now(),"%Y-%m-%d"))),
  "active":fields.Str(default='Y',missing='Y'),
  "update_dt":fields.Str(),
  }
)


