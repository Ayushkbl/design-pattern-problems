from typing import Optional, Dict

from domain.pricingRule import PricingRule
from domain.vehicle import Vehicle

class PricingRuleRepository:

    def __init__(self) -> None:
        self._rules: Dict[str, PricingRule] = dict()
        self._vehicle_type_to_rule: Dict[Vehicle.VehicleType, str] = dict()
    
    def save(self, rule: PricingRule) -> PricingRule:
        self._rules[rule.id] = rule
        self._vehicle_type_to_rule[rule.vehicle_type] = rule.id
        return rule
    
    def find_by_id(self, rule_id: str) -> Optional[PricingRule]:
        return self._rules.get(rule_id)
    
    def find_by_vehicle_type(self, vehicle_type: Vehicle.VehicleType):
        return self._rules.get(
            self._vehicle_type_to_rule.get(vehicle_type)
        )

    def find_all(self) -> list[PricingRule]:
        return list(self._rules.values())
    
    def update(self, rule: PricingRule):
        if rule.id in self._rules:
            self._rules[rule.id] = rule
            self._vehicle_type_to_rule[rule.vehicle_type] = rule.id
    
    def delete(self, rule_id: str):
        if rule_id in self._rule:
            rule = self._rules.pop(rule_id)
            self._vehicle_type_to_rule.pop(rule.vehicle_type, None)
    
    def clear(self):
        self._rules.clear()
        self._vehicle_type_to_rule.clear()