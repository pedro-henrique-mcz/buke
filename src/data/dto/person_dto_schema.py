'''This module is use to validate the person dto params 
with marshmallow library'''

from marshmallow import Schema, fields, validate

class PersonDTOSchema(Schema):
    """Validation of the Persons """
    
    # --- mandatory---
    person_id = fields.Int()
    
    first_name = fields.Str(
        required=True,
        validate=validate.Length(min=5, error="The name must have at least 5 characters")
    )
    
    category_id = fields.Int()

    # --- Opticional---
    last_name = fields.Str()
    nick_name = fields.Str()
    next_interaction = fields.Date()
    interaction_frequency = fields.Int()
    general_notes = fields.Str()
   