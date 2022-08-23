from app.instance import Instance
import pytest

rule1 = [
    ('inbound', '0.0.0.0/0', 443), 
    ('inbound', '0.0.0.0/0', 22), 
    ('outbound', '0.0.0.0/0', 22)
]

rule2 = [
    ('inbound', '0.0.0.0/0', 22), 
    ('inbound', '123.44.67.89/26', 81), 
    ('outbound', '127.0.0.1/0', 22)
]

perfect_rule = [
    ('inbound', '123.44.67.89/26', 81), 
    ('outbound', '127.0.0.1/0', 22)
]

instance1 = Instance(1, rule1)

instance2 = Instance(2, rule2)

perfect_instance = Instance(3, perfect_rule)

def test_instance_filtered():
    assert instance2.remove_loose_open_rule() == perfect_instance.rule

