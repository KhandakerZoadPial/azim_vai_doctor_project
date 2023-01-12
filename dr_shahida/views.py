from django.shortcuts import render
from dr_shahida.models import BlogPost

def index(request):
    # chamber_name = 'ল্যাব এইডে আপনাকে স্বাগতম'
    # doctor_tagline = 'আপনার শহরের সেরা নারী স্বাস্থ্যসেবা'

    # blog_title = 'ব্লগ পোস্ট'
    # blog_tagline = 'আমাদের সর্বশেষ মেডিকেল ব্লগ পোস্ট'
    # blog_posts = BlogPost.objects.all()

    # about_title = 'ড. শাহিদা বেগম মিনু সম্পর্কে '
    # about_tagline = 'নিজের এবং আপনার পরিবারের জন্য সর্বোত্তম চিকিৎসা সেবা'
    # about_text = 'ডাঃ শাহিদা বেগম মিনু ল্যাব এইড বরিশালের গাইনোকোলজিস্ট কনসালট্যান্ট। তিনি এমবিবিএস, ডিজিও, এমসিপিএস (ওবিজিওয়াইএন) এবং এফসিপিএস (ওবিজিওয়াইএন) ডিগ্রি অর্জন করেছেন। তিনি বন্ধ্যাত্ব এবং গাইনোকোলজিকাল ক্যান্সার চিকিৎসায় বিশেষভাবে প্রশিক্ষিত এবং নিবন্ধন নম্বর ২৫৭৫১ এর অধীনে বিএমডিসিতে নিবন্ধিত হন। এমবিবিএস ডিগ্রি পাওয়ার পর তার ২৭ বছরের অভিজ্ঞতা এবং স্নাতকোত্তর ডিগ্রি অর্জনের পর ২১ বছরের অভিজ্ঞতা রয়েছে। তিনি বাংলাদেশ ও সৌদি আরবের বেশ কয়েকটি উল্লেখযোগ্য হাসপাতালে কাজ করেছেন। তার সাম্প্রতিকতম অবস্থান ছিল খাজা ইউনূস আলী মেডিকেল কলেজ ও হাসপাতালের গাইনোকোলজি অ্যান্ড অবস্টেট্রিক্স বিভাগের বিভাগীয় প্রধান হিসেবে। বরিশালের ল্যাবএইড ডায়াগনস্টিকে সকাল সাড়ে ৯টা থেকে দুপুর ২টা পর্যন্ত তিনি রোগীদের চিকিৎসা দেন। (শনিবার-বৃহস্পতিবার)'

    # experience = '২৭ বছরের অভিজ্ঞতা'
    # degree1 = 'এমবিবিএস'
    # degree2 = 'DGO'
    # degree3 = 'এমসিপিএস (OBGYN)'
    # degree4 = 'এফসিপিএস (OBGYN)'
    # special_training = 'বন্ধ্যাত্ব এবং গাইনীকলজিক্যাল ক্যান্সার চিকিত্সা বিশেষভাবে প্রশিক্ষিত'

    # service_title = 'সেবাসমূহ '
    # service_tagline = 'চমৎকার চিকিৎসা সেবা'
    # service1 = 'আউটডোর চেকআপ'
    # service2 = 'অপারেশন ও সার্জারি'
    # service3 = 'জরুরী পরিচর্যা'

    # chamber_title = 'চেম্বার'
    # chamber__name = 'ল্যাব এইড'
    # chamber_address = 'ঠিকানা: ৬ষ্ঠ তলা, রুম নং: ৬০৭, কে জাহান সেন্টার, হাউজ-১০৬, সদর রোড, বরিশাল - ৮২০০'
    # visiting_hour = 'ভিজিটিং আওয়ার: সকাল ৯টা ৩০ মিনিট থেকে দুপুর ২টা পর্যন্ত। (শনিবার-বৃহস্পতিবার)'
    # appointment_title ='এপয়েন্টমেন্ট '
    # appointment_tag = 'একটি অ্যাপয়েন্টমেন্ট নিন'
    # appointment_btn = 'কল'

    # footer_title = 'যোগাযোগ'
    # footer_tagline = 'ল্যাব এইড, বরিশাল'
    # footer_address = '৬ষ্ঠ তলা, রুম নং: ৬০৭, কে জাহান সেন্টার, হাউজ-১০৬, সদর রোড, বরিশাল - ৮২০০'
    # footer_email = 'dr.shahida2007@yahoo.com'
    # footer_phone = '01766-663305'
    
    chamber_name = 'Welcome To Lab Aid'
    doctor_tagline = 'Best Women Healthcare In Your City'

    blog_title = 'BLOG POSTS'
    blog_tagline = 'Our Latest Medical Blog Posts'
    blog_posts = BlogPost.objects.all()

    about_title = 'About Dr. Shahida Begum Minu'
    about_tagline = 'Best Medical Care For Yourself and Your Family'
    about_text = 'Dr. Shahida Begum Minu is Gynecologist Consultant at Lab Aid Barisal. She holds degrees in medicine from MBBS, DGO, MCPS(OBGYN), and FCPS (OBGYN). She is specially trained in Infertility and Gynecological Cancer Treatment and  registered with the BMDC under registration number 25751. She has 27 years of experience after receiving her MBBS degree and 21 years of experience after receiving her postgraduate degree. She has worked in several notable hospitals in Bangladesh and Saudi Arabia. Her most recent position was as the department head in the Department of Gynecology & Obstetrics at Khwaja Yunus Ali Medical College & Hospital. She treats her patients at Labaid Diagnostic in Barisal from 9:30am to 2:00pm. (Saturday - Thursday)'

    experience = '27 Years Experience'
    degree1 = 'MBBS'
    degree2 = 'DGO'
    degree3 = 'MCPS(OBGYN)'
    degree4 = 'FCPS(OBGYN)'
    special_training = 'Specially trained in Infertility and Gynecological Cancer Treatment'

    service_title = 'SERVICES'
    service_tagline = 'Excellent Medical Services'
    service1 = 'Outdoor Checkup'
    service2 = 'Operation & Surgery'
    service3 = 'Emergency Care'

    chamber_title = 'Chamber'
    chamber__name = 'Lab Aid'
    chamber_address = 'Address: 5th Floor, Room no: 607, K Jahan Center, House-106, Sadar Road, Barisal - 8200'
    visiting_hour = 'Visiting Hour : 9:30am to 2:00pm. (Saturday - Thursday)'
    appointment_title ='Appointment'
    appointment_tag = 'Make an Appointment'
    appointment_btn = 'Call'

    footer_title = 'GET IN TOUCH'
    footer_tagline = 'Lab Aid, Barishal'
    footer_address = '5th Floor, Room no: 607, K Jahan Center, House-106, Sadar Road, Barisal - 8200'
    footer_email = 'dr.shahida2007@yahoo.com'
    footer_phone = '01766-663305'

    diction = {'chamber_name':chamber_name,'doctor_tagline':doctor_tagline, 
    'blog_title':blog_title,'blog_tagline':blog_tagline, 
    'blog_posts':blog_posts[0:3],
    'about_title':about_title, 'about_tagline': about_tagline, 'about_text':about_text,
    'experience':experience, 'degree1':degree1, 'degree2':degree2, 'degree3':degree3, 'degree4':degree4,'special_training':special_training,

    'service_title':service_title,
    'service_tagline':service_tagline, 'service1':service1, 'service2':service2, 'service3':service3,

    'chamber_title':chamber_title, 'chamber__name':chamber__name, 'chamber_address':chamber_address, 'visiting_hour':visiting_hour, 'appointment_title':appointment_title, 'appointment_tag':appointment_tag, 'appointment_btn':appointment_btn,

    'footer_title':footer_title, 'footer_tagline':footer_tagline, 'footer_address':footer_address,'footer_email':footer_email, 'footer_phone':footer_phone,



     }

    return render(request, 'dr_shahida/index.html', context=diction)


def about(request):
    diction = {}

    return render(request, 'dr_shahida/about.html', context=diction)

def service(request):
    diction = {}

    return render(request, 'dr_shahida/service.html', context=diction)

def testimonial(request):
    diction = {}

    return render(request, 'dr_shahida/testimonial.html', context=diction)


def appointment(request):
    diction = {}

    return render(request, 'dr_shahida/appointment.html', context=diction)

def contact(request):
    diction = {}

    return render(request, 'dr_shahida/contact.html', context=diction)


def blog(request):
    blog_posts = BlogPost.objects.all()
    diction = {'blog_posts':blog_posts}

    return render(request, 'dr_shahida/blog.html', context=diction)

def blogdetailview(request,post_id):
    blog_post = BlogPost.objects.get(pk=post_id)
    blog_posts = BlogPost.objects.all()
    
    diction = {'blog_post':blog_post, 'blog_posts':blog_posts[0:4]}

    return render(request, 'dr_shahida/detail.html', context=diction)