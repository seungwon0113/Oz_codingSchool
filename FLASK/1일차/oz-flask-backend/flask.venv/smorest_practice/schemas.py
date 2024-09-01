from marshmallow import Schema, fields

class BookSchema(Schema):
    id = fields.Int(dump_only=True) # 이 데이터는 서버에서 직접관리 한다
    title = fields.String(required=True)
    author = fields.String(required=True)