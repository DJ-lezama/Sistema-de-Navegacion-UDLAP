places = ["CE", "AU", "BI", "CS", "IA", "CN", "NE", "HA", "LB", "GB", "TD", "SL", "HU", "AG"]
places_display_name = ["Centro Estudiantil", "Auditorio", "Biblioteca", "Ciencias Sociales", "Ingeniería", "Ciencias",
                       "Negocios", "Hacienda", "Laboratorio B-34", "Gimnasio de Pesas", "Templo del Dolor",
                       "Ciencias de la Salud", "Humanidades", "Ágora"]

distances = {
    ("CE", "AU"): 101.86,  # Centro Social a Auditorio
    ("CE", "CS"): 52.93,   # Centro Social a Ciencias Sociales
    ("CE", "CN"): 119.35,  # Ingeniería a Ciencias
    ("IA", "LB"): 21.4,    # Ingeniería a Biblioteca
    ("IA", "AU"): 140.00,  # Ingeniería a Auditorio
    ("SL", "CE"): 154.55,  # Ciencias de la Salud a Centro Estudiantil
    ("SL", "TD"): 42.79,   # Ciencias de la Salud a Templo del Dolor
    ("HA", "HU"): 70.08,   # Hacienda a Humanidades
    ("AU", "CS"): 98.21,   # Auditorio a Ciencias Sociales
    ("CS", "NE"): 46.11,   # Ciencias Sociales a Negocios
    ("IA", "AU"): 121.92,  #Ingeniería a Auditorio
    ("CN","IA"): 47.9,     #Ciencias a Ingeniera
    ("AU", "HA"): 96.99,   #Auditorio a Hacienda
    ("BI", "CE"): 72.66,   #Biblioteca a Centro Estudiantil
    ("BI", "CN"): 78.41,   #Biblioteca a Ciencias
    ("SL", "TD"): 42.79,   #Ciencias de la Salud a Templo del Dolor
    ("GB", "TD"): 112.35,  #Gimnasio de Pesas a Templo del Dolor
    ("AG", "HU"): 21.47,   #Ágora a Humanidades
    ("HA", "AG"): 73.9,
}
