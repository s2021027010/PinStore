# Generated by Django 4.2.1 on 2023-12-19 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="db_Accessories",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("db_Access_ID", models.CharField(max_length=100)),
                ("db_Access_UseFor", models.TextField(max_length=255)),
                ("db_Access_Category", models.TextField(max_length=255)),
                ("db_Access_genderBase", models.TextField(max_length=255)),
                ("db_Access_ageBase", models.TextField(max_length=255)),
                ("db_Access_Extra", models.TextField(max_length=255)),
                ("db_Access_color", models.TextField(max_length=255)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="db_Cloth",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("db_Cloth_ID", models.CharField(max_length=100)),
                ("db_Cloth_color", models.TextField(max_length=255)),
                ("db_Cloth_genderBase", models.TextField(max_length=255)),
                ("db_Cloth_ageBase", models.TextField(max_length=255)),
                ("db_Cloth_Extra", models.TextField(max_length=255)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="db_Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("db_Comment_ID", models.CharField(max_length=100)),
                ("db_Comment_Sender", models.CharField(max_length=100)),
                ("db_Comment_Text", models.TextField(max_length=1000)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="db_Computer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("db_Computer_ID", models.CharField(max_length=100)),
                ("db_Computer_Store_RAM", models.TextField(max_length=255)),
                ("db_Computer_Store_ROM", models.TextField(max_length=255)),
                ("db_Computer_OS", models.TextField(max_length=255)),
                ("db_Computer_Camera", models.TextField(max_length=255)),
                ("db_Computer_Color", models.TextField(max_length=255)),
                ("db_Computer_BatteryTiming", models.TextField(max_length=255)),
                ("db_Computer_Card", models.TextField(max_length=255)),
                ("db_Computer_Charger", models.TextField(max_length=255)),
                ("db_Computer_Resolution", models.TextField(max_length=255)),
                ("db_Computer_Extra", models.TextField(max_length=255)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "db_photo",
                    models.ImageField(
                        blank=True, max_length=255, upload_to="media/Computer/"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="db_Message_Admin",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("db_message_sender", models.CharField(max_length=100)),
                ("db_message_reciever", models.CharField(max_length=100)),
                ("db_Message_Text", models.TextField(max_length=1000)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="db_Mobile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("db_Mobile_ID", models.CharField(max_length=100)),
                ("db_Mobile_Store_RAM", models.TextField(max_length=255)),
                ("db_Mobile_Store_ROM", models.TextField(max_length=255)),
                ("db_Mobile_OS", models.TextField(max_length=255)),
                ("db_Mobile_Camera", models.TextField(max_length=255)),
                ("db_Mobile_Color", models.TextField(max_length=255)),
                ("db_Mobile_BatteryTiming", models.TextField(max_length=255)),
                ("db_Mobile_Card", models.TextField(max_length=255)),
                ("db_Mobile_Charger", models.TextField(max_length=255)),
                ("db_Mobile_Resolution", models.TextField(max_length=255)),
                ("db_Mobile_Extra", models.TextField(max_length=255)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="db_Place_Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("product_id_order", models.CharField(max_length=100)),
                ("email_user", models.CharField(max_length=100)),
                ("email_order", models.CharField(max_length=100)),
                ("fname_order", models.TextField(max_length=100)),
                ("lname_order", models.TextField(max_length=100)),
                ("company_name_order", models.TextField(max_length=100)),
                ("country_order", models.TextField(max_length=100)),
                ("street_address_order", models.TextField(max_length=100)),
                ("appartment_order", models.TextField(max_length=100)),
                ("city_address_order", models.TextField(max_length=100)),
                ("state_order", models.TextField(max_length=100)),
                ("phone_order", models.TextField(max_length=100)),
                ("postCode_order", models.TextField(max_length=100)),
                ("cash_on", models.TextField(max_length=100)),
                ("status_order", models.TextField(max_length=100)),
                ("price_order", models.IntegerField()),
                ("quantity_order", models.IntegerField()),
                ("card_number", models.CharField(max_length=100)),
                ("card_Holder_name", models.CharField(max_length=100)),
                ("card_expDate", models.CharField(max_length=100)),
                ("card_ccv", models.CharField(max_length=10)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="db_Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("db_Product_ID", models.CharField(max_length=100)),
                ("db_Product_Name", models.TextField(max_length=255)),
                ("db_Product_Type", models.TextField(max_length=255)),
                ("db_Product_Category", models.TextField(max_length=255)),
                ("db_Product_Price", models.IntegerField()),
                ("db_Product_status", models.TextField(max_length=255)),
                ("db_Product_Brand", models.TextField(max_length=255)),
                ("db_Product_Size", models.TextField(max_length=255)),
                ("db_Product_Freshnes", models.TextField(max_length=255)),
                ("db_Product_MadeByCountry", models.TextField(max_length=255)),
                ("db_Product_Condition", models.TextField(max_length=255)),
                ("db_Product_Description", models.TextField(max_length=255)),
                ("db_Product_QR_Code", models.TextField(max_length=255)),
                ("db_Product_IssueDate", models.DateField(blank=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="db_Product_Image",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("db_Image_ID", models.CharField(max_length=100)),
                (
                    "db_Product_photo",
                    models.ImageField(blank=True, max_length=255, upload_to="Product/"),
                ),
                (
                    "list1_img",
                    models.ImageField(blank=True, max_length=255, upload_to="Product/"),
                ),
                (
                    "list2_img",
                    models.ImageField(blank=True, max_length=255, upload_to="Product/"),
                ),
                (
                    "list3_img",
                    models.ImageField(blank=True, max_length=255, upload_to="Product/"),
                ),
                (
                    "list4_img",
                    models.ImageField(blank=True, max_length=255, upload_to="Product/"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="db_Product_Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("db_order_ID", models.CharField(max_length=100)),
                ("db_order_email", models.CharField(max_length=255)),
                ("db_order_quantity", models.IntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="db_Review",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("db_Review_ID", models.CharField(max_length=100)),
                ("db_Review_email", models.CharField(max_length=100)),
                ("db_Review_Text", models.IntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="db_Shoes",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("db_Shoes_ID", models.CharField(max_length=100)),
                ("db_Shoes_color", models.TextField(max_length=255)),
                ("db_Shoes_genderBase", models.TextField(max_length=255)),
                ("db_Shoes_ageBase", models.TextField(max_length=255)),
                ("db_Shoes_Extra", models.TextField(max_length=255)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="db_Tv",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("db_Tv_ID", models.CharField(max_length=100)),
                ("db_Tv_Inches", models.TextField(max_length=255)),
                ("db_Tv_color", models.TextField(max_length=255)),
                ("db_Tv_Resolution", models.TextField(max_length=255)),
                ("db_Tv_Extra", models.TextField(max_length=255)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="db_Watch",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("db_Watch_ID", models.CharField(max_length=100)),
                ("db_Watch_color", models.TextField(max_length=255)),
                ("db_Watch_genderBase", models.TextField(max_length=255)),
                ("db_Watch_ageBase", models.TextField(max_length=255)),
                ("db_Watch_Extra", models.TextField(max_length=255)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="db_Wishlist",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("db_Wishlist_ID", models.CharField(max_length=100)),
                ("db_Wishlist_email", models.CharField(max_length=100)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
