from django.db import models

class CarMake(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    country = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    model = models.CharField(max_length=30)
    dealer_id = models.IntegerField()
    CAR_TYPE_CHOICES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
    ]
    car_type = models.CharField(max_length=20, choices=CAR_TYPE_CHOICES)
    year = models.DateField()
    color = models.CharField(max_length=10)

    def __str__(self):
        return self.model


class CarDealer(models.Model):
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    full_name = models.CharField(max_length=100)
    dealer_id = models.IntegerField(primary_key=True)
    lat = models.FloatField()
    long = models.FloatField()
    short_name = models.CharField(max_length=50)
    st = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return f"Dealer name: {self.full_name}"


class DealerReview(models.Model):
    dealership = models.ForeignKey(CarDealer, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    purchase = models.BooleanField()
    review = models.TextField()
    purchase_date = models.DateField()
    car_make = models.CharField(max_length=30)
    car_model = models.CharField(max_length=30)
    car_year = models.IntegerField()
    SENTIMENT_CHOICES = [
        ('POSITIVE', 'Positive'),
        ('NEUTRAL', 'Neutral'),
        ('NEGATIVE', 'Negative'),
    ]
    sentiment = models.CharField(max_length=10, choices=SENTIMENT_CHOICES)

    def __str__(self):
        return f"Dealer Review: {self.sentiment}"

# models.py

from django.db import models

class DealerReview(models.Model):
    dealership = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    purchase = models.BooleanField()
    review = models.TextField()
    purchase_date = models.DateField()
    car_make = models.CharField(max_length=50)
    car_model = models.CharField(max_length=50)
    car_year = models.IntegerField()
    sentiment = models.CharField(max_length=20)
    id = models.IntegerField(primary_key=True)  # Assuming id is the primary key

    def __str__(self):
        return f"Review for {self.dealership} by {self.name}"
