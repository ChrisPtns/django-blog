# Django Blog

Ένα πλήρες project δημιουργίας ενός Blog με το framework Django.

## Τι περιλαμβάνει
Το project έχει υλοποιηθεί σε δύο επίπεδα (Backend & Frontend):

**Backend (Βάση & Διαχείριση):**
- Δημιουργία του κεντρικού project (`mysite`) και της εφαρμογής (`blog`)
- Μοντέλο `Post` στη βάση δεδομένων για την αποθήκευση των άρθρων
- Πλήρως λειτουργικό περιβάλλον διαχείρισης (Admin Panel) με δυνατότητες αναζήτησης, φιλτραρίσματος και ταξινόμησης

**Frontend (Διεπαφή Χρήστη):**
- Σύστημα URL routing για την πλοήγηση μεταξύ της λίστας άρθρων και της προβολής μεμονωμένων άρθρων
- Δημιουργία Views (`post_list`, `post_detail`)
- Σχεδιασμός HTML Templates (`base.html`, `list.html`, `detail.html`) με χρήση template inheritance

## Πώς να το τρέξετε τοπικά

1. Εγκαταστήστε το Django στο περιβάλλον σας:
   `pip install django`

2. Εφαρμόστε τις αλλαγές στη βάση δεδομένων:
   `python manage.py migrate`

3. Σηκώστε τον server:
   `python manage.py runserver`

4. Ανοίξτε τον browser σας στις εξής διευθύνσεις:
   - Για να δείτε το blog: `http://127.0.0.1:8000/blog/`
   - Για το περιβάλλον διαχείρισης: `http://127.0.0.1:8000/admin/`
