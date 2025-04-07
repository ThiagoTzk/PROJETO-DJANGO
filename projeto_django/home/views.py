from django.shortcuts import render

def home_view(request):
    return render(request, "home/home.html")

def quartos_view(request):
    rooms = [
        {
            "image": "img/quarto1.jpg",
            "title": "Maragogi, Brasil",
            "location": "Praia do Camacho",
            "dates": "9 – 14 de mar.",
            "price": "R$1.149",
        },
        {
            "image": "img/quarto2.jpg",
            "title": "Jatiúca, Brasil",
            "location": "Ponta Verde",
            "dates": "5 – 10 de abr.",
            "price": "R$899",
        },
        {
            "image": "img/quarto3.jpg",
            "title": "Maceió, Brasil",
            "location": "Ponta Verde",
            "dates": "12 – 18 de jun.",
            "price": "R$1.299",
        },
    ]

    return render(request, "quartos/listagem_quartos.html", {"rooms": rooms})

def quartos_detalhes(request):
    quarto = {
        "image": "img/quarto1.jpg",
        "title": "Maragogi, Brasil",
        "location": "Praia do Camacho",
        "dates": "9 – 14 de mar.",
        "price": "R$1.149",
        "description": "Quarto aconchegante com vista para o mar.",
        "locatario": {
            "foto": "img/locatario.jpg",
            "nome": "João Silva",
            "email": "joao.silva@hotmail.com",
            "telefone": "(82) 91234-5678"
        }
    }

    return render(request, "quartos/quartos_detalhes.html", {"quarto": quarto})
