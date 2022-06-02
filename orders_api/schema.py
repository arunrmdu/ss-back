from marshmallow import Schema, fields

orders_schema = {
    'type': 'object',
    'properties':   {
        'u_id':{'type': 'string'},
        'order_total':{'type': 'string'},
        'shipping_address':{'type': 'string'},
        'order_rec':{'type': 'string'},
        'payment_rec':{'type': 'string'},
        'invoice_gen':{'type': 'string'},
        'shipped':{'type': 'string'},
        'order_completed':{'type': 'string'},
        'comments':{'type': 'string'},
        'update_by':{'type': 'string'},
        'is_cancelled':{'type': 'string'},
        'items':{'type': 'array'}
  },
    'required': [ 'u_id','shipping_address','order_total','comments']
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
    {"order_total": fields.Str(default='0.00'), "u_id": fields.Str(), "shipping_address": fields.Str(), "order_rec": fields.Str(default='Y',missing='Y'), 
    "payment_rec": fields.Str(default='N',missing='N'), "invoice_gen": fields.Str(default='N',missing='N'),
    "shipped": fields.Str(default='N',missing='N'),"order_completed": fields.Str(default='N',missing='N'),"comments":fields.Str(default='-',missing='-'),
    "update_by":fields.Str(default='admin',missing='admin'),"is_cancelled":fields.Str(default='Y',missing='Y'),
    "ins_dt":fields.Str(),"update_dt":fields.Str()
    }
)