from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/singaporeschools' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app)

class General_Details(db.Model):
    __tablename__ = 'generaldetails'
    School_Code = db.Column(db.Integer, primary_key=True)
    School_Name = db.Column(db.String(100), nullable=False)
    School_Region = db.Column(db.String(50), nullable=False)
    School_Address = db.Column(db.String(150), nullable=False)
    School_Postal_Code = db.Column(db.String(50), nullable=False)
    School_Mode = db.Column(db.String(50), nullable=False)
    School_Nature = db.Column(db.String(50), nullable=False)
    School_Type = db.Column(db.String(50), nullable=False)
    School_Number = db.Column(db.String(50), nullable=False)
    School_Email = db.Column(db.String(50), nullable=False)
    School_Website = db.Column(db.String(150), nullable=False)
    School_Image_Source = db.Column(db.String(200), nullable=False)

    



class PSLE_Scores(db.Model):
    __tablename__ = 'PSLE_Score_Details'
    School_Code = db.Column(db.Integer, primary_key=True)
    IP_Affiliation = db.Column(db.String(50), nullable=False)
    IP_NonAffiliation = db.Column(db.String(50), nullable=False)
    Express_Affiliation = db.Column(db.String(50), nullable=False)
    Express_NonAffiliation = db.Column(db.String(50), nullable=False)
    NA_Affiliation = db.Column(db.String(50), nullable=False)
    NA_NonAffiliation = db.Column(db.String(50), nullable=False)
    NT_Affiliation = db.Column(db.String(50), nullable=False)
    NT_NONAffiliation = db.Column(db.String(50), nullable=False)

class Subjects(db.Model):
    __tablename__ = 'Subjects_Offered'
    School_Code = db.Column(db.Integer, primary_key=True)
    Subject_Offered = db.Column(db.String(50), primary_key=True)

class DSA(db.Model):
    __tablename__ = 'dsa_opportunities'
    School_Code = db.Column(db.Integer, primary_key=True)
    DSA_CCA = db.Column(db.String(100), primary_key=True)

class CCA(db.Model):
    __tablename__ = 'cca_offered'
    School_Code = db.Column(db.Integer, primary_key=True)
    CCA = db.Column(db.String(100), primary_key=True)

class Special_Education(db.Model):
    __tablename__ = 'special_ed_support'
    School_Code = db.Column(db.Integer, primary_key=True)
    Support_Scheme = db.Column(db.String(100), primary_key=True)

class Electives(db.Model):
    __tablename__ = 'electives'
    School_Code = db.Column(db.Integer, primary_key=True)
    Elective_Name = db.Column(db.String(100), primary_key=True)
    Elective_Sub_Header = db.Column(db.String(100), nullable=False)
    Elective_Sub_Sub_Header = db.Column(db.String(100), primary_key=True)

class Affiliations(db.Model):
    __tablename__ = 'affiliations'
    School_Code = db.Column(db.Integer, primary_key=True)
    Affiliated_School = db.Column(db.String(100), primary_key=True)


@app.route("/details")
def get_all():
    all_schools = General_Details.query.all()
    if len(all_schools):
        school_data = []
        for school in all_schools:
            school_data.append({
                "School_Code": school.School_Code,
                "School_Name": school.School_Name,
                "School_Region": school.School_Region,
                "School_Address": school.School_Address,
                "School_Postal_Code": school.School_Postal_Code,
                "School_Mode": school.School_Mode,
                "School_Nature": school.School_Nature,
                "School_Type": school.School_Type,
                "School_Number": school.School_Number,
                "School_Email": school.School_Email,
                "School_Website": school.School_Website,
                "School_Image_Source": school.School_Image_Source
            })
        return jsonify(school_data)
    else:
        return jsonify(
            {
                "code": 404,
                "message": "There are no schools."
            }
        ), 404

@app.route("/details/<int:School_Code>")
def find_by_school_code(School_Code):
    school = General_Details.query.filter_by(School_Code=School_Code).first()
    if school:
        return jsonify(
            {
                "School_Code": school.School_Code,
                "School_Name": school.School_Name,
                "School_Region": school.School_Region,
                "School_Address": school.School_Address,
                "School_Postal_Code": school.School_Postal_Code,
                "School_Mode": school.School_Mode,
                "School_Nature": school.School_Nature,
                "School_Type": school.School_Type,
                "School_Number": school.School_Number,
                "School_Email": school.School_Email,
                "School_Website": school.School_Website,
                "School_Image_Source": school.School_Image_Source
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "School not found."
        }
    ), 404

@app.route("/details/<string:School_Name>")
def find_by_school_name(School_Name):
    school = General_Details.query.filter_by(School_Name=School_Name).first()
    if school:
        return jsonify(
            {
                "School_Code": school.School_Code,
                "School_Name": school.School_Name,
                "School_Region": school.School_Region,
                "School_Address": school.School_Address,
                "School_Postal_Code": school.School_Postal_Code,
                "School_Mode": school.School_Mode,
                "School_Nature": school.School_Nature,
                "School_Type": school.School_Type,
                "School_Number": school.School_Number,
                "School_Email": school.School_Email,
                "School_Website": school.School_Website,
                "School_Image_Source": school.School_Image_Source
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "School not found."
        }
    ), 404

@app.route("/subjects/<int:School_Code>")
def find_subject_by_school_code(School_Code):
    subjects = Subjects.query.filter_by(School_Code=School_Code).all()
    if len(subjects):
        school_code = subjects[0].School_Code
        subjects_offered = []
        for subject in subjects:
            subjects_offered.append(subject.Subject_Offered)
        
                
        return jsonify(
            {
                "School_Code": school_code,
                "Subjects_Offered": subjects_offered
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "School not found."
        }
    ), 404

@app.route("/dsa/<int:School_Code>")
def find_dsa_ccas_by_school_code(School_Code):
    dsa = DSA.query.filter_by(School_Code=School_Code).all()
    if len(dsa):
        school_code = dsa[0].School_Code
        dsa_cca = []
        for cca in dsa:
            dsa_cca.append(cca.DSA_CCA)
        
                
        return jsonify(
            {
                "School_Code": school_code,
                "DSA_CCA": dsa_cca
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "School not found."
        }
    ), 404

@app.route("/cca/<int:School_Code>")
def find_cca_by_school_code(School_Code):
    cca = CCA.query.filter_by(School_Code=School_Code).all()
    if len(cca):
        school_code = cca[0].School_Code
        cca_offered = []
        for cca_offering in cca:
            cca_offered.append(cca_offering.CCA)
        
                
        return jsonify(
            {
                "School_Code": school_code,
                "CCA_Offered": cca_offered
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "School not found."
        }
    ), 404

@app.route("/special_ed/<int:School_Code>")
def find_special_ed_by_school_code(School_Code):
    special_ed = Special_Education.query.filter_by(School_Code=School_Code).all()
    if len(special_ed):
        school_code = special_ed[0].School_Code
        special_ed_support = []
        for support in special_ed:
            special_ed_support.append(support.Support_Scheme)
        
                
        return jsonify(
           {
               "School_Code": school_code,
                "Special_Education_Support": special_ed_support
        }
        )
    return jsonify(
        {
            "code": 404,
            "message": "School not found."
        }
    ), 404

@app.route("/affiliations/<int:School_Code>")
def get_affiliated_schools_by_school_code(School_Code):
    affiliations = Affiliations.query.filter_by(School_Code=School_Code).all()
    if len(affiliations):
        school_code = affiliations[0].School_Code
        affiliated_schools = []
        for school in affiliations:
            affiliated_schools.append(school.Affiliated_School)

        return jsonify(
            {
                "School_Code": school_code,
                "Affiliated_Schools": affiliated_schools
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "School not found."
        }
    ), 404

@app.route("/psle/<int:School_Code>")
def get_psle_scores_by_school_code(School_Code):
    scores = PSLE_Scores.query.filter_by(School_Code=School_Code).first()
    if scores:
        return jsonify(
            {
                "School_Code": scores.School_Code,
                "IP_Affiliation": scores.IP_Affiliation,
                "IP_NonAffiliation": scores.IP_NonAffiliation,
                "Express_Affiliation": scores.Express_Affiliation,
                "Express_NonAffiliation": scores.Express_NonAffiliation,
                "NA_Affiliation": scores.NA_Affiliation,
                "NA_NonAffiliation": scores.NA_NonAffiliation,
                "NT_Affiliation": scores.NT_Affiliation,
                "NT_NONAffiliation": scores.NT_NONAffiliation
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "School not found."
        }
    ), 404

@app.route("/electives/<int:School_Code>")
def get_electives_by_school_code(School_Code):
    electives = Electives.query.filter_by(School_Code=School_Code).all()
    if len(electives):
        school_code = electives[0].School_Code
        all_elective_desc = []
        for elective in electives: 
            elective_desc = [elective.Elective_Name, elective.Elective_Sub_Header, elective.Elective_Sub_Sub_Header]
            all_elective_desc.append(elective_desc)
        return jsonify(
            {
                "School_Code": school_code,
                "Electives": all_elective_desc
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "School not found."
        }
    ), 404


if __name__ == '__main__':
    app.run(debug=True, port=5000)

# API KEY
# eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI0YjI5NjE2MWFkZjFkOWJiMDM4ZDI2ZWRiMGRlYTYzYSIsImlzcyI6Imh0dHA6Ly9pbnRlcm5hbC1hbGItb20tcHJkZXppdC1pdC0xMjIzNjk4OTkyLmFwLXNvdXRoZWFzdC0xLmVsYi5hbWF6b25hd3MuY29tL2FwaS92Mi91c2VyL3Bhc3N3b3JkIiwiaWF0IjoxNjk4ODkwMjUwLCJleHAiOjE2OTkxNDk0NTAsIm5iZiI6MTY5ODg5MDI1MCwianRpIjoicnROM3ZpaHN4R2pGQUE1SiIsInVzZXJfaWQiOjE0OTEsImZvcmV2ZXIiOmZhbHNlfQ.NMrhBY1Fl1o9nACt0P2b8Dh0ZrVOv8fqKswGeRc_EYo