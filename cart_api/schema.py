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
       
       "c_id":{'type': 'string'},
       "qty":{'type': 'string'},
    },
    'required': ['c_id','qty']
}