from Curso import Curso

curso1 = Curso("PyTorch for Deep Learning Bootcamp","Andrei Neagoie, Daniel Bourke","4,6","$12.99")
curso1.categoria = "BESTSELLER" #Get de mi categoria
curso2 = Curso("Machine Learning A-Z: AI, Python & R + ChatGPT Prize","Kirill Eremenko, Hadelin de Ponteves","4.5","$14.99")
curso2.categoria = "BESTSELLER"
curso3 = Curso("Deep Learning: Advanced Computer Vision (GANs, SSD)","Lazy Programmer INC.","4.6","$14.99")
curso4 = Curso("Applied Generative AI and Natural Language Processing","Bert Gollnick","4.7","$12.99")
curso4.categoria = "Hot & new"
curso1.imprimir()
curso2.imprimir()
curso3.imprimir()
curso4.imprimir()