import tkinter as tk
from tkinter import ttk
from collections import defaultdict

# Dictionary to store the mapping of symptoms to conditions
symptom_to_condition = {
    'pulsating feeling in stomach': ['Abdominal Aortic Aneurysm'],
    'back pain': ['Abdominal Aortic Aneurysm', 'Addisons disease', 'Angina', 'Ankylosing spondylitis'],
    'abdominal pain': ['Abdominal Aortic Aneurysm', 'Acute lymphoblastic leukaemia', 'Acute pancreatitis', 'Addisons disease', 'Alcohol related liver disease', 'Allergies', 'Anaphylaxis', 'Angioedema', 'Anorexia nervosa'],
    'dizziness': ['Abdominal Aortic Aneurysm', 'Acute lymphoblastic leukaemia', 'Addisons disease', 'Anorexia nervosa', 'Anxiety', 'Atrial fibrillation'],
    'sweating': ['Abdominal Aortic Aneurysm', 'Acute Cholecystitis', 'Acute myeloid leukaemia', 'Addisons disease', 'Anxiety'],
    'rapid heartbeat': ['Abdominal Aortic Aneurysm'],
    'tachycardia': ['Abdominal Aortic Aneurysm', 'Anxiety', 'Atrial fibrillation'],
    'fast heartbeat': ['Abdominal Aortic Aneurysm', 'Anxiety', 'Atrial fibrillation'],
    'shortness of breath': ['Abdominal Aortic Aneurysm', 'Acute lymphoblastic leukaemia', 'Acute myeloid leukaemia', 'Addisons disease', 'Allergies', 'Anxiety', 'Asbestosis', 'Asthma', 'Atrial fibrillation'],
    'feeling faint': ['Abdominal Aortic Aneurysm', 'Addisons disease', 'Allergies', 'Anaphylaxis', 'Atrial fibrillation'],
    'loss of consciousness': ['Abdominal Aortic Aneurysm', 'Addisons disease', 'Allergies', 'Anaphylaxis'],
    'swelling': ['Achilles Tendinopathy', 'Alcohol related liver disease', 'Allergies', 'Angioedema', 'Anorexia nervosa'],
    'pain that’s worse during or after moving or exercising' : ['Achilles Tendinopathy'],
    'stiffness that’s worse in the morning or after a period of rest': ['Achilles Tendinopathy'],
    'tenderness to touch the affected area': ['Achilles Tendinopathy'],
    'mild heat': ['Achilles Tendinopathy'],
    'ankle weakness': ['Achilles Tendinopathy', 'Ankle sprain'],
    'foot weakness': ['Achilles Tendinopathy'],
    'blackheads': ['Acne'],
    'whiteheads': ['Acne'],
    'papules': ['Acne'],
    'pustules': ['Acne'],
    'nodules': ['Acne'],
    'cysts': ['Acne'],
    'fever': ['Acute Cholecystitis', 'Acute lymphoblastic leukaemia', 'Acute myeloid leukaemia', 'Acute pancreatitis', 'Alcohol related liver disease', 'Appendicitis'],
    'nausea': ['Acute Cholecystitis', 'Acute pancreatitis', 'Addisons disease', 'Anaphylaxis', 'Angioedema', 'Appendicitis'],
    'vomiting': ['Acute Cholecystitis', 'Acute lymphoblastic leukaemia', 'Acute pancreatitis', 'Addisons disease', 'Alcohol related liver disease', 'Allergies', 'Anaphylaxis', 'Angioedema'],
    'loss of appetite': ['Acute Cholecystitis', 'Addisons disease', 'Alcohol related liver disease', 'Appendicitis'],
    'jaundice': ['Acute Cholecystitis', 'Acute pancreatitis', 'Alcohol related liver disease'],
    'lump in abdomen': ['Acute Cholecystitis'],
    'pale skin': ['Acute lymphoblastic leukaemia','Acute myeloid leukaemia', 'Addisons disease'],
    'tired': ['Acute lymphoblastic leukaemia', 'Acute myeloid leukaemia', 'Addisons disease', 'Anorexia nervosa', 'Anxiety', 'Ataxia', 'Atrial fibrillation'],
    'multiple infections': ['Acute lymphoblastic leukaemia', 'Acute myeloid leukaemia'],
    'bleeding gums': ['Acute lymphoblastic leukaemia', 'Acute myeloid leukaemia', 'Alcohol related liver disease'],
    'nose bleed': ['Acute lymphoblastic leukaemia', 'Acute myeloid leukaemia', 'Alcohol related liver disease'],
    'night sweats': ['Acute lymphoblastic leukaemia'],
    'bone pain': ['Acute lymphoblastic leukaemia', 'Acute myeloid leukaemia'],
    'joint pain': ['Acute lymphoblastic leukaemia', 'Acute myeloid leukaemia', 'Addisons disease', 'Ankylosing spondylitis', 'Arthritis'],
    'easily bruised skin': ['Acute lymphoblastic leukaemia', 'Acute myeloid leukaemia', 'Alcohol related liver disease'],
    'swollen lymph nodes': ['Acute lymphoblastic leukaemia'],
    'weight loss': ['Acute lymphoblastic leukaemia', 'Acute myeloid leukaemia', 'Addisons disease', 'Alcohol related liver disease'],
    'purple skin rash': ['Acute lymphoblastic leukaemia', 'Acute myeloid leukaemia'],
    'headache': ['Acute lymphoblastic leukaemia', 'Addisons disease', 'Anxiety'],
    'seizure' : ['Acute lymphoblastic leukaemia'],
    'blurred vision': ['Acute lymphoblastic leukaemia', 'Ataxia'],
    'petechiae': ['Acute myeloid leukaemia'],
    'feeling of fullness': ['Acute myeloid leukaemia'],
    'discomfort in stomach': ['Acute myeloid leukaemia', 'Acute pancreatitis', 'Adenomyosis'],
    'stomach pain': ['Acute pancreatitis', 'Allergies', 'Anorexia nervosa', 'Anxiety'],
    'stomach ache': ['Acute pancreatitis', 'Allergies', 'Anorexia nervosa', 'Anxiety'],
    'diarrhea': ['Acute pancreatitis', 'Addisons disease', 'Alcohol related liver disease', 'Allergies', 'Angioedema', 'Appendicitis'],
    'indigestion': ['Acute pancreatitis'],
    'fatigue': ['Addisons disease', 'Alcohol related liver disease', 'Ankylosing spondylitis', 'Asbestosis', 'Ataxia'],
    'lethargy': ['Addisons disease'],
    'muscle weakness': ['Addisons disease', 'Alcohol related liver disease', 'Arthritis'],
    'depression': ['Addisons disease', 'Alzheimers disease'],
    'irritability': ['Addisons disease', 'Anxiety'],
    'frequent urination': ['Addisons disease'],
    'thirst': ['Addisons disease'],
    'salty food craving': ['Addisons disease'],
    'dehydration': ['Addisons disease'],
    'low blood pressure': ['Addisons disease', 'Anorexia nervosa'],
    'muscle cramps': ['Addisons disease'],
    'exhaustion': ['Addisons disease'],
    'hyperpigmentation': ['Addisons disease'],
    'reduced libido': ['Addisons disease'],
    'cold skin': ['Addisons disease'],
    'clammy skin': ['Addisons disease'],
    'rapid breathing': ['Addisons disease'],
    'shallow breathing': ['Addisons disease'],
    'drowsiness': ['Addisons disease'],
    'heavy periods': ['Adenomyosis'],
    'period pain': ['Adenomyosis'],
    'pressure in tummy': ['Adenomyosis'],
    'bloating': ['Adenomyosis', 'Anorexia nervosa'],
    'feeling sick': ['Alcohol related liver disease', 'Allergies', 'Anxiety', 'Appendicitis'],
    'feeling generally unwell': ['Alcohol related liver disease'],
    'oedema': ['Alcohol related liver disease'],
    'swelling in abdomen': ['Alcohol related liver disease'],
    'shivering': ['Alcohol related liver disease'],
    'itchy skin': ['Alcohol related liver disease', 'Allergic rhinitis', 'Atopic eczema'],
    'hair loss': ['Alcohol related liver disease'],
    'clubbed fingers': ['Alcohol related liver disease', 'Asbestosis'],
    'curved fingers': ['Alcohol related liver disease'],
    'curved fingernails': ['Alcohol related liver disease'],
    'red palms': ['Alcohol related liver disease'],
    'weakness': ['Alcohol related liver disease'],
    'muscle loss': ['Alcohol related liver disease', 'Arthritis'],
    'confusion': ['Alcohol related liver disease', 'Allergies', 'Alzheimers disease'],
    'memory problems': ['Alcohol related liver disease', 'Alzheimers disease'],
    'insomnia': ['Alcohol related liver disease', 'Anxiety'],
    'changes in personality': ['Alcohol related liver disease'],
    'vomiting blood': ['Alcohol related liver disease'],
    'black stool': ['Alcohol related liver disease'],
    'sensitivity to alcohol': ['Alcohol related liver disease'],
    'sensitivity to drugs': ['Alcohol related liver disease'],
    'sneezing': ['Allergic rhinitis', 'Allergies'],
    'itchiness': ['Allergic rhinitis', 'Alcohol related liver disease', 'Allergies'],
    'blocked nose': ['Allergic rhinitis', 'Allergies'],
    'runny nose': ['Allergic rhinitis', 'Allergies'],
    'itchy nose': ['Allergic rhinitis', 'Allergies'],
    'itchy eyes': ['Allergies'],
    'red eyes': ['Allergies'],
    'watering eyes': ['Allergies'],
    'wheezing': ['Allergies', 'Anaphylaxis', 'Asbestosis', 'Asthma'],
    'chest tightness': ['Allergies', 'Angina', 'Asthma'],
    'cough': ['Allergies', 'Asbestosis', 'Asthma', 'Ataxia'],
    'hives': ['Allergies', 'Anaphylaxis', 'Angioedema'],
    'swollen lips': ['Allergies', 'Anaphylaxis', 'Angioedema'],
    'swollen tongue': ['Allergies', 'Anaphylaxis', 'Angioedema'],
    'swollen eyes': ['Allergies', 'Anaphylaxis', 'Angioedema'],
    'swollen face': ['Allergies', 'Anorexia nervosa'],
    'tummy pain': ['Allergies'],
    'dry skin': ['Allergies', 'Atopic eczema'],
    'red skin': ['Allergies', 'Arthritis', 'Atopic eczema'],
    'cracked skin': ['Allergies', 'Atopic eczema'],
    'swollen throat': ['Allergies', 'Anaphylaxis', 'Angioedema'],
    'swollen mouth': ['Allergies', 'Anaphylaxis'],
    'difficulty breathing': ['Allergies'],
    'lightheadedness': ['Allergies', 'Anaphylaxis', 'Anorexia nervosa'],
    'blue skin': ['Allergies'],
    'blue lips': ['Allergies'],
    'collapsing': ['Allergies', 'Anaphylaxis'],
    'disorientation': ['Alzheimers disease'],
    'difficulty making decisions': ['Alzheimers disease'],
    'problems with speech': ['Alzheimers disease'],
    'problems with language': ['Alzheimers disease'],
    'problems moving around': ['Alzheimers disease'],
    'problems with self-care': ['Alzheimers disease'],
    'stress': ['Alzheimers disease', 'Autism spectrum disorder'],
    'hallucinations': ['Alzheimers disease'],
    'delusions': ['Alzheimers disease'],
    'anxiety': ['Alzheimers disease', 'Autism spectrum disorder'],
    'rectal bleeding': ['Rectal cancer'],
    'anus itching': ['Rectal cancer'],
    'anus pain': ['Rectal cancer'],
    'lumps around anus': ['Rectal cancer'],
    'mucus from anus': ['Rectal cancer'],
    'bowel incontinence': ['Rectal cancer'],
    'swollen hands': ['Anaphylaxis', 'Angioedema', 'Anorexia nervosa'],
    'swollen feet': ['Anaphylaxis', 'Angioedema', 'Anorexia nervosa'],
    'chest pain': ['Angina', 'Asbestosis', 'Atrial fibrillation'],
    'heavy chest': ['Angina'],
    'chest ache': ['Angina'],
    'arm pain': ['Angina'],
    'neck pain': ['Angina'],
    'jaw pain': ['Angina'],
    'swollen genitals': ['Angioedema'],
    'swollen bowel': ['Angioedema'],
    'pricking sensation': ['Angioedema'],
    'hot sensation': ['Angioedema'],
    'painful sensation': ['Angioedema'],
    'swollen windpipe': ['Angioedema'],
    'swollen conjunctiva': ['Angioedema'],
    'bladder problems': ['Angioedema'],
    'difficulty urinating': ['Angioedema'],
    'ankle swelling': ['Ankle sprain'],
    'ankle pain': ['Ankle sprain'],
    'ankle redness': ['Ankle sprain', 'Arthritis'],
    'hot ankle': ['Ankle sprain'],
    'difficulty moving ankle': ['Ankle sprain'],
    'tingling ankle': ['Ankle sprain'],
    'ankle numbness': ['Ankle sprain'],
    'ankle pins and needles': ['Ankle sprain'],
    'back stiffness': ['Ankylosing spondylitis'],
    'arthritis': ['Ankylosing spondylitis'],
    'enthesitis': ['Ankylosing spondylitis'],
    'feat of being fat': ['Anorexia nervosa'],
    'problems with self-esteem': ['Anorexia nervosa'],
    'restricting food intake': ['Anorexia nervosa'],
    'low body weight': ['Anorexia nervosa'],
    'lanugo on body': ['Anorexia nervosa'],
    'excess hair on face': ['Anorexia nervosa'],
    'less pubic hair': ['Anorexia nervosa'],
    'slow heartbeat': ['Anorexia nervosa'],
    'bradycardia': ['Anorexia nervosa'],
    'irregular heartbeat:' : ['Anorexia nervosa', 'Anxiety', 'Atrial fibrillation'],
    'constipated': ['Anorexia nervosa'],
    'low body temperature': ['Anorexia nervosa'],
    'restlessness': ['Anxiety'],
    'sense of dread': ['Anxiety'],
    'feeling constantly on edge': ['Anxiety'],
    'difficulty concentrating': ['Anxiety','Attention deficit hyperactivity disorder'],
    'heart palpitations': ['Anxiety', 'Atrial fibrillation'],
    'muscle aches': ['Anxiety'],
    'muscle tension': ['Anxiety'],
    'shaking': ['Anxiety', 'Ataxia'],
    'trembling': ['Anxiety', 'Ataxia'],
    'dry mouth': ['Anxiety'],
    'pins and needles': ['Anxiety'],
    'being sick': ['Appendicitis'],
    'flushed face': ['Appendicitis'],
    'arterial thrombosis': ['Angina', 'Heart attack', 'Stroke', 'Peripheral vascular disease'],
    'joint tenderness': ['Arthritis'],
    'joint stiffness': ['Arthritis'],
    'joint inflammation': ['Arthritis'],
    'restricting movement in joints': ['Arthritis'],
    'warm skin around joints': ['Arthritis'],
    'clumsiness': ['Ataxia'],
    'slurred speech': ['Ataxia'],
    'difficulty swallowing': ['Ataxia'],
    'choking': ['Ataxia'],
    'jumpy vision': ['Ataxia'],
    'sore skin': ['Atopic eczema'],
    'chest discomfort': ['Atrial fibrillation'],
    'difficulty paying attention': ['Attention deficit hyperactivity disorder'],
    'hyperactivity': ['Attention deficit hyperactivity disorder'],
    'impulsiveness': ['Attention deficit hyperactivity disorder'],
    'atypical communication': ['Autism spectrum disorder'],
    'atypical interaction': ['Autism spectrum disorder'],
    'atypical experiencing of senses': ['Autism spectrum disorder'],
    'stress from social situations': ['Autism spectrum disorder'],
    'thrive in a familiar routine': ['Autism spectrum disorder'],
    'masking': ['Autism spectrum disorder'],
}

#INACTIVE - gets all conditions associated with any symptom
def get_conditions_for_symptoms(input_symptoms):
    result = set()
    for symptom in input_symptoms:
        if symptom in symptom_to_condition:
            result.update(symptom_to_condition[symptom])
    return list(result)

# Active
def get_most_associated_conditions(input_symptoms):
    # Count the occurrences of each symptom
    condition_counts = defaultdict(int)
    for symptom in input_symptoms:
        if symptom in symptom_to_condition:
            for condition in symptom_to_condition[symptom]:
                condition_counts[condition] += 1

    # If no symptoms found, return an empty list
    if not condition_counts:
        return []

    # Find the maximum count
    max_count = max(condition_counts.values())

    # Return symptoms with the maximum count
    return [condition for condition, count in condition_counts.items() if count == max_count]

class SymptomsToConditionsApp:
    def __init__(self, master):
        self.master = master
        master.title("What Do I Have?")
        master.geometry("1366x768")

        style = ttk.Style()
        style.theme_use('clam')

        # Configure styles
        style.configure('TFrame', background='#E8F5E9')
        style.configure('TLabel', font=('Helvetica', 24), foreground='#1B5E20', background='#E8F5E9')
        style.configure('TEntry', font=('Helvetica', 20), fieldbackground='#FFFFFF')
        style.configure('TButton', font=('Helvetica', 20), background='#4CAF50', foreground='#FFFFFF')
        style.map('TButton', background=[('active', '#45A049')])
        style.configure('TNotebook', background='#E8F5E9')
        style.configure('TNotebook.Tab', font=('Helvetica', 16), padding=[20, 10], background='#81C784', foreground='#1B5E20')
        style.map('TNotebook.Tab', background=[('selected', '#4CAF50')], foreground=[('selected', '#FFFFFF')])
        style.configure('Canvas.TFrame', background='#E8F5E9')
        style.configure('Small.TLabel', font=('Helvetica', 14), foreground='#1B5E20', background='#E8F5E9')

        # Create notebook
        self.notebook = ttk.Notebook(master)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Main page
        self.main_page = ttk.Frame(self.notebook, style='TFrame')
        self.notebook.add(self.main_page, text="Main")

        # Symptoms page
        self.symptoms_page = ttk.Frame(self.notebook, style='TFrame')
        self.notebook.add(self.symptoms_page, text="Recognized Symptoms")

        self.setup_main_page()
        self.setup_symptoms_page()

    def setup_main_page(self):
        main_frame = ttk.Frame(self.main_page, padding="20 20 20 20", style='TFrame')
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Add version number to top left
        version_label = ttk.Label(main_frame, text=f" Current Condition Database: Conditions Starting With A", font=('Helvetica', 14, 'italic'), style='Small.TLabel')
        version_label.pack(side=tk.TOP, anchor=tk.NW)

        #date
        database_label = ttk.Label(main_frame, text=f"Version 1.0.1", style='Small.TLabel')
        database_label.pack(side=tk.BOTTOM, anchor=tk.SE)

        title_label = ttk.Label(main_frame, text="What Do I Have?", font=('Helvetica', 36, 'bold'), style='TLabel')
        title_label.pack(pady=30)

        self.label = ttk.Label(main_frame, text="Enter symptoms in lowercase separated by commas:", style='TLabel')
        self.label.pack(pady=20)
        self.label = ttk.Label(main_frame, text="To see which symptoms are valid, please click 'Recognized Symptoms'", style='TLabel')
        self.label.pack(pady=20)

        self.entry = ttk.Entry(main_frame, width=80, style='TEntry')
        self.entry.pack(pady=20)

        button_frame = ttk.Frame(main_frame, style='TFrame')
        button_frame.pack(pady=20)

        self.find_button = ttk.Button(button_frame, text="Find Conditions", command=self.find_symptoms, style='TButton')
        self.find_button.pack(side=tk.LEFT, padx=10)

        self.quit_button = ttk.Button(button_frame, text="Quit", command=self.master.quit, style='TButton')
        self.quit_button.pack(side=tk.LEFT, padx=10)

        self.result_label = ttk.Label(main_frame, text="", style='TLabel', wraplength=1800)
        self.result_label.pack(pady=30)

        self.symptoms_label = ttk.Label(main_frame, text="", style='TLabel', wraplength=1800)
        self.symptoms_label.pack(pady=30)

    def setup_symptoms_page(self):
        symptoms_frame = ttk.Frame(self.symptoms_page, padding="20 20 20 20", style='TFrame')
        symptoms_frame.pack(fill=tk.BOTH, expand=True)

        title_label = ttk.Label(symptoms_frame, text="Recognized Symptoms", font=('Helvetica', 36, 'bold'), style='TLabel')
        title_label.pack(pady=30)

        # Add search bar
        search_frame = ttk.Frame(symptoms_frame, style='TFrame')
        search_frame.pack(fill=tk.X, pady=10)

        search_label = ttk.Label(search_frame, text="Search:", style='TLabel', font=('Helvetica', 20))
        search_label.pack(side=tk.TOP, padx=10)

        self.search_var = tk.StringVar()
        self.search_var.trace("w", self.update_list)
        search_entry = ttk.Entry(search_frame, textvariable=self.search_var, font=('Helvetica', 20), width=40)
        search_entry.pack(side=tk.TOP, padx=10)

        # Create a canvas with scrollbar
        self.canvas = tk.Canvas(symptoms_frame, bg='#E8F5E9', highlightthickness=0)
        scrollbar = ttk.Scrollbar(symptoms_frame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas, style='Canvas.TFrame')

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Initial population of the list
        self.update_list()

    def update_list(self, *args):
        # Clear the current list
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        # Get the search query
        search_query = self.search_var.get().lower()

        # Filter and sort identifiers
        filtered_symptoms = sorted(
            sym for sym in symptom_to_condition.keys()
            if search_query in sym.lower()
        )

        # Add filtered identifiers to the scrollable frame
        for symptom in filtered_symptoms:
            ttk.Label(self.scrollable_frame, text=symptom, style='TLabel', font=('Helvetica', 20)).pack(pady=5,anchor='w')


    def find_symptoms(self):
        input_text = self.entry.get()
        input_symptoms = [symptom.strip() for symptom in input_text.split(',')]

        result = get_most_associated_conditions(input_symptoms)

        if result:
            self.result_label.config(text=f"Most associated conditions: {', '.join(result)}")
        else:
            self.result_label.config(text="Invalid Symptom: This is not in our database of symptoms.\n To see symptoms in our database, click 'Recognized Symptoms'")


#INACTIVE
def parse_input(user_input):
    # Split the input by commas and strip whitespace from each symptom
    return [symptom.strip() for symptom in user_input.split(',')]


# Main program
if __name__ == "__main__":
    root = tk.Tk()
    app = SymptomsToConditionsApp(root)
    root.mainloop()