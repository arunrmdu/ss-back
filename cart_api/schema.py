from marshmallow import Schema, fields

cart_schema = {
    'type': 'object',
    'properties': {
       "u_id":{'type': 'string'},
       "p_id":{'type': 'string'},
       "name":{'type': 'string'},
       "i_url":{'type': 'string'},
       "v_id":{'type': 'string'},
       "size":{'type': 'string'},
       "v_qty":{'type': 'string'},
       "qty":{'type': 'string'},
       "u_price":{'type': 'string'},
       "gst":{'type': 'string'},
       "mrp":{'type': 'string'}
    },
    'required': ['p_id', 'u_id','qty']
}


delete_schema={
    'type': 'object',
    'properties': {
       
       "c_id":{'type': 'string'},
    },
    'required': ['c_id']
}

update_schema={
    'type': 'object',
    'properties': {
       "u_id":{'type': 'string'},
       "c_id":{'type': 'string'},
       "qty":{'type': 'string'},
    },
    'required': ['c_id','qty',"u_id"]
}

insert_schema= Schema.from_dict(
    {"p_id": fields.Str(), "u_id": fields.Str(), "name": fields.Str(), "i_url": fields.Str(), "v_id": fields.Str(), "size": fields.Str(),
    "qty":fields.Integer(),"v_qty":fields.Str(),"u_price":fields.Str(),"gst":fields.Str(),"mrp":fields.Str(),"active":fields.Str(),
    "ins_dt":fields.Str(),"update_dt":fields.Str()
    }
)