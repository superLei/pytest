#coding=UTF-8
MYSQL_TABLE = {

    "master": [
        'cityLst', 'orgIDLst', 'excludedShopIDLst', 'consumeTimeLst', 'submitTimeLst', 'crmLevelLst',
        'crmConditionsJson', 'foodScopeType', 'categoryCodeLst', 'foodCodeLst', 'excludedFoodNameLst',
        'sharedPromotionIDLst', 'maintenanceLevel', 'maintenanceOrgID', 'modifiedBy','action',
        'script','excludedSubjectLst','createStamp','actionStamp','subjectType','defaultRun',
        'isActive','promotionShowName','groupID'
    ],
"master_noRuleJson": [
        'cityLst', 'orgIDLst', 'excludedShopIDLst', 'consumeTimeLst', 'submitTimeLst', 'crmLevelLst',
        'crmConditionsJson', 'foodScopeType', 'categoryCodeLst', 'foodCodeLst', 'excludedFoodNameLst',
        'sharedPromotionIDLst', 'maintenanceLevel', 'maintenanceOrgID', 'modifiedBy','action',
        'script','excludedSubjectLst','createStamp','actionStamp','subjectType','defaultRun',
        'isActive','promotionShowName','groupID','ruleJson'
    ],
    "food_price": [
        'actionStamp', 'createStamp', 'action', 'num'
    ],
    "food_price_da": [
        'actionStamp', 'createStamp', 'action'
    ],
    "food_scope": [
        'createStamp', 'num', 'stageNo'
    ],
    "food_scope_da": [
        'createStamp'
    ],
    "time": [
        'createStamp'
    ]

}
