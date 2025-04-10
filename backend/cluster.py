CLUSTERS = {
    "bio_data": """
    <h3 class="section-header">Bio Data</h3>
    <div class="form-row">
        <div class="form-group">
            <label>First Name:</label>
            <input type="text" name="first_name" />
        </div>
        <div class="form-group">
            <label>Middle Name:</label>
            <input type="text" name="middle_name" />
        </div>
        <div class="form-group">
            <label>Last Name:</label>
            <input type="text" name="last_name" />
        </div>
    </div>

    <div class="form-row">
        <div class="form-group">
            <label>Nationality:</label>
            <input type="text" name="nationality" />
        </div>
        <div class="form-group">
            <label>Gender:</label>
            <input type="text" name="gender" />
        </div>
        <div class="form-group">
            <label>Date of Birth:</label>
            <input type="text" name="dob" />
        </div>
    </div>

    <div class="form-row">
        <div class="form-group">
            <label>Address Line 1:</label>
            <input type="text" name="address1" />
        </div>
        <div class="form-group">
            <label>Address Line 2:</label>
            <input type="text" name="address2" />
        </div>
    </div>

    <div class="form-row">
        <div class="form-group">
            <label>City:</label>
            <input type="text" name="city" />
        </div>
        <div class="form-group">
            <label>State:</label>
            <input type="text" name="state" />
        </div>
        <div class="form-group">
            <label>Pin Code:</label>
            <input type="text" name="pincode" />
        </div>
    </div>
    """,

    "medical": """
    <h3 class="section-header">Medical</h3>
    <div class="form-row">
        <div class="form-group"><label>Blood Type:</label><input type="text" name="blood_type" /></div>
        <div class="form-group"><label>Weight (kg):</label><input type="text" name="weight" /></div>
        <div class="form-group"><label>Height (cm):</label><input type="text" name="height" /></div>
    </div>
    <div class="form-row">
        <div class="form-group"><label>BMI:</label><input type="text" name="bmi" /></div>
        <div class="form-group"><label>Heart Rate:</label><input type="text" name="heart_rate" /></div>
        <div class="form-group"><label>BP Status:</label><input type="text" name="bp_status" /></div>
    </div>
    <div class="form-row">
        <div class="form-group"><label>Known Allergies:</label><input type="text" name="allergies" /></div>
        <div class="form-group"><label>Chronic Conditions:</label><input type="text" name="chronic_conditions" /></div>
        <div class="form-group"><label>Primary Doctor:</label><input type="text" name="doctor_name" /></div>
    </div>
    """,

    "financial": """
    <h3 class="section-header">Financial</h3>
    <div class="form-row">
        <div class="form-group"><label>Bank Name:</label><input type="text" name="bank_name" /></div>
        <div class="form-group"><label>Account Number:</label><input type="text" name="account_number" /></div>
        <div class="form-group"><label>IFSC Code:</label><input type="text" name="ifsc_code" /></div>
    </div>
    <div class="form-row">
        <div class="form-group"><label>PAN Number:</label><input type="text" name="pan_number" /></div>
        <div class="form-group"><label>Monthly Income:</label><input type="text" name="monthly_income" /></div>
        <div class="form-group"><label>Investment Details:</label><input type="text" name="investments" /></div>
    </div>
    """,

    "family": """
    <h3 class="section-header">Family</h3>
    <div class="form-row">
        <div class="form-group"><label>Father's Name:</label><input type="text" name="father_name" /></div>
        <div class="form-group"><label>Mother's Name:</label><input type="text" name="mother_name" /></div>
        <div class="form-group"><label>Number of Siblings:</label><input type="text" name="siblings" /></div>
    </div>
    <div class="form-row">
        <div class="form-group"><label>Spouse Name:</label><input type="text" name="spouse_name" /></div>
        <div class="form-group"><label>Children (if any):</label><input type="text" name="children" /></div>
        <div class="form-group"><label>Emergency Contact:</label><input type="text" name="emergency_contact" /></div>
    </div>
    """,

    "transit": """
    <h3 class="section-header">Transit</h3>
    <div class="form-row">
        <div class="form-group"><label>Vehicle Number:</label><input type="text" name="vehicle_number" /></div>
        <div class="form-group"><label>Registration Date:</label><input type="text" name="registration_date" /></div>
        <div class="form-group"><label>Vehicle Type:</label><input type="text" name="vehicle_type" /></div>
    </div>
    <div class="form-row">
        <div class="form-group"><label>Driving License No:</label><input type="text" name="license_number" /></div>
        <div class="form-group"><label>License Expiry Date:</label><input type="text" name="license_expiry" /></div>
        <div class="form-group"><label>Insurance Provider:</label><input type="text" name="insurance" /></div>
    </div>
    """,

    "educational": """
    <h3 class="section-header">Educational</h3>
    <div class="form-row">
        <div class="form-group"><label>Highest Qualification:</label><input type="text" name="qualification" /></div>
        <div class="form-group"><label>University Name:</label><input type="text" name="university" /></div>
        <div class="form-group"><label>Field of Study:</label><input type="text" name="field_of_study" /></div>
    </div>
    <div class="form-row">
        <div class="form-group"><label>Year of Graduation:</label><input type="text" name="graduation_year" /></div>
        <div class="form-group"><label>Certifications:</label><input type="text" name="certifications" /></div>
        <div class="form-group"><label>Languages Known:</label><input type="text" name="languages" /></div>
    </div>
    """,

    "work_exp": """
    <h3 class="section-header">Work Experience</h3>
    <div class="form-row">
        <div class="form-group"><label>Current Employment:</label><input type="text" name="current_employment" /></div>
        <div class="form-group"><label>Past Employment:</label><input type="text" name="past_employment" /></div>
        <div class="form-group"><label>Years of Experience:</label><input type="text" name="years_experience" /></div>
    </div>
    <div class="form-row">
        <div class="form-group"><label>Skills:</label><input type="text" name="skills" /></div>
        <div class="form-group"><label>Projects:</label><input type="text" name="projects" /></div>
        <div class="form-group"><label>References:</label><input type="text" name="references" /></div>
    </div>
    """
}
