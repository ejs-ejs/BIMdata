# import re, collections
# from lxml import etree

from ifctester.facet import Classification, Property, Entity, Restriction

import datetime


from lib.layout import Layout
from lib.report import Report
from vvk.eir import EIR

def main(eir, output_flavour: str = "VVK", report_type: str = 'ids', stage:str='s2'):

    layout = Layout()
    report = Report(report_type)

    if output_flavour.upper() == 'VVK':
        
        output_classification = 'NSIK'

        report.title = "IPP GEOMETRIJA"
        report.set_column_widths({'A':4.5, 'B':2.0, 'C':2.0, 'D':2.0, 'E':2.0, 'F':2.0, 'G':4.0, 'H':3.0, 'I':3.0,
                              'J':2.5,'N':2.5, 'Q':2.5, 'T':2.5, 'W':2.5, 'Z':4.5, 
                              'K':6.0, 'O':6.0, 'R':9.0, 'U':8.0, 'X':10.0, 'AA':10.0,
                              'L':7.0, 'P':4.5, 'S':4.5, 'V':4.5, 'Y':4.5, 'AB':4.5}
                 )
        layout.flavour = output_flavour
        layout.set_metas({'ifcType':1, 'name':8, 'names':9, 'file':10})
        layout.set_stages({'s0':11, 's2':14, 's3':17, 's4':20, 's5':23, 's6':24})
        layout.set_classifications({'NSIK LF':2, 'NSIK LT':3,  'NSIK LK':4, 'NSIK B':6})
        layout.set_titles({'ifcType':'IFC kategorija','name':'Pavadinimas', 'file':'PROJEKTO DALIS', 
                'NSIK LF':'Funkcinės sistemos kodas - ClassificationSystemCF arba „ISO81346 CF“ klasifikatorius',
                'NSIK LT':'Techninės sistemos kodas - ClassificationSystemCT arba „ISO81346 CT“ klasifikatorius',
                'NSIK LK':'Komponento kodas - ClassificationSystemCO arba „ISO81346 CO“ klasifikatorius',
                'NSIK B':'Erdvės kodas - ClassificationSystemCS arba „ISO81346 CS“ klasifikatorius',
                # 'Uniclass':'"Uniclass 2015" klasifikatorius',
                'names':'Pavadinimas kitose klasifikavimo sistemose',
                's0':'ES MODELIAI', 's2':'PP MODELIAI','s4':'TDP MODELIAI', 
                'properties':'Privalomų pateikti savybių ir sąrašas ir ju priskyrimas savybių rinkiniams',
                'classification':"Klasifikatoriai",
                'memo': 'Pastabos', 'String': 'Tekstas', 'Real':'Skaičius'})
    
    if output_flavour.upper() == 'SKST':
        report.title = "IPP GEOMETRIJA"
        layout.flavour = output_flavour

        output_classification = 'NSIK'
        report.set_column_widths({'A':6.0, 'B':2.5, 'C':2.5, 'D':2.5, 'E':2.5, 'F':0.2, 'G':5.0, 'H':0.2, 
                                  'I':2.5, 'J':2.5, 'K':2.5, 'L':2.5, 'M':2.5, 'N':2.5, 'O':2.5}
                                )
        layout.set_metas({'ifcType':7, 'name':1, 'file':15})
        layout.set_stages({'s0':9, 's2':10, 's3':11, 's4':12, 's5':13, 's6':14})
        # layout.set_classifications({'NSIK LF':2, 'NSIK LT':3,  'NSIK LK':4, 'NSIK B':6, 'Uniclass':7})
        layout.set_classifications({'NSIK LF':2, 'NSIK LT':3,  'NSIK LK':4, 'NSIK B':5})

        # output_classification = 'Uc'
        # report.set_column_widths({'A':6.0, 'B':0.2, 'C':0.2, 'D':0.2, 'E':4.5, 'F':0.2, 'G':5.0, 'H':0.2, 
        #                           'I':2.5, 'J':2.5, 'K':2.5, 'L':2.5, 'M':2.5, 'N':2.5, 'O':2.5}
        #                         )
        # layout.set_metas({'ifcType':7, 'name':1, 'file':15})
        # layout.set_stages({'s0':9, 's2':10, 's3':11, 's4':12, 's5':13, 's6':14})
        # # layout.set_classifications({'NSIK LF':2, 'NSIK LT':3,  'NSIK LK':4, 'NSIK B':6, 'Uniclass':7})
        # layout.set_classifications({'Uniclass':5})

        layout.set_titles({'ifcType':'IFC tipas','name':'Elemento pav.', 'file':'PROJEKTO DALIS', 
                'NSIK LF':'Funkcinės sistemos kodas - ClassificationSystemCF arba „ISO81346 CF“ klasifikatorius',
                'NSIK LT':'Techninės sistemos kodas - ClassificationSystemCT arba „ISO81346 CT“ klasifikatorius',
                'NSIK LK':'Komponento kodas - ClassificationSystemCO arba „ISO81346 CO“ klasifikatorius',
                'NSIK B':'Erdvės kodas - ClassificationSystemCS arba „ISO81346 CS“ klasifikatorius',
                'Uniclass':'Uniclass2015 kodas',
                's0':'Esama situacija', 's2':'PP modeliai','s4':'TDP modeliai', 
                'classification':"Klasifikatoriai", 'LOD':"LOD"}
                )
        
    if output_flavour.upper() == 'BE-LIVE':
        report.title = "LOI"
        layout.flavour = output_flavour
        report.set_special_handling_aspects(['classifications', 'stages', 'properties', 'nsik_name', 'description', 'examples', 'nsik_descr'])

        output_classification = 'NSIK'
        report.set_column_widths({'A':4.0, 'B':2.0, 'C':2.0, 'D':2.0, 'E':2.0, 'F':2.0, 'G':5.0, 'H':3.0, 
                                  'I':4.0, 'J':2.5, 'K':3.5, 'L':2.5, 'M':3.0, 'N':2.5, 'O':3.5, 'P':3.0,
                                  'M':4.0, 'U':4.0, 'AC':4.0, 'AK':4.0, 'AS':4.0, 'BA':4.0,
                                  'N':3.0, 'V':3.0, 'AD':3.0, 'AL':3.0, 'AT':3.0, 'BB':3.0,
                                  'O':2.2, 'W':2.2, 'AE':2.2, 'AM':2.2, 'AU':2.2, 'BC':2.2,
                                  'P':2.0, 'X':2.0, 'AF':2.0, 'AN':2.0, 'AV':2.0, 'BD':2.0,
                                  'Q':2.2, 'Y':2.2, 'AG':2.2, 'AO':2.2, 'AW':2.2, 'BE':2.2,
                                  'R':3.5, 'Z':3.5, 'AH':3.5, 'AP':3.5, 'AX':3.5, 'BF':3.5,
                                  'S':3.5, 'AA':3.5, 'AI':3.5, 'AR':3.5, 'AY':3.5, 'BG':3.5,
                                  'BH':2.5}
                                )
        layout.set_metas({'name':1, 'example':8, 'memo':11, 'ifcType':10, 'file':60})
        # layout.set_stages({'s0':12, 's2':20, 's3':28, 's4':36, 's5':44, 's6':52})
        
        layout.set_metas({'nsik_name':1 ,'name':7, 'description':8, 'examples':9, 'ifcType':10, 'memo':11, 'file':25})
        layout.set_stages({'s3':12})

        layout.set_relative_offsets({'properties': 1, 'uri': 2, 'prop_descr':3, 'prop_ifc_datatype':4, 'prop_datatype':5, 'prop_example':6, 'prop_allowed':7, 'prop_memo':8})
        # layout.set_classifications({'NSIK LF':2, 'NSIK LT':3,  'NSIK LK':4, 'NSIK B':6, 'Uniclass':7})
        layout.set_classifications({'NSIK LF':2, 'NSIK LT':3,  'NSIK LK':4, 'NSIK B':5, 'NSIK E':6})

        layout.set_titles({'ifcType':'IFC tipas', 'examples':'Modeliuojamų elementų pavyzdžiai', 'memo': "Pastabos", 'name': 'Pavadinimas', 'description':'Elemento aprašymas', 'nsik_descr':'Elemento aprašymas (NSIK)', 'file':'PROJEKTO DALIS', 
                           'properties_top':'Atributai ir savybės', 'properties':'Pavadinimas arba \nSavybių rinkinys.Pavadinimas', 'prop_descr':'Atributo ar savybės aprašymas', 'prop_allowed':'Leidžiamos reikšmės',
                           'prop_ifc_datatype':'IFC duomenų tipas', 'prop_datatype':'Duomenų tipas', 'prop_example':"Vertės pavyzdžiai",'prop_memo':'Pastabos', 'uri':'Nuoroda',
                           'nsik_name' : 'Komponento pavadinimas pagal NSIK klasifikatorių',
                'NSIK LF':'Funkcinės sistemos kodas - ClassificationSystem.NSIK LF arba „NSIK LF“ klasifikatorius',
                'NSIK LT':'Techninės sistemos kodas - ClassificationSystem.NSIK LT arba „NSIK LT“ klasifikatorius',
                'NSIK LK':'Komponento kodas - ClassificationSystemNSIK LK arba „NSIK LK“ klasifikatorius',
                'NSIK B':'Erdvės kodas - ClassificationSystem.NSIK B arba „NSIK B“ klasifikatorius',
                'NSIK E':'Statinio kodas - ClassificationSystem.NSIK E arba „NSIK E“ klasifikatorius',
                's0':'Esama situacija', 's2':'PP modeliai','s3':'TP modeliai', 's4':'TDP modeliai', 
                'classification':"Klasifikatoriai", 'LOD':"Pateikiama informacija",
                'String': 'Tekstas', 'Real':'Skaičius'}
                )
    
    if report_type.upper() == 'IDS':
        report.stage = stage
        
    report.prepare(output_flavour)
    report.publish(eir, layout)
    # eir.to_any(layout, report, current_row = current_row)

    # if report_type.upper() == 'IDS':
    #     pprint(report)

    # eir.to_console()

    output_file = F"{output_flavour}_EIR_{output_classification}_{datetime.date.today()}"
    
    try:
        
        report.save(F"{output_file}.{report_type}")
    except AssertionError:
        pass

    return F"{output_file}.{report_type}"

def pprint(report):
    # print(report.__dict__)
    # print(report.__report__.__dict__)

    # print(report.__report__.specifications)
    for spec in report.__report__.specifications:
        # print(F"\t{spec.__dict__}")
        print(F"\n#{spec.identifier}', name: '{spec.name}', IFC version: {spec.ifcVersion}")
        for app in spec.applicability:
            # print(F"\t{app.__dict__} of type {type({app})}")
            if isinstance (app, Restriction):
                print(F"\tRESTR: {app.__dict__}")
            elif hasattr(app, 'parameters'):
                if hasattr(app.parameters, 'name'):
                    print(F"\t APP: name: '{app.name}'")
            else:
                print(F"\t{app.__dict__} of type {type({app})}")
                
        for req in spec.requirements:
            if isinstance(req, Property):
                print(F"\t REQ: P_set: {req.propertySet}, baseName: {req.baseName}, value: {req.value}, datatype: {req.dataType}, URI: {req.uri}, cardinality: {req.cardinality}")
            elif isinstance(req, Classification):
                print(F"\t CLASS: system: {req.system}, value: {req.value}")
            elif isinstance(req, Entity):
                print(F"\t ENTITY: name: {req.name}, predefinedType: {req.predefinedType}")
            else:
                print(F"\t {req}: {req.__dict__}")



if __name__ == "__main__":
    import yaml

    yaml_file = 'sandbox/project_lod_s2.yaml'
    yaml_file = 'sandbox/project_lod.yaml'
    yaml_file = 'sandbox/462.02_lod_s3.yaml'
    yaml_file = 'sandbox/L95_part.yaml'
    yaml_file = 'sandbox/Moravai.yaml'

    yaml_file = 'sandbox/Moravai_v2_ej.yaml'

    use_cases_file = 'sandbox/use_cases.yaml'
    project_file = 'sandbox/462.02_lod_s3.yaml'
    
    with open(project_file,'r', encoding='utf-8') as stream:
        try:
            data = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

    with open(use_cases_file,'r', encoding='utf-8') as stream:
        try:
            use_cases = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    # print(F"[{len(use_cases)}]: {use_cases}")
    if len(use_cases) > 0:
        data['useCases'] = use_cases


    
    with open(yaml_file,'r', encoding='utf-8') as stream:
        try:
            loin = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    if len(loin) > 0:
        data['loin'] = loin['loin']
        if 'properties' in loin.keys():
            data['project']['properties'] = loin['properties']
            # print(F"Merging 'properties' from '{yaml_file}': {data['project']['properties'].keys()=}")

       

    
        
    # if 'loin' in data.keys():
    #     __loin__  = data['loin']

    # if 'project' in data.keys():
    #     __project__  = data['project']

    output_flavour = 'VVK'
    output_flavour = 'SKST'
    output_flavour = 'BE-LIVE'

    # report_type = 'ids'
    report_type = 'xlsx'

    # stage = 's4'
    # stage = 's5'
    stage = 's6'
    stage = 's3'
    
    res = main(EIR(data), output_flavour=output_flavour, report_type=report_type, stage=stage)
    print(F"\n\tOutput file: {res}\n")
    
