complect = {
	'colums' : [
		'id',
		'id_contract',
		'complect_shifr',
		'contract_shifr',
		'contract.subject',
		'stage',
		'tom_name',
		'status',
		'contract_etap_name',
		'spr_mark.name',
		'spr_mark.descriptio'
	],
        
    'query' : '''SELECT TOP(40)
		complect.id
		,complect.id_contract
		,complect.shifr AS complect_shifr
		,contract.shifr AS contract_shifr
		,contract.subject
		,stage.name AS stage
		,complect.tom_name
		,complect.status
		,contract_etap.name AS contract_etap_name
		,spr_mark.name
		,spr_mark.description
		FROM dbo.complect
		JOIN dbo.spr_stage AS stage ON complect.id_stage = stage.id
		JOIN dbo.contract AS contract ON complect.id_contract = contract.id
		JOIN dbo.contract_etap AS contract_etap ON contract_etap.id_contract = contract.id
		JOIN dbo.spr_mark AS spr_mark ON complect.id_mark = spr_mark.id
	'''}


complect_stage = '''SELECT TOP(3)
		complect.id
		,complect.tom_name
		,stage.name
		,stage.description
		FROM dbo.complect AS complect
		JOIN dbo.spr_stage AS stage ON complect.id_stage = stage.id
    '''

contracts = '''SELECT * FROM dbo.contract'''

stages = '''SELECT DISTINCT stage.* FROM dbo.spr_stage AS stage
	JOIN dbo.complect AS complect ON complect.id_stage=stage.id
	JOIN dbo.contract AS contract ON contract.id=complect.id_contract
	WHERE contract.Id = '52a1089c-dc4b-40f6-bf83-6815d9744629';
'''

KOForStageR = '''SELECT DISTINCT op.* FROM dbo.complect AS complect
	JOIN dbo.contract AS contract ON contract.id=complect.id_contract
	JOIN dbo.spr_stage AS stage ON stage.id=complect.id_stage
	JOIN dbo.op AS op ON op.id_contract=contract.Id
	WHERE stage.name = 'Р'  AND contract.Id = '52a1089c-dc4b-40f6-bf83-6815d9744629' AND op.id_parent is NULL
'''

KO = '''SELECT * FROM dbo.op AS op	
	WHERE op.id_parent = '842dc766-9217-4cee-95cf-156b4b2dbe32'
'''

complectForIS = '''SELECT DISTINCT complect.* FROM dbo.op AS op
	JOIN dbo.complect AS complect ON complect.id_oi=op.id
	JOIN dbo.spr_stage AS stage ON stage.id=complect.id_stage
'''
	# WHERE op.id_parent = '842dc766-9217-4cee-95cf-156b4b2dbe32' AND stage.name = 'Р' AND complect.dt_deleted is null

shtamp = '''SELECT DISTINCT 
		contract.subject AS project_name, 
		gip.surname AS gip, 
		oi.description AS object_name, 
		ko.description AS complex_name, 
		doc.shifr AS doc_shifr,
		complect.dt_normocontrol,
		complect.dt_checking, 
		doc.dt_create,
		normocontroler.surname AS normocontroler,
		checkuser.surname AS check_user,
		docuser.surname AS creater_name, 
		stage.name AS stage_shifr,
		doc.description AS doc_description,
		cr.shifr AS rev_shifr, 
		org.name_full AS org_name,
		spv.full_num
		cr.begin_date,
		cr.order_num, 
		complect.dt_approve,
		approve.surname AS approvename,
		mark.description AS mark_description,
		stage.description
	FROM  dbo.complect AS complect
	INNER JOIN dbo.spr_stage AS stage ON complect.id_stage = stage.id                      
	INNER JOIN dbo.op AS oi ON oi.id = complect.id_oi
	INNER JOIN dbo.op AS ko ON oi.id_parent = ko.id
	INNER JOIN dbo.document AS doc ON complect.id = doc.id_complect 
	INNER JOIN dbo.document_part AS dp ON doc.id = dp.id_document  
	INNER JOIN dbo.document_version AS docver ON dp.id = docver.id_part 
	INNER JOIN dbo.contract AS contract ON complect.id_contract = contract.id 
	INNER JOIN dbo.spr_organization AS org ON contract.id_operator = org.id 
	INNER JOIN dbo.spr_mark AS mark ON mark.id = complect.id_mark
	LEFT OUTER JOIN dbo.sheet_permits_view  AS spv
	RIGHT OUTER JOIN dbo.complect_revision AS cr ON spv.id = cr.id_permission ON doc.id_complect = cr.id_complect 
	LEFT OUTER JOIN dbo.users AS checkuser ON complect.id_checking_user = checkuser.id 
	LEFT OUTER JOIN dbo.users AS normocontroler ON complect.id_normocontroler = normocontroler.id
	LEFT OUTER JOIN dbo.users AS gip ON contract.id_gip = gip.id
	LEFT OUTER JOIN dbo.users AS approve ON approve.id = complect.id_approve_user 
	LEFT OUTER JOIN dbo.users AS docuser ON doc.id_user = docuser.id
	WHERE  (doc.shifr = '88883/1-Р-000.000.000-АД-01-С-016')
	AND (doc.status is null OR doc.status<>N'аннул')
	AND (cr.dt_deleted is null)
	ORDER BY cr.begin_date desc
'''