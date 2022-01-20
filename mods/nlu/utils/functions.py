import bangla
import datetime 
import re

class Extractors:

    def dates(self, date, lang): 
        
        if int(date.split('-')[-1])>31:
            return "The date is not correct"
        elif int(date.split('-')[1])>12 and int(date.split('-')[1])<1:
            return "The month is not correct"
        try:
            ddate = datetime.datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            return "The format is incorrect"
        en_date = ddate.strftime("%d %B, %Y")
        ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4])
        en_rep = en_date.replace(en_date.split(' ')[0], ordinal(int(en_date.split(' ')[0])))
        
        m_en = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        m_bn = ['জানুয়ারি', 'ফেব্রুয়ারী', 'মার্চ', 'এপ্রিল', 'মে', 'জুন', 'জুলাই', 'আগষ্ট', 'সেপ্টেম্বর', 'অক্টোবর', 'নভেম্বর', 'ডিসেম্বর']
        d = en_date.split(' ')[0]
        y = en_date.split(' ')[2]
        m = en_date.split(' ')[1]
        m = m[0:len(m)-1]
        bn_d = bangla.convert_english_digit_to_bangla_digit(d)
        bn_y = bangla.convert_english_digit_to_bangla_digit(y)
        bn_m = m_bn[m_en.index(m)]
        li1 = [ '০৫','০৬','০৭' ,'০৮' ,'০৯' ,'১০' ,'১১' ,'১২' ,'১৩' ,'১৪' ,'১৫' ,'১৬' ,'১৭' ,'১৮' ] 
        li2 = ['১৯' ,'২০' ,'২১' ,'২২', '২৩', '২৪' ,'২৫' ,'২৬', '২৭' ,'২৮' ,'২৯' ,'৩০' ,'৩১' ]

        if bn_d == '০১':
            bn_d = '০১'+'লা'
        elif bn_d == '০২':
            bn_d = bn_d+'রা'   
        elif bn_d == '০৩':
            bn_d = bn_d+'রা'    
        elif bn_d == '০৪':
            bn_d = bn_d+'ঠা'
        elif bn_d in li1:
            bn_d = bn_d+'ই'
        else:
            bn_d = bn_d+'শে'

        bn_date = bn_d+ ' '+bn_m+' '+bn_y
        if lang == 'bn':
            return bn_date
        elif lang == 'en':
            return en_rep
        else:
            return "Please provide the correct language format"
        
        
    def extractor(self,te):
        
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        elst = re.findall(regex, te)
        ph =[]
        nn = []
        nlst =[]
        res ={}
        nlst = re.findall('[0-9]+', te)
        if nlst:
            for i in range(len(nlst)):
                if (nlst[i][0:2] == '01' and len(nlst[i])== 11 ) or (nlst[i][0:4] == '8801' and len(nlst[i])== 13):
                    ph.append(nlst[i])
                    nn.append(nlst[i])
                elif len(nlst[i])>9:
                    nn.append(nlst[i])
            for n in nn:
                nlst.remove(n)
            if nlst:
                digit = int(nlst[0])
                res['digit']=digit
        if elst:
            em = elst[0]
            res['email']=em
        if ph:
            phone = ph[0]
            res['phone']=phone
        
        return res
    