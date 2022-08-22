from instance import Instance

def find_loose_open_instances(instances):
    for i in instances:
        i.remove_loose_open_rule()
        print("Instance ", i.id," now has remaing secure rules: ", i.rule)
    return instances

if __name__ == "__main__":
    rule1 = [
        ('inbound', '0.0.0.0/0', 443), 
        ('inbound', '0.0.0.0/0', 22), 
        ('outbound', '0.0.0.0/0', 22)
    ]
    rule2 = [
        ('inbound', '0.0.0.0/0', 443), 
        ('inbound', '0.0.0.0/0', 80), 
        ('outbound', '123.44.67.89/26', 81), 
        ('inbound', '0.0.0.0/0', 22)
    ]

    rule3 = [
        ('inbound', '0.0.0.0/0', 22), 
        ('inbound', '123.44.67.89/26', 81), 
        ('outbound', '127.0.0.1/0', 22)
    ]

    perfect_rule = [
        ('inbound', '123.44.67.89/26', 81), 
        ('outbound', '127.0.0.1/0', 22)
    ]

    instances = []
    instance1 = Instance(1, rule1)
    instance2 = Instance(1, rule2)
    instance3 = Instance(3, rule3)
    perfect_instance = Instance(3, perfect_rule)

    instances.append(instance1)
    instances.append(instance2)
    instances.append(instance3)
    
    find_loose_open_instances(instances)