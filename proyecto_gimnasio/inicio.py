class Usuario:

    def __init__(self, nombre:str, correo, membresia, t_documento, n_documento):
        self.nombre = nombre
        self.correo = correo
        self.membresia = membresia
        self.t_documento = t_documento
        self.n_documento = n_documento
        self.membresias = []
        self.medidas = []
        self.asistencias = []

    def estado_membresia(self, membresia, fecha_inicio, fecha_final):
        self.membresias.append(Membresia(membresia, fecha_inicio, fecha_final))

    def medidas_usuarios(self, altura, peso, medidas_corporales, fecha_registro):
        self.medidas.append(Medidas(altura, peso, medidas_corporales, fecha_registro))
    
    def asistencias_usuario(self, fecha, hora_entrada, hora_salida, duracion_entrenamiento):
        self.asistencias.append(Asistencia(fecha, hora_entrada, hora_salida, duracion_entrenamiento))


class Membresia:
    def __init__(self, membresia, fecha_inicio, fecha_final):
        self.membresia = membresia
        self.fecha_inicio = fecha_inicio
        self.fecha_final = fecha_final
        self.estado = "Activo"

    def congelar(self, fecha_congelar):
        self.estado = "Congelar"
        self.fecha_congelar = fecha_congelar
    
    def cancelar(self):
        self.estado = "Inactivo"

class Medidas:
    def __init__(self, altura, peso, medidas_corporales, fecha_registro):
        self.altura = altura
        self.peso = peso
        self.medidas_corporales = medidas_corporales
        self.fecha_registro = fecha_registro


class Asistencia:
    def __init__(self, fecha, hora_entrada, hora_salida, duracion_entrenamiento):
        self.fecha = fecha
        self.hora_entrada = hora_entrada
        self.hora_salida = hora_salida
        self.duracion_entrenamiento = duracion_entrenamiento


class Invitado:
    def __init__(self, nombre, correo, t_documento, n_documento):
        self.nombre = nombre
        self.correo = correo
        self.t_documento = t_documento
        self.n_documento = n_documento


class Gimnasio:
    def __init__(self):
        self.usuarios = []
    
    def registrar_usuario(self, nombre, correo, membresia, t_documento, n_documento):
        usuario = Usuario(nombre, correo, membresia, t_documento, n_documento)
        self.usuarios.append(usuario)
        return usuario
    
    def pase_invitado(self, nombre, correo, t_documento, n_documento):
        self.nombre = nombre
        self.correo = correo
        self.t_documento = t_documento
        self.n_documento = n_documento

    def generar_informe(self, usuario):
        informe = []
        informe.append("Informe del usuario:")
        informe.append("Nombre: {}". format(usuario.nombre))
        informe.append("Correo: {}". format(usuario.correo))
        informe.append("Tipo de documento: {}". format(usuario.t_documento))
        informe.append("Número de documento: {}". format(usuario.n_documento))

        informe.append("\nInformación de membresía:")
        for membresia in usuario.membresias:
            informe.append("Estado de membresía: {}". format(membresia.estado))
            informe.append("Fecha de inicio: {}". format(membresia.fecha_inicio))
            informe.append("Fecha final: {}". format(membresia.fecha_final))
        
        informe.append("\nMedidas:")
        for medida in usuario.medidas:
            informe.append("Fecha de registro: {}". format(medida.fecha_registro))
            informe.append("Altura: {}". format(medida.altura))
            informe.append("Peso: {}". format(medida.peso))
            informe.append("Medidas corporales: {}". format(medida.medidas_corporales))


        informe.append("\nAsistencias:")
        for asistencias in usuario.asistencias:
            informe.append("Fecha: {}". format(asistencias.fecha))
            informe.append("Hora de entrada: {}". format(asistencias.hora_entrada))
            informe.append("Hora de salida: {}". format(asistencias.hora_salida))
            informe.append("Duración del entrenamiento: {}". format(asistencias.duracion_entrenamiento))

        return "\n".join(informe)
    

#Ejemplo de uso
gimnasio = Gimnasio()

usuario1 = gimnasio.registrar_usuario("Fredy Rojo", "fredyrojo@gmail.com", "Gold", "Cédula", "113342423")
usuario1.estado_membresia("Gold", "20/05/2023", "20/05/2024")
usuario1.medidas_usuarios("183cm", "74 kilos", "Cintura 80cm", "26/05/2023")
usuario1.asistencias_usuario("23/06/2023","9am","11am","1 hora 20 minutos")

print(gimnasio.generar_informe(usuario1))

