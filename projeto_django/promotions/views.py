from django.shortcuts import render

def index(request):
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
        {
            "image": "img/quarto4.jpg",
            "title": "Maceió, Brasil",
            "location": "Ponta Verde",
            "dates": "20 – 25 de ago.",
            "price": "R$750",
        },
        {
            "image": "img/quarto5.jpg",
            "title": "Maceió, Brasil",
            "location": "Centro",
            "dates": "3 – 8 de set.",
            "price": "R$990",
        },
        {
            "image": "img/quarto6.jpg",
            "title": "Maceió, Brasil",
            "location": "Praia de Cruz das Almas",
            "dates": "15 – 20 de nov.",
            "price": "R$1.100",
        }
    ]
    return render(request, 'quartos/index.html', {'rooms': rooms})
