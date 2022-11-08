from enum import Enum
from sys import argv
from typing import NamedTuple

class IdentifierClass(Enum):
    universal = 0
    application = 1
    context = 2
    private = 3

class IdentifierPC(Enum):
    primitive = 0
    constructed = 1

class IdentifierType(Enum):
    end_of_content = 0
    boolean = 1
    integer = 2
    bit_string = 3
    octet_string = 4
    null = 5
    object_identifier = 6
    object_descriptor = 7
    external = 8
    real = 9
    enumerated = 10
    embedded_pdv = 11
    utf8_string = 12
    relative_oid = 13
    time = 14
    reserved = 15
    sequence_of = 16
    set_of = 17
    numeric_string = 18
    printable_string = 19
    t61string = 20
    videotex_string = 21
    ia5string = 22
    utc_time = 23
    generalized_time = 24
    graphic_string = 25
    visible_string = 26
    general_string = 27
    universal_string = 28
    character_string = 29
    bmp_string = 30
    date = string = 31
    time_of_day = 32
    date_time = 33
    duration = 34
    oid_iri = 35
    relative_oid_iri = 36

class Specific(NamedTuple):
    value: int

class ContextSpecific(Specific):
    name = 'Position'

class ApplicationSpecific(Specific):
    name = 'Application'

def parse(identifier: int) -> tuple[IdentifierClass, IdentifierPC, IdentifierType]:
    id_class = IdentifierClass(identifier >> 6)  # 0b1100_0000
    id_pc = IdentifierPC(identifier >> 5 & 0b1)  # 0b0010_0000
    id_type = IdentifierType(identifier & 0x1F)  # 0b0001_1111
    return id_class, id_pc, id_type

def run(identifier: int) -> None:
    id_class, id_pc, id_type = parse(identifier)
    if id_class.value == 1:
        id_type = ApplicationSpecific(value=id_type.value)
    elif id_class.value == 2:
        id_type = ContextSpecific(value=id_type.value)
    print('-', format(id_class.value, '#04b'), id_class.name)
    print('-   ', id_pc.value, id_pc.name)
    print('-   ', id_type.value, id_type.name)

def run_hex() -> None:
    identifier = int(argv[1], 16)
    print(format(identifier, '#04x'), 'is:')
    print(' ', format(identifier, '#011_b'))
    run(identifier)

def run_bin() -> None:
    identifier = int(argv[1], 2)
    print(format(identifier, '#011_b'), 'is:')
    print(' ', format(identifier, '#04x'))
    run(identifier)

