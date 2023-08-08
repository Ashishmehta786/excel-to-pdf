from django.shortcuts import render,HttpResponse
import os 
from .main import Liver, Thyroid, Diabetes, Kidney, Lipid_Cholestrol, Vitamin_B12, Vitamin_D25, Iron, Bone_Care, Cardiac_Care

def handle_uploaded_file(file):
    upload_dir = os.path.join('media', 'uploads')

    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)

    file_path = os.path.join(upload_dir, file.name)

    with open(file_path, 'wb') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    return file_path

def upload1(request):
    if request.method == 'POST' and request.FILES.get('excel_file'):
        excel_file = request.FILES['excel_file']

        if not excel_file.name.endswith('.xlsx'):
            return render(request, 'base.html', {'error_message': 'Invalid file type. Please upload an Excel file with .xlsx extension.'})

        file_path = handle_uploaded_file(excel_file)

        # Process the uploaded Excel file as needed.
        # For example, you can read the data using pandas, openpyxl, etc.

         # Handling the selected items
        selected_items = request.POST.getlist('selected_items')
        if selected_items:
            # Save the selected_items list to a variable or process them as needed
            # For example, you can save them to a variable named "selected_items_list"
            selected_items_list = selected_items
        else:
            # No items selected
            selected_items_list = []
        print("Selected Items List:", selected_items_list)


        return render(request, 'base.html', {'success_message': 'File uploaded successfully.', 'file_path': file_path, 'selected_items_list': selected_items_list})

    return render(request, 'base.html')
def result_page(request):

   def result(request):
    if request.method == 'POST' and request.POST.get('selected_items') and request.POST.get('file_path'):
        selected_items = request.POST.get('selected_items')
        file_path = request.POST.get('file_path')

        # Here you can call the main functions based on the selected_items
        # For example, if 'Liver' is selected, you can call Liver() function from main.py
        if selected_items == 'Liver':
            result = Liver()
        elif selected_items == 'Thyroid':
            result = Thyroid()
        elif selected_items == 'Diabetes':
            result = Diabetes()
        elif selected_items == 'Kidney':
            result = Kidney()
        elif selected_items == 'Lipid_Cholesterol':
            result = Lipid_Cholesterol()
        elif selected_items == 'Vitamin_B12':
            result = Vitamin_B12()
        elif selected_items == 'Vitamin_D25':
            result = Vitamin_D25()
        elif selected_items == 'Iron':
            result = Iron()
        elif selected_items == 'Bone_Care':
            result = Bone_Care()
        elif selected_items == 'Cardiac_Care':
            result = Cardiac_Care()

        if result:
            list1, major_function, causes, img = result

            # Processing the uploaded Excel file
            df = pd.read_excel(file_path)
            # You can now use 'df' to further process the data as needed.
            # For example, you can analyze the data, generate reports, etc.

            return render(request, 'result.html', {'list1': list1, 'major_function': major_function, 'causes': causes, 'img': img})

    return HttpResponse("Invalid request or selected item not found.")