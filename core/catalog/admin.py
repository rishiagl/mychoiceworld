from django.contrib import admin, messages

from .models import Brand, Category, Product, GstClassification

from django.utils.text import slugify

from fpdf import FPDF


admin.site.site_header = "Complete Enterprise Resource Management Software"
admin.site.site_title = "CERMS"
admin.site.index_title = "Administration Panel"


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_name')


admin.site.register(Brand, BrandAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_name')


admin.site.register(Category, CategoryAdmin)

pdf_w = 210
pdf_h = 297


class PDF(FPDF):
    def addText(self, x, y, text):
        self.set_font('Arial', '', 10)
        self.text(x, y, text)


def Download_QR_Code(modeladmin, request, queryset):
    pdf = PDF(orientation='P', unit='mm', format='A4')
    pdf = PDF()
    pdf.add_page()
    pdf.addText(10, 10, "Hello World!")
    pdf.output("text.pdf", 'F')
    modeladmin.message_user(
        request, "Selected products have been marked as discounted.", messages.SUCCESS)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'brand', 'category', 'gst_classification')
    readonly_fields = ('name',)
    list_filter = ["brand", "category"]
    search_fields = ("model__startswith",)
    actions = [Download_QR_Code]

    def get_readonly_fields(self, request, obj=None):
        if obj is None:  # This is an add operation
            return ()
        return self.readonly_fields


admin.site.register(Product, ProductAdmin)


class GstClassificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'type', 'rate')

    def name(self, obj):
        return obj


admin.site.register(GstClassification, GstClassificationAdmin)
