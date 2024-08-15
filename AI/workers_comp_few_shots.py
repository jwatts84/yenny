

work_comp_examples = [
        {
            "input":"""Claimant: Amie Townsend
                        Witness: Jordan Smith

                        NOTE: Called Amie for initial interview on 26 July 2024
                        SMS Message: Hi Amie, this is regarding your claim. Please call us back at your earliest convenience.

                        NOTE: Left voicemail for Jordan on 3 August 2024
                        SMS Message: Jordan, we need to discuss the incident. Please return our call when possible.

                        NOTE: Completed interview with Jordan by phone 6 August 2024

                        NOTE: Requested Return to Work plan from Anne Mead on 10 August 2024

                        EMAIL: yenny@gmail.com

                        SUBJECT LINE:  | Workers Comp Matter

                        Hello Yenny Vasquez,

                        Can you please supply a copy of the following documents:

                        Position description
                        Leave and attendance records
                        Injury report dated 12 October

                        Kind regards,

                        NOTE: Our instruction are to obtain witness statements and complete an on site inspection""",
            "output":"""----INTERVIEWS----
                        Claimant: Amie Townsend
                        Status: Incomplete
                        Note: Send sms requesting call back
                        \n\n

                        Witness: Jordan Smith
                        Status: Complete
                        Note: Completed interview by phone on 6 August 2024
                        \n\n

                        ----DOCUMENTS----
                        Documents requested
                        (Yenny Vasquez) - Position description
                        (Yenny Vasquez) - Leave and attendance records
                        (Yenny Vasquez) - Injury report dated 12 October
                        (Anne Mead) - Return to Work Plan

                        ---INSTRUCTIONS---
                        Obtain witness statements
                        On site inspection
                        NIL"""
        },
        {
            "input":"""Claimant: Olivia Chen
                    Witness: Aisha Johnson
                    NOTE: Called Olivia for initial interview on 26 July 2024
                    SMS Message: Hi Olivia, this is regarding your claim. Please call us back at your earliest convenience.
                    NOTE: Sent email to Aisha on 3 August 2024
                    SMS Message: Aisha, we need to discuss the incident. Please respond to our email at your earliest convenience.
                    NOTE: Completed written statement from Aisha received via email on 7 August 2024
                    NOTE: Requested ergonomic assessment from Dr. Liam Torres on 10 August 2024
                    EMAIL: diego@gmail.com
                    SUBJECT LINE:  | Workers Comp Matter
                    Hello Diego Morales,
                    Can you please supply a copy of the following documents:

                    Employee training records
                    Safety incident reports for the past 12 months
                    Medical certificate dated 15 October

                    Kind regards,
                    NOTE: Our instructions are to conduct employee interviews and review workplace safety protocols""",

            "output":"""----INTERVIEWS----
                    Claimant: Olivia Chen
                    Status: Incomplete
                    Note: Send sms requesting call back
                    Witness: Aisha Johnson
                    Status: Complete
                    Note: Completed written statement received via email on 7 August 2024
                    ----DOCUMENTS----
                    Documents requested
                    (Diego Morales) - Employee training records
                    (Diego Morales) - Safety incident reports for the past 12 months
                    (Diego Morales) - Medical certificate dated 15 October
                    (Dr. Liam Torres) - Ergonomic assessment
                    ---INSTRUCTIONS---
                    Conduct employee interviews
                    Review workplace safety protocols"""
        },
        {

            "input":"""Claimant: Ethan Nakamura
                    Witness: Sophia Ramirez
                    NOTE: Attempted to reach Ethan via phone on 15 September 2024
                    SMS Message: Hello Ethan, this is about your recent claim. Please contact us as soon as possible.
                    NOTE: Left voicemail for Sophia on 18 September 2024
                    SMS Message: Sophia, we need your input on the recent incident. Please call us back when you can.
                    NOTE: Received written account from Sophia via email on 22 September 2024
                    NOTE: Scheduled workplace noise level assessment with Dr. Fiona Chang for 25 September 2024
                    EMAIL: hr@technovate.com
                    SUBJECT LINE: | Workplace Injury Claim
                    Hello Alex Thompson,
                    Could you please provide the following documents:

                    Employee handbook (latest version)
                    Maintenance logs for the past 6 months
                    Incident report filed on 5 September

                    Best regards,
                    NOTE: We are instructed to interview coworkers and evaluate the workplace environment""",

            "output":"""----INTERVIEWS----
                    Claimant: Ethan Nakamura
                    Status: Incomplete
                    Note: Send follow-up SMS for callback

                    Witness: Sophia Ramirez
                    Status: Complete
                    Note: Received written account via email on 22 September 2024

                    ----DOCUMENTS----
                    Documents requested
                    (Alex Thompson) - Employee handbook (latest version)
                    (Alex Thompson) - Maintenance logs for the past 6 months
                    (Alex Thompson) - Incident report filed on 5 September
                    (Dr. Fiona Chang) - Workplace noise level assessment

                    ---INSTRUCTIONS---
                    Interview coworkers"""
        },
        {

            "input":"""Claimant: Zara Patel
                    Witness: Lucas Nguyen
                    NOTE: Spoke with Zara on 3 October 2024 for initial statement
                    SMS Message: Zara, thanks for speaking with us. We'll be in touch if we need any further information.
                    NOTE: Attempted to contact Lucas on 5 October 2024
                    SMS Message: Lucas, we need to discuss the incident involving Zara. Please call us at your earliest convenience.
                    NOTE: Received email response from Lucas on 8 October 2024 agreeing to a phone interview
                    NOTE: Completed phone interview with Lucas on 10 October 2024
                    NOTE: Requested ergonomic assessment from Dr. Elena Rodriguez on 12 October 2024
                    EMAIL: hr@globaltech.com
                    SUBJECT LINE: | Workplace Injury Claim - Zara Patel
                    Hello Rajesh Kumar,
                    Please provide the following documents for our investigation:
                    1. Zara's job description
                    2. Safety training records for the past year
                    3. Incident report from 28 September
                    Best regards,
                    EMAIL: facilities@globaltech.com
                    SUBJECT LINE: | Equipment Maintenance Records Request
                    Dear Facilities Team,
                    In relation to a recent workplace incident, could you please send:
                    1. Maintenance logs for workstation equipment in Section B
                    2. Any repair requests filed in the last 3 months for that area
                    Thank you for your assistance,
                    EMAIL: zara.patel@globaltech.com
                    SUBJECT LINE: | Follow-up on Your Claim
                    Dear Zara,
                    We hope you're doing well. To proceed with your claim, we need:
                    1. A copy of your medical report from Dr. Johnson
                    2. Any photos you may have of the incident area
                    3. Your signed statement form (attached to this email)
                    Please send these at your earliest convenience.
                    Best wishes,""",

            "output":"""----INTERVIEWS----
                    Claimant: Zara Patel
                    Status: Complete
                    Note: Initial statement taken on 3 October 2024

                    Witness: Lucas Nguyen
                    Status: Complete
                    Note: Phone interview completed on 10 October 2024

                    ----DOCUMENTS----
                    Documents requested
                    (Rajesh Kumar) - Zara's job description
                    (Rajesh Kumar) - Safety training records for the past year
                    (Rajesh Kumar) - Incident report from 28 September
                    (Facilities Team) - Maintenance logs for workstation equipment in Section B
                    (Facilities Team) - Repair requests filed in the last 3 months for Section B
                    (Zara Patel) - Medical report from Dr. Johnson
                    (Zara Patel) - Photos of the incident area
                    (Zara Patel) - Signed statement form
                    (Dr. Elena Rodriguez) - Ergonomic assessment

                    ---INSTRUCTIONS---
                    NIL"""
        },

        
        {

            "input":"""Claimant: Finn O'Connor
                    Witness: Mei Li
                    NOTE: Left voicemail for Finn on 5 November 2024
                    SMS Message: Hi Finn, this is regarding your recent incident report. Please call us back when you can.
                    NOTE: Sent email to Mei on 7 November 2024
                    SMS Message: Mei, we need to discuss the incident involving Finn. Please check your email and respond at your earliest convenience.
                    NOTE: Received call from Finn on 8 November 2024, scheduled in-person interview for 10 November
                    NOTE: Completed video call with Mei on 9 November 2024
                    NOTE: Scheduled on-site safety inspection with Safety Officer Jamal Williams for 12 November 2024
                    EMAIL: team@safeworkspaces.com
                    SUBJECT LINE: | Safety Inspection Scheduling
                    Hello Jamal,
                    We've scheduled the safety inspection for 12 November as discussed. Please confirm your availability.
                    Best regards,
                    EMAIL: finn.oconnor@techinnovate.com
                    SUBJECT LINE: | Interview Confirmation
                    Dear Finn,
                    This email confirms your in-person interview scheduled for 10 November at 2 PM in our office. Please bring any relevant information about the incident.
                    Thank you,
                    NOTE: Our instructions are to complete all interviews, conduct the safety inspection, and prepare a preliminary report by 15 November 2024""",

            "output":"""-----INTERVIEWS----
                    Claimant: Finn O'Connor
                    Status: Scheduled
                    Note: In-person interview scheduled for 10 November 2024

                    Witness: Mei Li
                    Status: Complete
                    Note: Video call completed on 9 November 2024

                    ----DOCUMENTS----
                    NIL

                    ---INSTRUCTIONS---
                    Complete all interviews
                    Conduct safety inspection (scheduled for 12 November with Jamal Williams)
                    Prepare preliminary report by 15 November 2024"""
                            },

            
        {

            "input":"""Claimant: Jasmine Wong
Witness 1: Carlos Mendoza
Witness 2: Aisha Patel
Witness 3: Trevor Nkosi
NOTE: Spoke with Jasmine via phone on 18 April 2025
SMS Message: Jasmine, thank you for speaking with us. We'll be in touch if we need any further information.
NOTE: Sent email to Carlos on 19 April 2025
SMS Message: Carlos, please check your email regarding the incident involving Jasmine. Your input is crucial.
NOTE: Left voicemail for Aisha on 20 April 2025
SMS Message: Aisha, we need to discuss the workplace incident. Please call us back at your earliest convenience.
NOTE: Received email response from Trevor on 21 April 2025 agreeing to an in-person interview
NOTE: Completed phone interview with Carlos on 22 April 2025
NOTE: Scheduled video call with Aisha for 24 April 2025
NOTE: Arranged on-site interview with Trevor for 25 April 2025
NOTE: Requested workplace stress assessment from Psychologist Dr. Olivia Chen for 28 April 2025
EMAIL: facilities@innovacorp.com
SUBJECT LINE: | Workspace Inspection Request
Hello Facilities Team,
We need to conduct an inspection of the workspace where the recent incident occurred. Please advise on available dates next week.
Regards,
EMAIL: jasmine.wong@innovacorp.com
SUBJECT LINE: | Follow-up on Your Report
Dear Jasmine,
We hope you're doing well. We've scheduled interviews with your colleagues and are proceeding with our investigation. If you have any additional information you'd like to share, please don't hesitate to contact us.
Best wishes,
NOTE: Our instructions are to interview all witnesses, conduct the workspace inspection, complete the stress assessment, and prepare a comprehensive report by 5 May 2025""",

            "output":"""----INTERVIEWS----
Claimant: Jasmine Wong
Status: Complete
Note: Phone interview conducted on 18 April 2025

Witness 1: Carlos Mendoza
Status: Complete
Note: Phone interview completed on 22 April 2025

Witness 2: Aisha Patel
Status: Scheduled
Note: Video call scheduled for 24 April 2025

Witness 3: Trevor Nkosi
Status: Scheduled
Note: On-site interview scheduled for 25 April 2025

----DOCUMENTS----
NIL

---INSTRUCTIONS---
Interview all witnesses
Conduct workspace inspection
Complete workplace stress assessment (scheduled with Dr. Olivia Chen for 28 April 2025)
Prepare comprehensive report by 5 May 2025"""
                            },


]
