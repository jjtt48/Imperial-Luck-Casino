import json

def lambda_handler(event, context):
    politica = """
    Política de Tratamiento de Datos de Imperial Luck:
    
    1. Recopilación de datos: Recopilamos información personal necesaria para ofrecer nuestros servicios.
    2. Uso de datos: Utilizamos la información para mejorar la experiencia del usuario y cumplir con regulaciones legales.
    3. Compartición de datos: No compartimos datos personales con terceros sin su consentimiento explícito.
    4. Seguridad: Implementamos medidas de seguridad para proteger su información personal.
    5. Derechos del usuario: Puede solicitar acceso, corrección o eliminación de sus datos en cualquier momento.

    Por favor, lea esta política cuidadosamente. Para continuar usando nuestros servicios, debe aceptar los términos de esta política.
    """

    
    try:
        action = event['action'].lower()

        if action == "mostrar_politica":
            return {
                'statusCode': 200,
                'body': json.dumps({'politica': politica})
            }
        elif action == "aceptar":
           return {
                'statusCode': 200,
                'body': json.dumps({'mensaje': "Aceptación registrada. Puede continuar usando el servicio."})
            }
        elif action == "rechazar":
            return {
                'statusCode': 403,
                'body': json.dumps({'mensaje': "No aceptó los términos. No podrá usar el servicio."})
            }
        else:
            return {
                'statusCode': 400,
                'body': json.dumps({'mensaje': "Acción no válida."})
            }
    except KeyError:
        return {
            'statusCode': 400,
            'body': json.dumps({'mensaje': "El campo 'action' es requerido en el evento."})
        }
