![](media/image1.png){width="7.344378827646544in" height="6.607477034120735in"}

#   {#section .TOC-Heading}

# 

## 

# Acknowledgments

This web user guidance is aimed at supporting implementation of EWARS in a box, WHO's electronic early warning, alert and response system in emergencies. This guidance fulfills a long felt need to have an easy to use resource with step-by-step instructions in establishing EWARS in a box, facilitating field epidemiologists, surveillance officers and emergency responders to configure EWARS in a box web instance.

This document was developed by the epidemiologists of the EWARS in a box team; Dr Niluka Wijekoon Kannangarage, Dr Yuka Jinnai and Mr Marcel Woung under the Department of Health Emergency Interventions (HEI) of the WHO Health Emergencies Programme at WHO headquarters. Valuable contributions were received from Mr Kevin Crampton from the Information Management and Technology (IMT) of HQ Business Operations (BOS) as well.

Special thanks go to colleagues at WHO regional offices and WHO country offices where EWARS in a box is implemented, as their experiences and insights have shaped the guidance to be a valuable learning resource.

# 

**\
**

# Abbreviations

**AFP** acute flaccid paralysis

**APK** Android application package

**app** application

**AWD** acute watery diarrhoea

**CSS** Cascading Style Sheets

**CSV** comma-separated values

**DHIS** district health information software

**EID** electronic identification

**EOC** emergency operations centre

**epi** **week** epidemiological week

**ERF** \[WHO\] Emergency Response Framework

**EWARS** Early Warning, Alert and Response System

**FV1** form version 1

**GPS** global positioning system

**HTML** HyperText Markup Language

**ID** identifier

**IDP** internally displaced person

**IP** internet protocol \[address\]

**JS** JavaScript

**lab** laboratory

**M&E** monitoring and evaluation

**NGO** nongovernmental organization

**OCHA** \[United Nations\] Office for the Coordination of Humanitarian Affairs

**PCODE** place code

**PHCC** primary health-care centre

**QR** quick response \[code\]

**SD** standard deviation

**SMS** Short Message Service

**sync** synchronize

**URL** universal resource locator

**UUID** universally unique identifier

**VHF** viral haemorrhagic fever

# Executive summary

EWARS in a box is WHO's electronic early warning, alert and response system that enables rapid detection of epidemic-prone disease outbreaks in emergencies. EWARS in a box supports epidemiologists, surveillance officers and emergency responders of Ministry of Health (MoH), local health authorities, WHO and health partners to protect populations from catastrophic consequences of disease outbreaks. In emergency settings, the tool helps to rapidly gather data, verify alerts, analyze and disseminate information for rapid response. EWARS in a box comprises two elements; EWARS mobile application to report data and EWARS web interface to manage data gathered from the EWARS mobile.

This guidance provides concrete and pragmatic support to epidemiologists and surveillance officers to configure EWARS in a box web interface. EWARS in a box web interface operationalizes four key thematic areas of early warning, alert and response system.

-   Reporting -- EWARS in a box facilitates data collection from both offline and online modes.

-   Alert management -- This supports tracking of disease threats, verification of alerts, risk assessment and determination of the risks involved.

-   Data analysis - EWARS analyses data with automated novel techniques. The data analysis features support simple to complex analysis and interactive data explorations online and

offline.

-   Dissemination - The tool disseminates information to users, emergency responders and the public. This is done through configurable dynamic dashboards, a public-facing websites and automated bulletins.

In the EWARS web interface, 24 electronic features translate above four key thematic areas into actions. The document explains each electronic feature comprehensively. It provides step-by-instructions with easy-to-understand illustrations, guiding field epidemiologists and surveillance officers to independently manage the EWARS in a box in emergencies. The guidance is structured in to four parts.

+--------------------------------------------+---------------------------------------------------------+
| Part I. Introduction                       | Part III. Data Collection and Monitoring                |
|                                            |                                                         |
| -   Overview of EWARS in a box             | -   Report manager                                      |
|                                            |                                                         |
| -   Getting started                        | -   M&E Auditor                                         |
|                                            |                                                         |
|                                            | -   Alerts log                                          |
|                                            |                                                         |
|                                            | -   Data import                                         |
|                                            |                                                         |
|                                            | -   Exports                                             |
+============================================+=========================================================+
| Part II. Setting up your EWARS account     | Part IV. Data analysis, visualization and dissemination |
|                                            |                                                         |
| -   Locations                              | -   Plot                                                |
|                                            |                                                         |
| -   Configuration Transfer                 | -   Mapping                                             |
|                                            |                                                         |
| -   Indicators                             | -   Widgets and their configuration                     |
|                                            |                                                         |
| -   Forms                                  | -   Notebooks                                           |
|                                            |                                                         |
| -   Alarms                                 | -   Dashboards                                          |
|                                            |                                                         |
| -   Users and their assignments            | -   Outbreaks                                           |
|                                            |                                                         |
| -   User profiles, tasks and notifications | -   Documents and document templates                    |
|                                            |                                                         |
| -   EWARS accounts settings                | -   Website builder                                     |
|                                            |                                                         |
| -   SMS reporting and teams                |                                                         |
|                                            |                                                         |
| -   EWARS Stand-alone                      |                                                         |
+--------------------------------------------+---------------------------------------------------------+

mThis guidance is part of the EWARS in a box training and capacity building package that includes EWARS in a box quick start guide, EWRS in a box mobile user guide and EWARS in a box: electronic early warning, alert and response system implementation in emergencies OpenWHO online training course.

This guidance fulfills the long-felt need to have a written instruction guide for EWARS in a box for field use in emergencies.

# PART I. Introduction

Chapters 1 and 2 provide an introduction to Early Warning, Alert and Response System (EWARS) in a box, and set out information about how to get started with the tool.

# Chapter 1. Overview of EWARS in a box

WHO's [Emergency Response Framework](https://apps.who.int/iris/handle/10665/258604) (ERF)[^1] highlights the Early Warning, Alert and Response System (EWARS) as one of the priority emergency interventions to be implemented within the first two weeks of an emergency response operation. The aim of ensuring early detection and prompt response is to mitigate the impact of communicable diseases among crisis-affected populations.

EWARS in a box brings novel technology to early warning in emergencies and is supported by the Health Emergencies Programme at WHO headquarters. Strategic use of technology and innovation makes disease detection in emergencies easier and more effective, saving lives in the process.

EWARS in a box is an innovative and effective tool designed to detect disease outbreaks quickly in emergency, conflict and vulnerable settings. It can be deployed in humanitarian emergencies such as:

-   war or civil strife, affecting large civilian populations and causing displacement;

-   natural disasters, such as floods, tsunamis, volcanic eruptions and earthquakes;

-   food insecurity and famine;

-   large-scale disease outbreaks that overwhelm national capacity;

-   food, chemical or radio-nuclear spills, and public health emergencies due to other hazards.

EWARS in a box is mainly used by front-line workers; it consists of manuals, mobile phones and laptops to capture and submit key data, thereby facilitating multifaceted, in-depth analysis and monitoring/tracking. The EWARS in a box kit contains the items depicted in Fig. 1.1.

Fig. 1.1. EWARS in a box kit contents

![A picture containing text, indoor, computer, computer Description automatically generated](media/image3.png){width="5.739584426946632in" height="2.948885608048994in"}

EWARS in a box is designed with the needs of front-line users in mind. It is a simple, rapidly deployable and flexible tool (Fig. 1.2).

Fig. 1.2. EWARS in a box as a simple, rapidly deployable and flexible tool

![](media/image4.png){width="4.932622484689414in" height="2.785929571303587in"}

For ease of use and brevity, this guide will refer to the EWARS in a box tool as "EWARS" throughout. Subsequent sections address the different EWARS components, its key modules, EWARS environments and deployment.

## 1.1 EWARS components

EWARS comprises several components, including WHO EWARS/EWARS Web, EWARS Country, EWARS Stand-alone, EWARS Mobile and Short Message Service (SMS) Gateway, as shown in Fig. 1.3.

Fig. 1.3. EWARS components

![](media/image5.png){width="5.77083552055993in" height="5.77083552055993in"}

-   **WHO EWARS/EWARS Web** refers to the EWARS web version, which is accessible via the internet. It contains all EWARS accounts across regions and countries.

-   **EWARS Country** is a local copy of EWARS running on a country server that may be accessible via the internet or open to a private network only. It is not connected to WHO EWARS: it is an entirely separate server, containing all the EWARS components and roles, but the data and components are only accessible by the authorized users of that country.

-   **EWARS Stand-alone** is a local EWARS developed for settings without reliable internet connections, which connects to either WHO EWARS or an EWARS Country server when connection is established.

-   **EWARS Mobile** is the mobile application running on Android, which is used for reporting data from the field to WHO EWARS.

-   **SMS Gateway** is t[he EWARS Mobile application on Android developed to facilitate SMS reporting in settings with unreliable internet connection.]{.mark}

## 1.2 EWARS components and their deployment in various scenarios

EWARS can be deployed easily under various scenarios in different countries or contexts, even where there is unreliable or no internet connectivity. A few key scenarios are described below, depicting practical situations in which EWARS is deployed.

In **Scenario A**, there is reliable internet connectivity. Field workers such as nurses, surveillance officers and community health workers throughout the country are equipped with mobile phones and can submit reports directly to WHO EWARS (Fig. 1.4).

Fig. 1.4. EWARS reporting with reliable internet connectivity

![A picture containing text, screenshot Description automatically generated](media/image6.png){width="5.822916666666667in" height="1.4166666666666667in"}

In this instance, the EWARS Mobile application is installed on the EWARS phones of field workers for reporting purposes. The field workers, Reporting Users of primary health-care centres (PHCCs), laboratory workers, mobile clinics and field hospital workers capture data on the mobile application and submit it directly to WHO EWARS using an internet connection (Fig. 1.5).

Fig. 1.5. Scenario A: reporting with reliable internet connectivity

![](media/image7.png){width="6.340277777777778in" height="4.473611111111111in"}

In **Scenario B**, the internet connection is unreliable -- for example, in the case of those in remote islands and rural areas, where Reporting Users visit the local surveillance office on a regular basis (such as daily or weekly) to submit reports. Possible deployments for this scenario are outlined below.

EWARS Stand-alone functions as an intermediary medium, facilitating reporting between EWARS Mobile and WHO EWARS in scenarios that are offline or that lack access to reliable internet connections (Fig. 1.6). Reporting Users can input data in offline mode using EWARS Mobile. All Reporting Users visit the local surveillance office, where EWARS Stand-alone is set up, regularly. They submit the entered data to EWARS Stand-alone through quick response (QR) code sharing, using a local hotspot.

Fig. 1.6. EWARS reporting with unreliable internet connectivity

![Text Description automatically generated with low confidence](media/image8.jpg){width="6.151042213473316in" height="1.1040332458442694in"}

The data in EWARS Stand-alone are submitted to WHO EWARS using an internet connection (Fig. 1.7). For detailed information, refer to **Chapter 25. EWARS** **Stand-alone**.

Fig. 1.7. Scenario B: reporting via EWARS Stand-alone overview

![Diagram Description automatically generated](media/image9.png){width="6.27083552055993in" height="4.40625in"}

In deployment using the internet connection of the surveillance office, Reporting Users collect the data in offline mode and submit it from their EWARS Mobile application to WHO EWARS, using the office internet connection (Fig. 1.8). These submitted reports are saved as "queued" reports.

Fig. 1.8. EWARS reporting using office internet connection

![Text Description automatically generated](media/image10.png){width="6.27083552055993in" height="1.2395833333333333in"}

Reporting Users visit the surveillance office and submit the queued reports to WHO EWARS through the office internet connection (Fig. 1.9).

Fig. 1.9. Scenario B: reporting via queued reports overview

![Diagram Description automatically generated](media/image11.png){width="6.27083552055993in" height="4.40625in"}

In **Scenario C**, all Reporting Users are equipped with mobile phones but are not able to visit the surveillance office regularly, or the office is not in the near vicinity -- for example, those in remote areas, conflict-affected areas or areas with poor infrastructure support. These users can access the SMS Gateway. The Reporting Users collect their reports in their EWARS Mobile application [and submit them to WHO EWARS via SMS (Fig. 1.10).]{.mark}

Fig. 1.10. EWARS reporting using SMS Gateway connection

![Graphical user interface Description automatically generated with low confidence](media/image12.png){width="6.238839676290464in" height="1.1197922134733158in"}

[These reports are received by the SMS Gateway phone. This is a dedicated Android phone with the EWARS SMS Gateway application activated.]{.mark} It relays the reports received as SMSs to the WHO EWARS server, using an internet connection (Fig. 1.11). For detailed information, refer to **Chapter 24.** **SMS** **reporting** **and** **teams**.

Fig. 1.11. Scenario C reporting overview

![](media/image13.jpg){width="5.935614610673666in" height="4.16729658792651in"}

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** all the above scenarios use the WHO EWARS server. If you want to run EWARS on your own server, follow the steps below.
  --------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In an EWARS Country scenario, the country wants to host its server locally. This is an entirely separate server that contains all the EWARS components and roles, but the data and components are accessible only by the authorized users of that EWARS Country server. All the information given above for **Scenarios A, B** and **C** is also applicable, but the server used is an EWARS Country one.

In EWARS deployment as in **Scenario A**, with stable internet connection, the field workers can submit the report directly to the EWARS Country server using the internet connection (Fig. 1.12).

Fig. 1.12. EWARS reporting using EWARS Country server

![A picture containing text, screenshot Description automatically generated](media/image15.png){width="5.822916666666667in" height="1.4166666666666667in"}

## 1.3 Key modules

Fig. 1.13 and Table 1.1 set out the four key EWARS modules.

Fig. 1.13. Key EWARS modules

![](media/image16.png){width="6.2296741032370955in" height="2.6605905511811025in"}

Table 1.1. Details of the key EWARS modules

+---------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Module**                                                                                  | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
+=============================================================================================+==================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
| **Reporting**                                                                               | EWARS facilitates data collection and reporting in both offline and online modes. With the Reporting module, users can report from different geographical locations, such as the community, temporary establishments, emergency shelters, internally displaced person (IDP) or refugee camps and mobile clinics. Reporting can happen from fixed locations too, such as PHCCs or field hospitals.                                                                                |
|                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ![](media/image17.png){width="0.3854166666666667in" height="0.4270833333333333in"} |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
+---------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Alert management**                                                                        | [EWARS has a dedicated Alert management module that aims to detect potential disease threats at the earliest possible opportunity. This module facilitates tracking of disease threats, verification of alerts, risk assessment and determination of the risks involved. Furthermore, timely resolution of alerts helps improve disease outbreak detection in humanitarian emergencies, saving lives and arresting potential spreads before they become hard to control.]{.mark} |
|                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ![](media/image18.png){width="0.3854166666666667in" height="0.3854166666666667in"} |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
+---------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Data analysis**                                                                           | EWARS analyses data with automated novel techniques. The Data analysis module supports simple to complex analyses and interactive data explorations online and offline. EWARS data visualizations via graphs, charts and tables enable accurate data interpretation for rapid response. The system also facilitates creation of maps. EWARS systematically logs data and facilitates filtering and downloading in different formats.                                             |
|                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ![](media/image19.png){width="0.4270833333333333in" height="0.4270833333333333in"} |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
+---------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Dissemination**                                                                           | The Dissemination module provides various ways to disseminate information to users, emergency responders and the public. This is done through configurable dynamic Dashboards, a public-facing EWARS website and automated bulletins. These bulletins are created at regular intervals, such as on a weekly or monthly basis. For example, this module includes a weekly epidemiological bulletin in the majority of EWARS deployments.                                          |
|                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ![](media/image20.png){width="0.3854166666666667in" height="0.34375in"}            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
+---------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

## 1.4 Types of users

EWARS supports different types of users (Fig. 1.14), providing to different levels of functionality and permissions for the application. The users supported by EWARS are:

-   Super Administrators

-   Account Administrators

-   Geographical Administrators

-   Reporting Users.

Fig. 1.14. Types of EWARS users

![](media/image21.png){width="6.555179352580927in" height="5.052950568678916in"}

-   A **Super Administrator** is usually a member of the EWARS core team at the central level. Super Administrators look after EWARS management across all accounts. They can create and delete EWARS Country accounts according to the needs and requests of country emergency responders or the surveillance team.

-   An **Account Administrator** manages the individual country/context account, including alerts, bulletins, dashboards and the EWARS website.

-   A **Geographical Administrator** manages EWARS in specific geographical areas, or areas in a country/context. Geographical Administrators are responsible for managing alerts, dashboards, bulletins and data analysis for that area.

-   A **Reporting User** reports data to EWARS from specific locations. Reporting Users have a very specific set of account permissions that facilitate submission of particular reports from particular locations. Locations can range from PHCCs, mobile clinics and field hospitals to the community. A Reporting User could be a nurse; a medical officer in a PHCC, health post or mobile clinic; a surveillance officer in a district office; or a community health worker/volunteer from the community. Most EWARS Reporting Users use EWARS Mobile for reporting; however, if logistics allow, Reporting Users can use tablets, desktops and laptops as well. In remote locations where there is no internet connection, Reporting Users can still create reports and synchronize them later when they have internet access. These accounts may be generic and linked to a health facility (rather than a specific individual).

This web user guide provides in-depth knowledge about the various features and users of EWARS Mobile. It is intended to assist web users only. The web user could be an Account Administrator or a Geographical Administrator; a mobile user guide is available for Reporting Users. He/she can access the system through an internet browser such as Google Chrome or Microsoft Firefox. All the permissions can be configured in the system but new roles cannot be created.

Chapter 2 covers all aspects of the registration process for EWARS web users in detail.

# Chapter 2. Getting started

This Early Warning, Alert and Response System (EWARS) web user guide is intended to assist an Account Administrator or a Geographical Administrator. Reporting Users can refer to the mobile user guide. If you are not an Account Administrator or a Geographical Administrator, this guide may not be useful for you.

This chapter will help you to register for and access the EWARS account for your context. It goes into detail on topics including user registration, the authentication process (logging in and out), retrieving forgotten credentials and requesting access to accounts in a different country or context. This is designed to help users set up their accounts easily and optimize the powerful EWARS technology to make disease detection and control in emergencies more effective.

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** EWARS Country account creation is done in negotiation with the EWARS core team and the Super Administrator. As an Account Administrator you need to register a user account in the newly created EWARS Country account.
  --------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 2.1 Registering as a new user

The first step to get started is to create an EWARS account for your context/country. EWARS account creation is done centrally by the EWARS Super Administrator.

Once an EWARS account is created and an Account Administrator assigned, each subsequent user has to request approval from the Account Administrator for registration (Fig. 2.1).

![](media/image22.png){width="4.4006944444444445in" height="3.540277777777778in"}Fig. 2.1. The user registration system

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** the following sections assume that you already have an EWARS Country account for your context.
  --------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The registration process is depicted in Fig. 2.2 and the steps are set out in detail below.

Fig. 2.2. The EWARS registration process

![](media/image23.png){width="6.510416666666667in" height="3.255207786526684in"}

-   Open [[https://www.ewars.ws]{.underline}](https://www.ewars.ws.) on an internet browser.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** use Google Chrome for best performance. The link can also be accessed using Mozilla Firefox or Microsoft Edge.
  --------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-   Click on **Create an Account**. The following registration page appears:

![](media/image24.png){width="5.927777777777778in" height="4.117361111111111in"}

-   Populate the following mandatory details.

```{=html}
<!-- -->
```
-   **Your Name**: enter your name.

-   **Your Email**: enter your email address. This will be used for verification of your EWARS account.

-   **Confirm Email**: re-enter the email address for confirmation.

-   **Password**: enter the password for your account.

-   **Confirm Password**: re-enter the password for confirmation.

-   **Organization**: select the organization that you belong to.

-   **Account**: select the EWARS account you wish to register for.

```{=html}
<!-- -->
```
-   Click on **Submit registration**. A verification email will be sent to the email address you have registered with:

![](media/image25.png){width="5.0in" height="2.65625in"}

-   Click on **Verify your email address**. A request will be sent for approval.

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** A Super Administrator will create the EWARS Country account and then create one Account Administrator who can give approval to subsequent Account Administrators and Geographical Administrators.
  --------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The approval will be granted by the Account Administrator of the requested EWARS account. The Account Administrator can either **approve** or **reject** a request. You will receive an email confirming approval or rejection of your registration request, as applicable.

If the request is approved, you will receive an email, as shown below:

![](media/image26.png){width="5.033410979877515in" height="3.2307699037620297in"}

If the request is rejected, you will receive an email with the reason for rejection:

![](media/image27.png){width="4.990972222222222in" height="3.9006944444444445in"}

To follow up on the reason for rejection, please contact support via email at [[ewars@who.int]{.underline}](mailto:ewars@who.int).

## 2.2 Requesting access for another account

If you have already registered in the system but would like to access other accounts -- for example, for a different country or context -- it can be done as follows.

-   Open [[https://www.ewars.ws]{.underline}](https://www.ewars.ws) on an internet browser. Click on **Create an Account**. Click on the **Existing Users** tab. The following screen appears:

![](media/image28.png){width="5.864583333333333in" height="3.3875in"}

-   Populate the following mandatory details.

```{=html}
<!-- -->
```
-   **Email**: enter your registered email address.

-   **Password**: enter the registered password of your account.

-   **New Account**: select the new EWARS Country account you want to access.

```{=html}
<!-- -->
```
-   Click on **Request access**. Your request is sent for approval, and you will receive an appropriate email with the outcome.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** you can request access to another account only if you are an existing user and [you want to access multiple accounts -- for example, if you have a regional EWARS role and are responsible for multiple countries or contexts.]{.mark}
  --------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 2.3 Logging into EWARS

To log into your EWARS account, follow the steps below.

-   Open [[https://www.ewars.ws]{.underline}](https://www.ewars.ws) on an internet browser. The login page appears, as shown below:

![](media/image29.png){width="5.927777777777778in" height="2.8645833333333335in"}

-   Enter the **Email** linked to your EWARS account. Enter the **Password** of your account. Click on **Login**.

## 2.4 Recovering a forgotten password

If you forget your password, EWARS facilitates setting a new password for your account, using the forgot password feature.

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** this feature is only available for users whose accounts have been created with valid personal email addresses. Users with a system-generated email address -- an email address ending in "@ewars.ws" --need to contact the Account Administrator to reset a password.
  --------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To recover your password, follow the steps below.

-   Open [[https://www.ewars.ws]{.underline}](https://www.ewars.ws) on an internet browser. Click on **Forgot Password** on the login page. The following screen appears:

![](media/image30.png){width="5.215972222222222in" height="2.3875in"}

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** if the email provided by the user does not exist in the system, the system notifies the user with the message "No account associated with this address".
  --------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-   Enter the **email address** of your account. Click on **Request Password**. An email will be sent to your registered email address. Click on the **Password** **Reset** link in the email. The following screen appears:

![](media/image31.png){width="5.0in" height="2.5625in"}

-   Enter a **New Password** for your account (minimum six characters). Re-enter the password in the **Confirm new password** field. Click on **Save Password**. Your password has now been changed successfully.

-   To log out of EWARS, click on the **logout** ![](media/image32.png){width="0.32430555555555557in" height="0.31527777777777777in"} icon at the top right-hand corner of the screen. You will be logged out of EWARS and redirected to the login screen, where the new password can now be used to access the system.

## 2.5 Configuring a new EWARS account

Following successful registration, as an Account Administrator or Geographical Administrator, you are required to manage configurations of the new EWARS account in accordance with the country or context.

Configuration of the new account includes several key areas, including adding locations for your country/context, followed by adding indicators, forms, alarms, users and so on. You can use the standard templates provided by EWARS to create forms, dashboards, document templates and websites. Standard templates are available in the Model account, which can be transferred easily and modified to your context. If not, you have the freedom to create new formats according to your needs.

The following chapters of this guide explain these features in greater detail.

# PART II. Setting up your EWARS account 

[Part I provided an overview of]{.mark} the Early Warning, Alert and Response System ([EWARS), and outlined how to get started with the tool. Chapters 3--10 will help you navigate setting up your EWARS account and exploring the features such as Locations, Configuration Transfer, Indicators, Forms and Alarms. They will also provide further detail on]{.mark} users and related actions [(Fig. II.1).]{.mark}

[Fig. II.1. Setting up EWARS account elements]{.mark}

![](media/image33.png){width="7.0in" height="2.4208333333333334in"}

# Chapter 3. Locations

When setting up a new Early Warning, Alert and Response System (EWARS) account, organizing reporting locations is the primary activity. This chapter will help you to set these up.

EWARS needs to recognize reporting units (such as health facilities and shelters) and health administrative levels at national and subnational levels of a country, and their context, before establishing a reporting mechanism.

By setting up locations, you enable the following three key actions:

-   letting EWARS know your reporting locations by adding reporting locations and their hierarchies (via the "location tree") to the system;

-   letting EWARS know what information each reporting location should report by assigning reporting forms to reporting locations;

-   letting EWARS map data geospatially by adding geographical data to reporting locations.

To clarify these processes, this chapter uses the example of Nambutu (a fictional country). For demonstration purposes, let's say that the Account Administrator has to establish reporting from four health facilities within two provinces of Nambutu: Bilnula, Birigo, Dirabi and Isltun primary health-care centres (PHCCs). To do this, a location tree should be created (Fig. 3.1).

Fig. 3.1. Example location tree

![](media/image34.png){width="6.241666666666666in" height="2.65in"}

This example shows three location types with the hierarchy of **Level 1: Country** \> **Level 2: Province** \> **Level 3: Health facility**. Level 1 and Level 2 are administrative location types, whereas Level 3 is a reporting location type.

Other administrative location types may also be relevant to your context, such as a state, district, county, hub, governorate or health area. Other reporting location types include health posts, mobile clinics, field hospitals, community health worker areas and community health volunteer areas.

EWARS uses the parent--child hierarchy when describing locations. In Fig. 3.1 above, Nambutu is the **Parent location** for provinces Aimal and Dirran. Using the same logic, it also follows that Aimal and Dirran are the **Child locations** of Nambutu.

In brief, it is important to recognize the types of locations and their hierarchies applicable to your context by creating a location tree before you create locations. This logic is used throughout when creating new locations or adding locations to an established EWARS account.

## 3.1 Creating, editing and deleting location types

The first step in creating locations is inputting the location types applicable to your context. You can create as many administrative and reporting location types as you need. In the example of the fictional country Nambutu, the location tree has three location types: country, province and health facility.

Creating, editing and deleting location types is done under settings.

To create location types, follow the steps below.

-   Click on the **settings** ![](media/image35.png){width="0.35833333333333334in" height="0.375in"} icon at the top right-hand corner of your dashboard screen. Click on ![](media/image36.png){width="0.8166666666666667in" height="0.275in"} in the menu on the left of the screen. Click on ![](media/image37.png){width="0.20833333333333334in" height="0.23333333333333334in"}, and the following screen appears:

![](media/image38.png){width="5.59166447944007in" height="2.4in"}

-   Enter the name of the **Location Type** (e.g. "Country"). To enter the name in French, click on **en** in the right-hand box and select **fr** from **Available Languages**. Enter the name in French. It will be visible in French once you have selected French as your default language.

-   Set Status as **Active**.

-   Enter the **Description** for the **Location Type** (e.g. "This is a top-level location type").

-   Click on **Save Change(s)**. A notification appears, confirming that the location type has been added.

-   Repeat the steps above to add a **Province** or **Health facility** location type.

The newly added location types are displayed as shown below:

![](media/image39.png){width="6.16666447944007in" height="2.9916666666666667in"}

Follow the steps below to edit an existing location type.

-   Click on the **settings** ![](media/image35.png){width="0.35833333333333334in" height="0.375in"} icon at the top right-hand corner of your dashboard screen. Click on ![](media/image36.png){width="0.9576388888888889in" height="0.31666666666666665in"} in the menu on the left of the screen. Click on the **Location Type** that needs editing. Click on the **edit** ![](media/image40.png){width="0.36666666666666664in" height="0.36666666666666664in"} icon and make the changes. Click on **Save Change(s)**. A notification that the changes have been saved appears.

Follow the steps below to delete an existing location type.

-   Click on the **settings** ![](media/image35.png){width="0.35833333333333334in" height="0.375in"} icon at the top right-hand corner of your dashboard screen. Click on ![](media/image36.png){width="1.0333333333333334in" height="0.35833333333333334in"} in the menu on the left of the screen. Click on the location type to be deleted. Click on the **delete** ![](media/image41.png){width="0.35833333333333334in" height="0.35833333333333334in"} icon and **Confirm**. A notification that the location type has been deleted appears.

## 3.2 Creating locations

Once you have added location types in the system, the next step is to categorize locations under existing location types.

Locations can be entered in EWARS either manually or in bulk. For either method, four key variables need to be known about each location before the details can be entered:

-   **Location name**: the name of the location to be added

-   **Location type**: the location type of the location to be added

-   **Parent location**: the parent location of the location to be added

-   **PCODE**: the place code of the location to be added.

Place codes (PCODEs) are unique identifiers for locations that are represented by combinations of letters and/or numbers to identify a specific location within a database -- these provide a systematic means of linking data to a specific, unambiguous location, such as "NBT001" or "NBT001HF001" in this fictional example. PCODEs need to be identified for each new location before entering it in EWARS.

Before entering the locations in EWARS, list all the locations and their variables as shown in Table 3.1.

Table 3.1. Locations and variables

  --------- ------------------- -------------- ------------------- ---------------------
  No.       **Location name**   **PCODE**      **Location type**   **Parent location**

  1         Nambutu             NBT            Country             --

  2         Aimal               NBT001         Province            Nambutu

  3         Bilnula PHCC        PHCC001        Health Facility     Aimal

  4         Birigo PHCC         PHCC002        Health Facility     Aimal

  5         Dirran              NBT002         Province            Nambutu

  6         Dirabi PHCC         PHCC003        Health Facility     Dirran

  7         Isltun PHCC         PHCC004        Health Facility     Dirran
  --------- ------------------- -------------- ------------------- ---------------------

Parent location is the location immediately above the location under consideration.

Level 1 locations (such as Country) have no parent location as they are the highest level for a country. They are set up automatically by the system as Root location (Uncategorized).

First, you need to create the root location, from which all other locations and the location tree will span out.

The following sections set out the steps to create a location tree by editing the root location to country as the parent location and creating child locations manually one by one or importing them in bulk.

### 3.2.1 Editing root location as country

To set the root location as the top-level location type of your location hierarchy -- as country (for Nambutu), in this example -- follow the steps below.

-   Select the **menu** icon \> **Locations**. Click on **Root Location (Uncategorized)**. The following screen appears:

> ![](media/image42.png){width="5.691666666666666in" height="2.841666666666667in"}

-   Enter the **Location Name** as the Country name: "Nambutu" in this example.

-   Give the **PCODE** for the Country: "NBT" in this example.

-   Select **Location Type** as **Country**.

-   Click on **Save Change(s)**.

### 3.2.2 Creating child locations manually

You can create child locations -- including provinces, districts and health facilities -- manually in the system. As this is a manual process, creation of new locations is done one by one.

Please follow a hierarchy when creating locations manually: the parent location must be created before the child location.

  ---------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------
  ![](media/image43.png){width="0.65625in" height="0.3541666666666667in"}   Have a location tree created in a separate Excel spreadsheet. This makes entering each location in EWARS within the correct hierarchy much easier.

  ---------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------

Using the example shown in Fig. 3.1, the following steps explain how to add the six locations manually.

-   Select the **menu** icon \> **Locations**. Click on **Create New**, and the **General Settings** tab opens:

![](media/image44.png){width="6.091666666666667in" height="2.6666666666666665in"}

-   Enter the new **Location Name**: "Aimal" in this fictional example.

-   The **UUID (universally unique identifier)** is a system-generated unique number assigned to the new location.

-   Set **Status** as **Active**.

```{=html}
<!-- -->
```
-   **Active** locations appear in green; these can receive reports.

-   **Inactive** locations appear in red; these cannot receive reports.

```{=html}
<!-- -->
```
-   Enter the **PCODE** for the new location: "NBT001" for Aimal in this example.

-   Enter the location **Prefix** -- for example, for Aimal the prefix is AIM (see Table 3.1).

![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"} **Note:** A prefix is useful to auto-generate unique identifiers on form submissions. For more information, refer to **Chapter 6. Forms**, topic **6.8.4.2 Auto-generating a unique ID on form** **submissions**.

-   Select an appropriate **Location Type** from the drop-down menu (e.g. Provinces).

-   Enter the **Location Group** name -- for example, let's assume that Aimal belongs to nongovernmental organization (NGO) A or NGO B. You can assign multiple groups by separating them with a comma (,). For more information, refer to topic **3.6 Adding locations to the location group.**

-   Select an appropriate **Parent Location** from the drop-down menu. The new location is created as a Child of the selected Parent location.

-   Click on **Save Change(s)**.

Follow the same steps to create all six locations. Entered locations are displayed in the location tree on the system.

-   Click on the **folder** ![](media/image45.png){width="0.25in" height="0.24166666666666667in"} icon on the left to see the correct location pathway for each location entered. The expanded location tree appears, as shown below:

![](media/image46.png){width="5.91666447944007in" height="2.8333333333333335in"}

Within the location tree, the **folder** ![](media/image47.png){width="0.3416666666666667in" height="0.3351563867016623in"} icon represents administrative locations, while the **location** ![](media/image48.png){width="0.3333333333333333in" height="0.35619094488188974in"} icon represents reporting locations.

### 3.2.3 Importing child locations in bulk via a CSV file

Rather than entering them individually, manually, you can import all provinces, districts and health facilities in your location hierarchy at once using a comma-separated values (CSV) file.

  ---------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------
  ![](media/image43.png){width="0.65625in" height="0.3541666666666667in"}   Use the import feature when you need to set up many reporting sites in EWARS rapidly.

  ---------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------

Check the flowchart in Fig. 3.2 to understand the process of importing locations.

Fig. 3.2. Flowchart for importing locations

![](media/image49.png){width="3.9169083552055994in" height="6.550925196850394in"}

Follow the steps below to import locations as shown in Table 3.1.

**Step 1.** Select **Menu** \> **Administration** \> **Locations** \> **Import Locations**. The following screen appears:

![](media/image50.png){width="5.75in" height="2.175in"}

**Step 2.** Click on **Download** **Template CSV** and open the **locations_template** file in Excel:

![](media/image51.png){width="6.0in" height="1.6416666666666666in"}

**Step 3.** Populate the CSV file as shown in the example below:

![](media/image52.png){width="6.04166447944007in" height="2.1416666666666666in"}

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** for successful location import, the Parent row must be added before the Child rows.
  --------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ---------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------
  ![](media/image43.png){width="0.65625in" height="0.3541666666666667in"}   Be careful to ensure that spellings, uppercase and lowercase letters are accurate while doing the bulk import of locations.

  ---------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------

Populate the columns as outlined below.

-   **name.en** \[Mandatory\]: enter the location name in English. If you want to add a name in French, change the column name from "Name.en" to "Name.fr". Here, "en" and "fr" denote the language code, which is defined when adding new languages. To obtain codes for other languages, click on the **settings** ![](media/image35.png){width="0.35833333333333334in" height="0.375in"} icon and [click on]{.mark} ![](media/image53.png){width="0.8666666666666667in" height="0.2833333333333333in"}[.]{.mark}

-   **pcode** \[Mandatory\]: enter a unique PCODE for the location (e.g. "NBT001" for Aimal in this example).

-   **description:** enter a short description of the location.

-   **parent_pcode** \[Mandatory\]: enter the PCODE of the Parent location.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** parent locations must be imported before doing the bulk import or the locations will not be able to be imported, and an error message will appear.
  --------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-   **prefix:** enter the location prefix (e.g. "NBT" for Nambutu). A prefix is useful to auto-generate a unique identifier on form submissions. For more information, refer to **Chapter 6. Forms**, topic **6.8.4.2 Auto-generating a unique ID on form** **submissions**.

-   **location_type.en:** enter the type under each location name (e.g. "Health facility", "Mobile clinic").

-   **location_groups**: enter the location group's name (e.g. NGO A or NGO B). You can assign multiple groups by separating them with a comma (,). For more information, refer to topic **3.6 Adding locations to the location group**.

-   **status**: enter the status "ACTIVE".

**Save** the file.

  ---------------------------------------------------------------------------------- -------------------------------------------------------------
  ![](media/image43.png){width="0.65625in" height="0.3541666666666667in"}   Complete only the mandatory fields for a rapid import.

  ---------------------------------------------------------------------------------- -------------------------------------------------------------

**Step 4.** On the **Import Locations** screen, Click on ![](media/image54.png){width="0.8583333333333333in" height="0.325in"} \> browse and select the prepared CSV file. The **Status_of_imported_records.csv** file is downloaded.

**Step 5.** Analyse the **Status_of_imported_records.csv** file as below.

The downloaded Status_of_imported_records.csv file has two additional columns: **import_status** and **import_description**.

All successfully imported rows have import_status as SUCCESS and import_description as Created successfully. For any unsuccessful imports, import_status appears as FAILED. The reason for any failure listed is indicated in the import_description column.

The following is a screenshot of the Status_of_imported_records.csv file:

![](media/image55.png){width="7.0in" height="1.8375in"}

As shown in the screenshot, four locations have been successfully imported and two locations have failed to import. For location Birigo PHCC, import_description states "parent_pcode: NBT003 does not exist"; this means that a location with the parent PCODE provided (NBT003) is not available in the system. You need to create the parent location first and then import the location Birigo PHCC.

Similarly, for location Isltun PHCC, import_description states "location_type: County does not exist"; this means that the location type provided (County) is not available in the system. You need to create the location type "County" first, and then import the location Isltun PHCC.

![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}**Note:** to reimport locations that cannot be imported at the first attempt, you need to make the appropriate corrections to the field in the file, as per the instructions in the import_description, and then import the locations again.

**Step 6.** After creating all locations, select **Menu** \> **Locations**. Click on the **Table** tab on the left, and the imported locations are listed, as shown below:

![](media/image56.png){width="6.125in" height="2.533333333333333in"}

## 3.3 Editing locations

Existing or imported locations can be edited when there is a change in their name or status.

Locations can also be edited either individually or in bulk via a CSV file.

### 3.3.1 Editing locations individually

-   Select **Menu** \> **Locations** \> expand or search location you want to edit by clicking on the **folder** ![](media/image45.png){width="0.25in" height="0.24166666666666667in"} icon of the parent location, and clicking on the name of the location you would like to edit. Information on the location will appear on the right-hand side under General settings. Make changes or edits and **Save Change(s)**.

  ---------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------
  ![](media/image43.png){width="0.65625in" height="0.3541666666666667in"}   When you have few locations that need to be edited, use General Settings to edit locations individually.

  ---------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------

### 3.3.2 Editing locations in bulk via a CSV file

Editing locations in bulk allows you to edit all variables except the PCODE. It can be useful in situations involving the same change to multiple locations at once -- for example, if 20 PHCCs managed by NGO A plan to change their management to NGO B, or if you need to disable reporting from multiple PHCCs because they are decommissioned. Instead of changing each location individually, you can edit everything easily in one action by creating a CSV file with the changes you want to make to the existing locations.

To identify a location, the PCODE is the primary identifier. It is a mandatory column in the CSV file. For example, Birigo PHCC is an active PHCC in the system, and you want to disable reporting from it. EWARS will rely on the PCODE to identify which PHCC needs to be disabled. It is therefore paramount that the PCODE of the new CSV file with your changes matches the existing PCODE of the location. If the PCODEs do not match or there are no existing locations using that PCODE, you will not be able to edit or introduce new changes with bulk importation.

See the example below of how to change the status of reporting locations Birigo PHCC and Isltun PHCC and set the location as disabled.

-   Select **Menu** \> **Administration**\> **Locations** \> **Import Locations**. Click on **Download Template CSV** and open the **locations_template** file in Excel:

![](media/image51.png){width="5.933333333333334in" height="1.625in"}

-   Populate the CSV file as shown in the screenshot below:

![](media/image57.png){width="6.025in" height="1.525in"}

-   Check the box in ![](media/image58.png){width="1.9083333333333334in" height="0.2916666666666667in"} \> click on ![](media/image54.png){width="0.8583333333333333in" height="0.325in"} \> browse and select the prepared CSV file. **Status_of_imported_records.csv** file is downloaded.

-   Analyse the **Status_of_imported_records.csv** file as below:

![](media/image59.png){width="6.40833552055993in" height="1.5833333333333333in"}

The file downloaded is the same as the uploaded file with two additional columns: **import_status** and **import_description.**

The import_status column shows the success or failure of the imported records, with reasons for any failures indicated in the import_description column.

To edit locations that could not be updated at the first attempt, you need to make the appropriate corrections to the field locations according to the instructions given in the import_description column, and import the locations again.

## 3.4 Adding geographical mapping information to locations

EWARS supports the integration of geographical information to locations you have entered. EWARS allows locations to be displayed as either a **point** or a geometric **polygon**.

Reporting locations such as health facilities, clinics and treatment centres are points. Administrative locations such as countries, provinces and districts are geometric polygons. They appear as highlighted in Fig. 3.3.

Fig. 3.3. Examples of a point location and a polygon

![](media/image60.png){width="2.8666666666666667in" height="1.8166666666666667in"} ![](media/image61.png){width="3.0605610236220473in" height="1.8in"}

EWARS supports geographical mapping with GeoJson files. If you plan to develop maps with EWARS data, please have your GeoJson dataset ready for the locations.

### 3.4.1 Mapping reporting locations as point locations

-   Select **Menu** \> **Locations**. Click on the **folder** ![](media/image45.png){width="0.25in" height="0.24166666666666667in"} icon \> click on **Location Name** \> click on the **Mapping** tab at the left-hand side. Select **Point** from the **Mapping Display Type** drop-down menu, and the screen below appears:

![](media/image62.png){width="5.864583333333333in" height="3.198863735783027in"}

Provide latitude and longitude information for the location. This can be achieved in three different ways.

-   Enter it manually: type in the latitude and longitude coordinates of the location.

-   Enter it via **Current Location**: if you are currently at the location, this method can be used to automatically input the latitude and longitude. Click on **Current Location** and confirm that EWARS should use your current location. The latitude and longitude coordinates are added.

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** for security reasons, the browser may ask you to allow use of the location service. Select **Confirm** to allow this.
  --------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-   Enter it via **Map Location**: with this method**,** you can specify a location on the map to get the latitude and longitude coordinates. Click on **Map Location**. Navigate and locate the location on the map, and double-click on the centre of the location. Close the map screen, and the latitude and longitude coordinates are set automatically in the input box. Click on **Save Change(s)**.

### 3.4.2 Mapping administrative locations to geometric polygons

Before embarking on mapping locations as geometric polygons, please make sure you have GeoJson files for the administrative locations in your context.

-   Select **Menu** \> **Locations**. Click on the **folder** ![](media/image45.png){width="0.25in" height="0.24166666666666667in"} icon \> click on **Location Name** \> click on the **Mapping** tab at the left-hand side. Select **Geometry** from the **Mapping Display Type** drop-down menu, and the screen below appears:

![](media/image63.png){width="6.108333333333333in" height="2.65in"}

-   Paste the mapping data information in the **GeoJSON** field, as shown below:

> ![https://lh3.googleusercontent.com/GikC7F7IgG23E2Wv9EQg-\_8X1vdhGnjpmeFh2kaFAbFKfby9JZSefYhCG94_vHIjECAC8hV5Z4_8Je51pvQT0FITvAqxyeJX4k5ug5tkWlAkNolEm2N4VT9gPTGfgq42-bBP8ypw](media/image64.png){width="5.770833333333333in" height="2.28125in"}

-   Click on **Edit Geometry**, and a map of the location appears, as shown below:

> ![](media/image65.jpeg){width="4.97695428696413in" height="2.34331583552056in"}

-   Click on **Save Change(s)**.

## 3.5 Adding reporting information to locations

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** to add reporting to locations, you need to have reporting forms ready. For information on creating and configuring the reporting forms, refer to **Chapter 6. Forms**, and then revisit this topic to connect the locations to the reporting forms.
  --------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The reporting tab enables you to set up reporting from different locations, including setting up reporting periods. For example, you can create a weekly EWARS reporting form or an event-based surveillance form for 23 February 2021 to 31 December 2021.

This helps during emergencies, when reporting status may change over time. New reports can be added to locations or removed. This section explains how such modifications can be done easily.

  ---------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![](media/image43.png){width="0.65625in" height="0.3541666666666667in"}   It is important to manage the reporting periods carefully and keep them up to date to calculate performance indicators, completeness and timeliness accurately.

  ---------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------

You can add reporting forms under each reporting location manually. In most instances, however, all PHCCs within a particular province or district tend to report using the same reporting form. In that case, you can set up a reporting tab at the province level so that all changes are inherited by the child locations.

-   Select **Menu** \> **Locations** \> click on a reporting **Location Name** \> click on the **Reporting** tab. Click on **Add Reporting Period** \> select the relevant **Form** from the drop-down menu and select **Start Date**, **End Date** and **Status**.

Reporting start and end dates remain flexible, and can be edited later. Form and start date are mandatory fields, but the start date can be edited later.

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** you can select a start date that pre-dates the current calendar date. This allows the reporting location to report retrospectively, depending on the report. You can select an end date that is far in the future.
  --------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-   Set the **Status** of reporting (**Active/Disabled**). By default, the status is set as **Active**.

-   Click on **Save Change(s)**. The reporting period is added, as shown below:

![](media/image66.png){width="6.18333552055993in" height="2.6333333333333333in"}

Type is shown as custom when the reporting period is based on your preference (i.e., custom-made). It is shown as Inherited when the reporting period is inherited from the parent location. For example, all health facilities in a particular province or district may report within a specific period; that period is inherited from the province or district level.

-   To edit the reporting details, click on the **edit** ![](media/image67.png){width="0.375in" height="0.3in"} icon \> make the desired changes \> click on **Save Change(s)**. A notification appears to confirm that the information has been edited.

-   To delete the reporting details, click on the **delete** ![](media/image68.png){width="0.3416666666666667in" height="0.25in"} icon \> click **Confirm**. A notification appears to confirm that the information has been deleted.

## 3.6 Adding locations to the location group

Locations can be grouped based on your needs. For example, you can group reporting locations in internally displaced person (IDP) camps, locations belonging to humanitarian NGOs, remote areas and so on. This enables disaggregation of data by grouping.

One location can be a member of several groups. For example, Birigo PHCC can be grouped under the location groups "IDP camp clinics" and "NGO A".

Location groups are also useful when configuring widgets. For more information, refer to **Chapter 17. Widgets and their** **configuration**.

To group locations, add the group name to the location details under general settings.

-   Select **Menu** \> **Locations** \> select a reporting location you want to group (e.g. Dirabi PHCC ), and the screen below appears:

![](media/image69.png){width="6.133333333333334in" height="2.475in"}

-   Enter a **Location Group** name (e.g. "NGO A"). A popup screen appears as below:

![](media/image70.png){width="4.983333333333333in" height="0.7333333333333333in"}

-   Click on **Create Group: NGO A**, and the Group is added as below:

![](media/image71.png){width="5.033333333333333in" height="1.0in"}

-   Click on **Save Change(s)**, and the location is added to the group.

To continue grouping other locations, follow the steps above.

You can view all locations belonging to a group under the table tab at the far left-hand side.

-   Select **Menu** \> **Locations** \> click on the **Table** tab. Click on the **filter** ![](media/image72.png){width="0.21666666666666667in" height="0.23333333333333334in"} icon in the **Location Group(s)** column \> select **Is equal to** under **Filter by condition** \> select **NGO A** under **Filter by value**. Click on **Save Change(s)**, and the screen below appears:

![](media/image73.png){width="6.375in" height="2.225in"}

## 3.7 Activating and deactivating child locations

Child locations can be activated or deactivated.

-   Select **Menu** \> **Locations** \> select a location you want to activate/deactivate. Right-click on the location name and the screen below appears:

![](media/image74.png){width="3.8833333333333333in" height="2.2083333333333335in"}

-   Click on **Disable Children**, and child locations of the parent location are deactivated.

-   Click on **Enable Children**, and child locations of the parent location are activated.

## 3.8 Merging child locations with another location

You can merge the child locations of a parent location with another location.

-   Select **Menu** \> **Locations** \> expand or search location "Birigo PHCC". Right-click on the location name, click on **Merge Into**, and the screen below appears:

![](media/image75.png){width="6.26666447944007in" height="2.158333333333333in"}

-   Select the destination location from **Merge \[location\] into** drop-down menu -- Bilnula PHCC in this example.

-   Click on **Save Change(s)**.

Birigo PHCC is merged into Bilnula PHCC.

Once the merge is complete, Birigo PHCC will not be available in the system. Only the merged location -- Bilnula PHCC -- will remain in the system.

## 3.9 Viewing locations under the tree tab

To view the locations in a hierarchical manner, follow the steps below.

-   Select **Menu** \> **Administration** \> **Locations**. Click on the **Tree** tab \> click on a location **folder** ![](media/image45.png){width="0.25in" height="0.24166666666666667in"} icon. Right-click on the location name, and the screen below appears:

![](media/image76.png){width="5.883333333333334in" height="2.8583333333333334in"}

-   Click on **Save Change(s)**.

-   To expand or collapse the location, click on the **folder** ![](media/image45.png){width="0.25in" height="0.24166666666666667in"} icon.

The green highlighted bar by each name indicates **Active** locations; the red bar indicates that the location is **Inactive**.

## 3.10 Viewing locations under the table tab

The table tab displays locations in tabular form.

-   ![A screenshot of a computer Description automatically generated with medium confidence](media/image77.png){width="6.38333552055993in" height="1.825in"}Select **Menu** \> **Administration** \> **Locations**. Click on the **Table** tab, and the screen below appears:

## 3.11 Exporting locations

You can also export locations to share them with other users. To find out how to use the Export feature effectively, refer to **Chapter 23. Exports**, topic **23.4 Exporting locations data**.

# Chapter 4. Configuration Transfer

The Configuration Transfer feature allows users to copy configured items and dependencies from any source account. Configured items are templates. They can be forms, bulletins, dashboards and so on. Dependencies refer to features that are reliant on or influenced by other features. Dependencies linked to the configured items will therefore be transferred with the templates during Configuration Transfer. This feature is for super admin only.

A source account can be any country/context account in the Early Warning, Alert and Response System (EWARS) that contains templates. The Model account is not a real EWARS Country account but is a specially designed source account to share standard templates available for all users. Any new account can copy templates from other active accounts or from a Model account in the system. Users can only copy the templates -- not the data.

The Configuration Transfer feature lends speed and efficiency to the process of setting up an EWARS account during emergency settings, thereby improving response time and saving lives in the process.

  ---------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![](media/image43.png){width="0.65625in" height="0.3541666666666667in"}   Before configuring new items, the Account Administrator can consider using the standard templates and configured items available in the Model account to save effort and maintain uniformity.

  ---------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 4.1 Transferable items

The configured items available for transfer between accounts are document templates, forms, dashboards, indicators, alarms, notebooks, maps and website. These items and their dependencies are shown in Fig. 4.1.

Fig. 4.1. Transferable items and their dependencies

![](media/image78.png){width="5.677083333333333in" height="5.677083333333333in"}

Table 4.1 sets out more information about each of these transferable items.

Table 4.1. Transferable items

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Item type**            **Short description**                                                                                                          **Dependencies**
  ------------------------ ------------------------------------------------------------------------------------------------------------------------------ ------------------------------
  **Document templates**   The templates are used to generate documents (weekly bulletins), which provide information for analysis and decision-making.   Alarms and indicators

  **Forms**                The reporting forms are used for collecting data and information related to specific disease outbreaks or crises.              Indicators

  **Dashboards**           The dashboards are used to present data in a visually understandable manner.                                                   Indicators, forms and alarms

  **Indicators**           The indicators are bound with the form and help to transform data into relevant information for decision-making.               None

  **Alarms**               The alarms are responsible for generating alerts in the system when a disease threat is identified.                            Indicators and forms

  **Notebooks**            The notebooks are used to perform complex analyses on data within the system.                                                  Indicators, forms and alarms

  **Maps**                 The maps are used to analyse and display location-based data and present these in the form of maps.                            Indicators, forms and alarms

  **Website**              A website is created for each source account.                                                                                  Indicators, forms and alarms
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** Configuration Transfer only copies the empty template. There is no data transfer between the two accounts.
  --------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ---------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![](media/image43.png){width="0.65625in" height="0.3541666666666667in"}   The ability to copy templates from one account to another saves you time that would otherwise be spent setting up forms, dashboards and websites from scratch.

  ---------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------

## 4.2 Initiating Configuration Transfer

-   Select **Configuration Transfer** menu in the right panel. The screen below appears:

![](media/image79.png){width="6.035416666666666in" height="2.3826388888888888in"}

-   Click on the **Source Account** drop-down menu, and all the EWARS Country accounts in the system are listed. The **Destination Account** is your own account:

![](media/image80.png){width="6.279279308836395in" height="3.124689413823272in"}

-   Select the **Source Account** from the drop-down menu (e.g. Model account). All the available items inside the **Model account** are listed as shown below:

![](media/image81.png){width="6.115972222222222in" height="2.75in"}

Table 4.2 describes the Configuration Transfer screen.

Table 4.2. Configuration Transfer screen descriptions

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Item**                                                                      | **Description**                                                                                                                                                                                                                     |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 1.  **Tabular listing of available items**                                    |                                                                                                                                                                                                                                     |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Type**                                                                      | This column displays the type of the configured items -- e.g. forms, indicators and so on.                                                                                                                                          |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Name**                                                                      | This column shows the name of the configured items. You can click on the box at the left of the name to select this item for transfer.                                                                                              |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Actions**                                                                   | The box in this column initiates an individual transfer of the configured item.                                                                                                                                                     |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 2.  **Action**                                                                |                                                                                                                                                                                                                                     |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Search Items**                                                              | You can enter keywords/tags associated with the item you wish to search in this box. All transferable items have a tag configuration option inside the relevant configuration screen. The tag makes it easy to search for the item. |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Select All**                                                                | You can select all items at once by clicking on the **Select All** button, rather than selecting individually what you need in your account before transferring.                                                                    |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Deselect All**                                                              | You can click on the **Deselect All** button to deselect all selected items.                                                                                                                                                        |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ![](media/image82.png){width="1.0416666666666667in" height="0.45in"} | You can click on the **Transfer** button to help with the transfer of multiple selected items at once.                                                                                                                              |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

-   Select the item or items to transfer under **Name** \> click on ![](media/image82.png){width="1.0416666666666667in" height="0.45in"} and a popup box along with all the dependencies appears, as shown below:

![](media/image83.png){width="7.0in" height="3.272222222222222in"}

-   Click on **Confirm**, and a notification of successful transfer appears, as shown below:

![](media/image84.png){width="3.1840277777777777in" height="0.6833333333333333in"}

Once the successful transfer of the item(s) is complete, you can see the transferred items in their relevant menus. For example, if you have successfully transferred a form, it is visible under the Forms menu.

[Following this, you can also copy sample indicators from the Model account or create new indicator groups. The]{.mark} following [chapter will address this topic in greater detail]{.mark}[.]{.mark}

# Chapter 5. Indicators

This chapter provides an overview of indicators, their main types and key actions involving them. Data collected under different variables are categorized under a set of Early Warning, Alert and Response System (EWARS) indicators. EWARS analyses data according to indicators, and they set the stage for many features in EWARS, including Alarms, Plots, Notebooks, Document Templates, Dashboards, Website Builder and so on.

In EWARS, there are two types of indicators: **indicators attached to reporting forms** and **system indicators** that are generated automatically. Indicators attached to reporting forms need to be added to the EWARS Country account and mapped to the relevant forms before they can be used for analysis and in EWARS products.

Data submitted through reporting forms act as the main sources for the indicators. Fig. 5.1 shows an example.

Fig. 5.1. Data flow

![](media/image85.png){width="6.934425853018372in" height="1.2692475940507437in"}

## 5.1 Types of indicators

There are two types of indicators in EWARS:

-   **indicators based on reporting forms**, which are matched with a form field in a reporting form (e.g. suspected cases and deaths);

-   **system indicators**, which are not matched with a form or form field but are generated by the system (e.g. completeness, timeliness and so on).

With indicators based on reporting form indicators, mapping of the indicator to the form field happens when a reporting form is set up. Indicators in your system should map to the data that have been collected. Mapping indicators with reporting forms and form fields is explained in **Chapter 6. Forms**, topic **6.6 Adding logic in the form**.

You can also add indicators to the system, based on the data you plan to collect, before setting up a reporting form.

All early warning, alert and response systems have a similar outlook across emergencies. Therefore, the data collected and the indicators they feed into have a common structure.

For a standard set of indicators, refer to the indicators available in the Model account. You can copy the sample indicators from the Model account.

For the sake of convenience, EWARS recommends grouping indicators as shown in Fig. 5.2.

![](media/image86.png){width="5.78125in" height="3.6253258967629045in"}Fig. 5.2. Suggested indicator groups

### 5.1.1 Early warning indicators

Early warning indicators can be grouped into three categories. As standard practice, they are divided into age categories of "under 5" and "5 and over", and are usually not categorized by sex. These indicators may be:

-   related to access and utilization (e.g. the number of children under the age of 5 years having consultations at primary health-care centres (PHCCs));

-   related to morbidity (e.g. the number of children under the age of 5 years with suspected measles, or with suspected viral haemorrhagic fevers (VHFs));

-   related to mortality (e.g. the number of deaths of children over the age of 5 years from VHFs).

Sample early warning indicators are included in the Model account. You could refer to them and transfer selected ones, as suited to your setting. To transfer them to your account, refer to topic **5.2 Copying sample indicators from the Model account**.

If you want to create your own indicators, it is recommended that you follow the indicator groupings shown in Fig. 5.2 in your account.

### 5.1.2 Nutrition indicators

In some contexts, nutrition indicators are collected as a form of early warning of severe acute malnutrition. Collecting nutrition data using EWARS is not recommended. If used, they should be limited to providing an early warning of severe acute malnutrition and used only for a limited period.

Sample nutrition indicators are included in the Model account. You could refer to them and transfer selected ones, as suited to your setting. To transfer them to your account, refer to topic **5.2 Copying sample indicators from the Model account**.

### 5.1.3 Outbreak response indicators

A lot of case-based data need to be collected during outbreaks. These indicators are grouped as outbreak response indicators, and are different from early warning indicators. They may include, for example, the number of cholera cases with severe dehydration in people aged over 60 years.

[Outbreak response indicators may change with the outbreak and the line lists used. Please refer to your outbreak response plan for the specific outbreak to develop appropriate outbreak indicators.]{.mark}

### 5.1.4 System indicators

System indicators are special purpose indicators. They are not bound to reporting forms but are generated by the system when data are collected (e.g. completeness, timeliness of reporting and similar). System indicators are useful when configuring widgets -- for more information, refer to **Chapter 17. Widgets and their configuration**.

  ---------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------
  ![](media/image43.png){width="0.65625in" height="0.3541666666666667in"}   System indicators are already set up in the system once an account is created. You don't need to create them.

  ---------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------

You can copy the sample indicators available in the Model account or create new ones, as shown in the following sections.

## 5.2 Copying sample indicators from the Model account

Follow the steps below to copy the indicators available inside the Model account to your account.

-   Select **Menu** \> **Configuration Transfer**. Select **Model account** from the **Source Account** drop-down menu. Select the indicators you want to copy. Click on ![](media/image87.png){width="1.1090277777777777in" height="0.4in"}, and the indicators are copied to your account.

Follow the steps below to view the copied indicators.

-   Select **Menu** \> **Administration** \> **Indicators** \> click on the **folder** ![](media/image88.png){width="0.25833333333333336in" height="0.23194444444444445in"} icon to expand the **Indicator Group**, and the copied indicators are available.

## 5.3 Creating a new indicator group

The first step in creating indicators is to create an indicator group. An indicator group allows you to organize the related indicators together. You can also create subgroups within an indicator group to organize them into subcategories. Follow the steps below to create an indicator group.

![https://lh4.googleusercontent.com/EZA8hhLLKGcncV_XuYbzJPHTITBlMcD9hrURt3yWz6nEuHAQKaxZW0UaqJu1-GcqcqWgJjuxWbX4vQkYwBAD3HcGQ2cGxF_WiyL3Pxr3KeUlLJ2N3glcDngEGVXKmAyh4kUhTasu=s1600](media/image89.png){width="0.9479166666666666in" height="0.2916666666666667in"}

-   Select **Menu** \> **Administration** \> **Indicators**. Click on and the following screen appears:

![](media/image90.png){width="5.880208880139983in" height="2.8394160104986876in"}

Assume you want to create a laboratory indicator subgroup under the early warning indicator group.

-   Enter a **Name** (e.g. "Lab") \> select a **Parent** group from the drop-down menu (e.g. Early Warning). Click on **Save Change(s)**, and a notification appears that the group is created.

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** if you select a parent group, the new group is created as a subgroup of the parent group. If you do not, the new group is created as a top-level independent group.
  --------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 5.4 Editing or deleting an indicator group

To edit an indicator group, follow the steps below.

-   Select **Menu** \> **Administration** \> **Indicators** \> right-click on the name of the **Indicator Group** \> click on **Edit**.

-   Make appropriate changes to the **Indicator Group** \> click on **Save Change(s)**, and a notification appears that it is updated.

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** the system indicators group cannot be edited or deleted. The following notification appears when you try to delete or edit one:
  --------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](media/image91.png){width="3.0in" height="0.7083333333333334in"}

To delete an indicator group, follow the steps below.

-   Select **Menu** \> **Administration** \> **Indicators** \> right-click on the name of the **Indicator Group**. Click on **Delete** \> click on **Confirm**, and a notification appears that it is deleted.

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** if you delete an indicator group, all the subgroups and the indicators present inside the group and its subgroups will also be deleted.
  --------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 5.5 Creating indicators

Indicators depend on the data you collect. Therefore, an indicator that is applicable to one setting might not be applicable to another. For example, in some cases, the Under 5 fever and rash cases indicator is important, while in others, Under 5 suspected measles cases is the preferred indicator.

Before creating a new indicator, you need to identify the indicator group to which it belongs. Follow the steps below to create an indicator.

![](media/image92.png){width="1.1590277777777778in" height="0.31527777777777777in"}

-   Select **Menu** \> **Administration** \> **Indicators**. Click on and the following screen appears:

![](media/image93.png){width="5.94375in" height="3.3333333333333335in"}

-   Populate the details in the general settings tab of the indicator screen as shown below.

```{=html}
<!-- -->
```
-   **Name** \[Mandatory\]: enter the name of the indicator (e.g. "Total suspected measles cases").

-   **Status** \[Mandatory\]: set as **Active**.

> **Active** indicators appear with a green bar and are ready to use in features like Alarms, Plot and Mapping.
>
> **Inactive** indicators appear with a red bar and cannot be used in any features of EWARS.

-   **Value Type** \[Mandatory\]: select numeric from the drop-down menu.

    Set as **Numeric** to hold a numeric value (e.g. the total number of suspected measles cases).

    Set as **Text** if the indicator needs to bind with a text field in a form (e.g. the name of a hazard).

-   **Group/Folder** \[Mandatory\]: select the indicator group or subgroup from the drop-down menu to which the indicator belongs (e.g. total suspected measles cases would belong under the early warning \> morbidity indicator group).

-   **Description:** enter a description explaining the purpose of the indicator.

-   **Tag:** enter a tag for the indicator, click add tag, and the tag is added. Similarly, you can add multiple tags for an indicator. Tags make indicator searching easy when transferring indicators via Configuration Transfer.

```{=html}
<!-- -->
```
-   Click on **Save Change(s)**, and a notification appears that the indicator is added.

## 5.6 Editing an indicator

You can edit the indicator's name, status and other details.

-   Select **Menu** \> **Administration** \> **Indicators**. Expand the **Indicator Group** by clicking on the **folder** ![](media/image88.png){width="0.25833333333333336in" height="0.23194444444444445in"} icon \> right-click on the name of the indicator. Click on **Edit**, and the following screen appears:

![](media/image94.png){width="6.138888888888889in" height="3.0833333333333335in"}

-   Edit the indicator details \> click on **Save Change(s)**, and a notification appears that it is edited.

## 5.7 Viewing reporting forms matched with an indicator

Data for each indicator are collected via reporting forms in the system. Linking form fields to indicators is done when creating forms. This is discussed in **Chapter 6. Forms**, topic **6.6 Adding logic in the form**. When such linking has taken place, the form/forms feeding into each indicator is displayed underneath them.

-   Select **Menu** \> **Administration** \> **Indicators** \> expand the **Indicator Group** by clicking on the **folder** ![](media/image88.png){width="0.25833333333333336in" height="0.23194444444444445in"}icon. Click on the name of the indicator \> scroll down further and you will see the following screen:

> ![](media/image95.png){width="5.666666666666667in" height="2.8694444444444445in"}

-   **Derivation** shows a list of the form names bound within that indicator. [The derivation will only appear after the indicator is mapped to form fields, and it is not editable here.]{.mark}

## 5.8 System indicators

System indicators are a special set of fixed indicators. These are not bound to any form fields but are calculated automatically by EWARS. You cannot modify or delete the system indicators. They are useful when configuring widgets -- for more information, refer to **Chapter 17. Widgets and their configuration**.

A list of system indicators is shown here and described further below:

![](media/image96.png){width="2.9409722222222223in" height="3.4090277777777778in"}

-   **Alerts**: the alerts indicator provides a count for alerts based on filters and dimensions, such as closed alerts and similar. For more information, refer to **Chapter 13. Alert log**.

-   **Assignments:** the assignments indicator provides a count of assignments based on filters.

-   **Forms:** the forms indicator provides a count of the reporting locations based on filters.

-   **Form Submissions:** the form submissions indicator provides a count of submitted reports based on filters and dimensions, such as expected, late and so on.

-   **Locations:** the location indicator provides a count of locations, such as active locations and similar.

-   **Users:** the users indicator provides a count for users, such as active users, Inactive users and so on.

Table 5.1 lists the filters and dimensions options available for system indicators. [These are not visible under the indicators menu but are useful when configuring widgets in Notebooks, Bulletins, Website Builder and so on.]{.mark}

Table 5.1. Filters and dimension options for system indicators

+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **System indicators** | **Dimensions**                                                                                                                                                                             |
+=======================+============================================================================================================================================================================================+
| Alerts                | -   No selection                                                                                                                                                                           |
|                       |                                                                                                                                                                                            |
|                       | -   Alerts triggered                                                                                                                                                                       |
|                       |                                                                                                                                                                                            |
|                       | -   Open alerts                                                                                                                                                                            |
|                       |                                                                                                                                                                                            |
|                       | -   Alerts closed                                                                                                                                                                          |
|                       |                                                                                                                                                                                            |
|                       | -   Closed alerts (not incl. auto-discarded)                                                                                                                                               |
|                       |                                                                                                                                                                                            |
|                       | -   Auto-discarded alerts                                                                                                                                                                  |
|                       |                                                                                                                                                                                            |
|                       | -   Alerts discarded                                                                                                                                                                       |
|                       |                                                                                                                                                                                            |
|                       | -   Alerts monitor                                                                                                                                                                         |
|                       |                                                                                                                                                                                            |
|                       | -   Alerts response                                                                                                                                                                        |
|                       |                                                                                                                                                                                            |
|                       | -   Alerts in verification                                                                                                                                                                 |
|                       |                                                                                                                                                                                            |
|                       | -   Alerts awaiting verification                                                                                                                                                           |
|                       |                                                                                                                                                                                            |
|                       | -   Alerts verified                                                                                                                                                                        |
|                       |                                                                                                                                                                                            |
|                       | -   Alerts discarded at verification                                                                                                                                                       |
|                       |                                                                                                                                                                                            |
|                       | -   Alerts monitoring at verification                                                                                                                                                      |
|                       |                                                                                                                                                                                            |
|                       | -   Alerts in risk assessment                                                                                                                                                              |
|                       |                                                                                                                                                                                            |
|                       | -   Alerts risk assessed                                                                                                                                                                   |
|                       |                                                                                                                                                                                            |
|                       | -   Alerts in outcome                                                                                                                                                                      |
|                       |                                                                                                                                                                                            |
|                       | -   Alerts awaiting outcome                                                                                                                                                                |
|                       |                                                                                                                                                                                            |
|                       | -   Alerts with outcome                                                                                                                                                                    |
|                       |                                                                                                                                                                                            |
|                       | -   Alerts discarded at the outcome                                                                                                                                                        |
|                       |                                                                                                                                                                                            |
|                       | -   Alerts monitoring at the outcome                                                                                                                                                       |
|                       |                                                                                                                                                                                            |
|                       | -   Alerts respond at the outcome                                                                                                                                                          |
|                       |                                                                                                                                                                                            |
|                       | -   Alerts (Low risk)                                                                                                                                                                      |
|                       |                                                                                                                                                                                            |
|                       | -   Alerts (Moderate risk)                                                                                                                                                                 |
|                       |                                                                                                                                                                                            |
|                       | -   Alerts (High risk)                                                                                                                                                                     |
|                       |                                                                                                                                                                                            |
|                       | -   Alerts (Very high risk)                                                                                                                                                                |
+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Assignments           | **Form**: select a form from the drop-down menu. If set as **No selection**, the filter does not apply.                                                                                    |
|                       |                                                                                                                                                                                            |
|                       | **Status**: select an appropriate option to filter by status. If set as **No** **selection**, the filter does not apply. Status options are **No selection**, **Active** and **Inactive**. |
+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Forms                 | **Form**: select a form from the drop-down menu. If set as **No selection**, the filter does not apply.                                                                                    |
+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Form Submissions      | **Form**: select the form.                                                                                                                                                                 |
|                       |                                                                                                                                                                                            |
|                       | **Dimension**: select the dimension. If set as **No selection**, the filter does not apply.                                                                                                |
+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                       | \- Submitted: a count of the reports submitted                                                                                                                                             |
|                       |                                                                                                                                                                                            |
|                       | \- Late: a count of the reports submitted after the due date                                                                                                                               |
|                       |                                                                                                                                                                                            |
|                       | \- Expected: a count of the reports to be submitted during the reporting period of the form                                                                                                |
|                       |                                                                                                                                                                                            |
|                       | \- Missing: calculated as (Expected -- Submitted)                                                                                                                                          |
|                       |                                                                                                                                                                                            |
|                       | \- Completeness: indicator value is a percentage, calculated as (100 × Submitted/Expected)                                                                                                 |
|                       |                                                                                                                                                                                            |
|                       | \- Timeliness: indicator value is a percentage, calculated as (100 × On time/Expected)                                                                                                     |
+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                       | **Source**: select the source. If set as **No selection**, the filter does not apply. Source options are:                                                                                  |
|                       |                                                                                                                                                                                            |
|                       | -   Mobile: a count of the reports submitted via EWARS Mobile                                                                                                                              |
|                       |                                                                                                                                                                                            |
|                       | -   Web: a count of the reports submitted via EWARS Web                                                                                                                                    |
|                       |                                                                                                                                                                                            |
|                       | -   Desktop: not yet implemented                                                                                                                                                           |
|                       |                                                                                                                                                                                            |
|                       | -   Short Message Service (SMS): not yet implemented                                                                                                                                       |
+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Locations             | **Status**: select the locations. If set as **No selection**, the filter does not apply. Options are:                                                                                      |
|                       |                                                                                                                                                                                            |
|                       | -   Active: a count of the active locations                                                                                                                                                |
|                       |                                                                                                                                                                                            |
|                       | -   Disabled: a count of the disabled locations                                                                                                                                            |
|                       |                                                                                                                                                                                            |
|                       | **Location Type**: select the location type to filter the locations. If set as **No selection**, the filter does not apply.                                                                |
+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Users                 | **Status**: select an appropriate option to filter by status. If set as **No selection**, the filter does not apply.                                                                       |
|                       |                                                                                                                                                                                            |
|                       | Options are:                                                                                                                                                                               |
|                       |                                                                                                                                                                                            |
|                       | -   Active: a count of the active users                                                                                                                                                    |
|                       |                                                                                                                                                                                            |
|                       | -   Inactive: a count of the inactive users                                                                                                                                                |
|                       |                                                                                                                                                                                            |
|                       | -   Pending Approval: a count of the users with their approval in pending status                                                                                                           |
|                       |                                                                                                                                                                                            |
|                       | **User Type**: select an appropriate option to filter by user type. If set as No selection, the filter does not apply.                                                                     |
|                       |                                                                                                                                                                                            |
|                       | Options are:                                                                                                                                                                               |
|                       |                                                                                                                                                                                            |
|                       | -   Reporting User                                                                                                                                                                         |
|                       |                                                                                                                                                                                            |
|                       | -   Geographical Administrator                                                                                                                                                             |
|                       |                                                                                                                                                                                            |
|                       | -   Account Administrator                                                                                                                                                                  |
+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

You can now use indicators to analyse data in EWARS -- for example, in Plots, Notebooks, Document Templates, Dashboards, Website Builder and so on. Indicators act as an important link between raw data collection in forms, analysis, visualization and, ultimately, timely action. The following chapter gives an overview of the Forms feature in EWARS.

# Chapter 6. Forms

This chapter provides an overview of the Forms feature. Forms are integral to any Early Warning, Alert and Response System (EWARS) account, and they serve as the prime instruments to capture information. Moreover, in any given emergency, forms help define the data collection requirements. So they need to be closely aligned with the overall objectives of EWARS in the given situation.

The chapter will help you to perform key actions using forms, thereby setting the stage for data collection activities according to the key objectives of your situation.

## 6.1 Forms and their uses

Forms are created in EWARS Web and can be viewed in EWARS Mobile for data collection purposes. However, mobile users cannot create, edit or modify forms: only web users are able to modify the forms.

Fig. 6.1 shows the usage of forms in capturing data and using it to display different information via dashboards, alarms, website and so on.

Fig. 6.1. EWARS forms

![Diagram Description automatically generated](media/image97.png){width="6.270833333333333in" height="3.1354166666666665in"}

You can create any number of reporting forms for early warnings. There are three types of standard forms:

-   weekly EWARS reporting forms for health facilities

-   immediate reporting forms

-   event-based surveillance forms.

There are two ways to create reporting forms for the system:

-   copy sample forms and edit them according to your needs

-   create a new form from scratch.

EWARS provides standard templates for each of the reporting forms in the Model account. You can copy them and adopt according to the needs of your context.

## 6.2 Copying the sample form to your account

The example below sets out how to copy the weekly EWARS reporting form from the Model account.

-   Select **Menu** \> **Configuration Transfer**. Select **Model account** from the **Source Account** drop-down menu. The system displays the **List of transferable items**. Select the **Weekly EWARS Reporting Form**. Click on the **transfer** ![](media/image98.png){width="0.3472222222222222in" height="0.3055555555555556in"} icon, and the form is copied to your account.

  ---------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![](media/image43.png){width="0.65625in" height="0.3541666666666667in"}   Weekly EWARS reporting forms, immediate reporting forms and event-based surveillance forms share the same format regardless of the country or the context. Therefore, during emergencies, copying a sample form and editing it saves time.

  ---------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The form is copied to your account along with its dependencies -- a set of indicators linked to the form. These copied indicators are available under the indicators menu.

To view the sample form as a preview, follow the steps below:

-   Select **Menu** \> **Forms** \> click on the **edit** ![](media/image99.png){width="0.21736111111111112in" height="0.20833333333333334in"} icon of the Weekly EWARS Reporting Form. Click on **Fields** \> click on **Preview**, and the screen below appears:

![](media/image100.png){width="5.800694444444445in" height="2.536111111111111in"}

To view the sample form in Report manager, follow the steps below:

-   Select **Menu** \> **Data Collection** \> **Report manager**. Click on **Weekly EWARS Reporting Form**, and the screen below appears:

![](media/image101.png){width="7.0in" height="3.638888888888889in"}

Refer to topic **6.5 Adding and configuring data fields in the form** for more information.

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** it is not compulsory to use a form copied via Configuration Transfer. Having copied a sample form, you can still create a new form from the beginning. In that case, the sample form can act as a true sample to inspire the development of a form you need, but you should be mindful of the dependencies you may have in the system that transferred with the copied form.
  --------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 6.3 Editing the sample form

You can edit the copied weekly EWARS reporting form sample form according to your requirements, as in the following examples.

**Example 1.** Remove the Suspected measles row from the Morbidity and mortality table.

-   Select **Menu** \> **Forms** \> click on the **edit** ![https://lh4.googleusercontent.com/DhOlrU_Sh44rnZs8cX4VHTgSsjorHU0wLVkY9JmVOvm-0Obbu1UMe5oaW-lgK3gCOnmuihei4Q_mfM4xFbZTMO044CYm2x8Ct2pen2zfrOR_qmrM6aWDWInX4DOdeg](media/image99.png){width="0.21875in" height="0.20833333333333334in"} icon in the **Weekly EWARS Reporting Form** \> click on the ![](media/image102.png){width="0.6083333333333333in" height="0.25833333333333336in"} tab, and the screen with the existing fields appears.

-   Look for the **Suspected Measles** row \> click on the **delete** ![](media/image41.png){width="0.3541666666666667in" height="0.3541666666666667in"} icon, and the row is removed from the table.

-   Click on **Preview** to preview it. Click on **Save Change(s)**.

**Example 2.** Add Bacterial meningitis to the Morbidity and mortality table.

To add a disease row for Bacterial meningitis in the Morbidity and mortality table, you need to add one matrix row field and four input fields -- for Under 5 cases, Under 5 deaths, Over 5 cases and Over 5 deaths.

A matrix row field is used inside the table (matrix) field to define rows within in. Refer to topic **6.5.3 Configuring the matrix row field** for more information.

-   Select **Menu** \> **Forms** \> click on the **edit** ![https://lh4.googleusercontent.com/DhOlrU_Sh44rnZs8cX4VHTgSsjorHU0wLVkY9JmVOvm-0Obbu1UMe5oaW-lgK3gCOnmuihei4Q_mfM4xFbZTMO044CYm2x8Ct2pen2zfrOR_qmrM6aWDWInX4DOdeg](media/image99.png){width="0.21875in" height="0.20833333333333334in"} icon of **Weekly EWARS Reporting Form** \> click on the ![](media/image102.png){width="0.6083333333333333in" height="0.25833333333333336in"} tab, and you the screen below with the existing fields appears:

![](media/image103.png){width="4.9847222222222225in" height="2.691666666666667in"}

-   Look for the **Morbidity and Mortality** table field \> click on the **add** ![https://lh6.googleusercontent.com/yXcBM3eEtYFT4MLeQOKQV49pCgAJFd2pMykrQ8h9XIkmnPnPGdXrU4tEiNFX3_PqmxbS7X-P0-6QvBWcRNKkZhzF9hsODDk00WM0FqhNJCofHJ6H3OQknaEDa4NDGA](media/image104.png){width="0.21875in" height="0.20833333333333334in"} icon, and a new field is created inside the table. Look for **New Field** at the bottom of the table \> click on the **expand** ![https://lh6.googleusercontent.com/LRl8Gl6tvpojKNk6zr5D8wjnifmkq9zck43NOCqhoHHfmVQ8un7jecw8oKFro7R0v1no3cb9Ria24HOb7cecB537TU4UffmglhQrJ2YfOFg2czcNtWpBtnvlXZz-Gg](media/image105.png){width="0.20833333333333334in" height="0.20833333333333334in"} icon, and the screen below appears:

![](media/image106.png){width="4.84375in" height="2.9090277777777778in"}

-   Enter "Bacterial Meningitis" as the **Field label** \> select the **Field type** as **Matrix Row Field** \> set **Show on Mobile?** to **Yes** \> set **Show** **row label** to **Yes**. \> Let the other options remain the defaults. The Bacterial Meningitis row is added.

Next, add an Input field for Under 5 cases.

-   Click on the **add** ![https://lh6.googleusercontent.com/yXcBM3eEtYFT4MLeQOKQV49pCgAJFd2pMykrQ8h9XIkmnPnPGdXrU4tEiNFX3_PqmxbS7X-P0-6QvBWcRNKkZhzF9hsODDk00WM0FqhNJCofHJ6H3OQknaEDa4NDGA](media/image104.png){width="0.21875in" height="0.20833333333333334in"} icon of Bacterial Meningitis, and **New Field** is added under the Bacterial Meningitis row. Click on the **expand** ![https://lh6.googleusercontent.com/LRl8Gl6tvpojKNk6zr5D8wjnifmkq9zck43NOCqhoHHfmVQ8un7jecw8oKFro7R0v1no3cb9Ria24HOb7cecB537TU4UffmglhQrJ2YfOFg2czcNtWpBtnvlXZz-Gg](media/image105.png){width="0.20833333333333334in" height="0.20833333333333334in"} icon of **New Field**.

-   Enter "Under 5 cases" as the **Field label** \> select the **Field type** as **Numeric Field**. Let the other options remain the defaults.

-   In the same way, add three more **Numeric Fields** with **Field labels** Under 5 deaths, Over 5 cases and Over 5 deaths.

-   Click on **Preview**, and the added row is visible, as shown below:

![](media/image107.png){width="5.626388888888889in" height="3.3465277777777778in"}

-   Click on **Save Change(s)**.

When you copy a sample form, dependencies such as indicators are also transferred to your account. However, when you make edits and modifications, you also must make changes to the dependencies -- i.e. the indicators. You need to map the form fields to the indicators in the system; otherwise, EWARS cannot link or make data accessible for analysis.

### 6.3.1 Linking form fields and indicators via the logic feature 

Every time you add a new field to the sample form, you need to modify the logic and link the indicator. For more information, refer to topic **6.6 Adding logic in the form**. If you don't have a matching indicator in the system, create indicators according to your requirements. For example, make sure you have created an indicator for Bacterial meningitis before you map the new form field and the indicator. To create an indicator, refer to **Chapter 5. Indicators**, topic **5.5 Creating indicators**.

-   Select **Menu** \> **Forms** \> click on the **edit** ![](media/image108.png){width="0.3020833333333333in" height="0.3020833333333333in"} icon of **Weekly EWARS Reporting Form** \> click on the **Logic** tab.

-   Click on **Add Indicator** \> click on the **expand** ![](media/image109.png){width="0.3125in" height="0.3125in"} icon to expand the indicator \> select the indicator Bacterial Meningitis Under 5 \> on the left-hand side. Click on **Form** \> click on **Data \[root\]** \> click on **Morbidity and Mortality \[matrix\]** to find the matching form field in the weekly EWARS reporting form for Bacterial Meningitis under 5 \> drag and drop the **Bacterial Meningitis** **Under 5 cases \[number\]** field from left to right on the selected indicator. These actions link the form field and the indicator.

-   Similarly, map the other three fields: Under 5 deaths, Over 5 cases and Over 5 deaths with the relevant indicators.

-   Click on **Save Change(s)**.

## 6.4 Creating a new form

You can create a new form if you have not copied the sample form to your account. Creating a form involves four major steps (Fig. 6.2).

Fig. 6.2. Steps to create a form

![](media/image110.png){width="6.044070428696413in" height="2.946484033245844in"}

Details of the steps are as follows:

-   **Settings** enables you to set up basic information related to the form, such as name, identifier (ID) and so on.

-   **Fields** enables you to set up all form fields.

-   **Logic** enables you to link form fields with the indicators in the system.

-   **Translation** enables you to set the language for the form.

The following steps set out how to create the form with basic information setting.

-   Select **Menu** \> **Forms**. Click on **New Form**, and the **Form Settings** screen below opens:

> ![](media/image111.png){width="4.969444444444444in" height="2.6993055555555556in"}

-   Add the **Form Title** (e.g. "EWARS reporting form").

-   Set Status as **Active**.

```{=html}
<!-- -->
```
-   **Active:** visible in the reporting manager menu and can be assigned to the users

-   **Archived**: archived forms no longer in use

-   **Draft:** forms that are yet to be completed or configured

```{=html}
<!-- -->
```
-   Keep **Is Sub Form?** disabled (assuming that you are creating a main form).

```{=html}
<!-- -->
```
-   If **Is Sub Form?** is enabled, you can create a sub form -- refer to topic **6.9 Creating a sub form** for more information.

```{=html}
<!-- -->
```
-   Enter a **Description** for the form.

-   Enter the **Submission electronic identification (EID) Prefix** (e.g. "FV1" for form version 1). The same form may have different versions, so you can add prefixes according to the versions, such as FV1, FV2 and so on.

```{=html}
<!-- -->
```
-   EWARS auto-generates a Submission EID for each submitted record. With the Submission EID Prefix, the user can identify the submitted records easily. For example, if the specified Submission EID Prefix is "FV1", the Submission EID will be in the format FV1-0B-9604-9601-D646. If the prefix is not set, then the Submission EID will be in the format 0B-9604-9601-D646.

```{=html}
<!-- -->
```
-   Enter a **Tag** for the form.

```{=html}
<!-- -->
```
-   A tag is an ID that will help you to find your form rapidly with a search field, especially when you have a number of forms to select from. You can add one or more tags or leave the field blank.

```{=html}
<!-- -->
```
-   Click on **Allow Export** to **enable** it. Exports allow the reporting data in the form to be exported as Excel or comma-separated values (CSV) formats. (For more information, refer to **Chapter 23. Exports**, topic **23.1 Exporting form submissions**). By default, it is **disabled.**

-   Click on **Save Change(s)**.

Once you have set up all the details under the **Settings** tab, move to the **Fields** tab.

## 6.5 Adding and configuring data fields in the form

  ---------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![](media/image43.png){width="0.65625in" height="0.3541666666666667in"}   Before you create an electronic form in EWARS, have your paper reporting form handy to guide you on the format. The electronic form looks like the paper form for all users.

  ---------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The next step is to configure the data fields. Various fields are available to develop the form in EWARS, such as text field, select field and date field. Follow the steps below to view all the available fields.

-   Select **Menu** \> **Forms** \> click on the **edit** ![](media/image40.png){width="0.3125in" height="0.2708333333333333in"} icon in your desired form. Click on the ![](media/image112.png){width="0.6770833333333334in" height="0.3229166666666667in"} tab, and the screen below appears:

![](media/image113.png){width="5.775in" height="3.6430555555555557in"}

This is where you can create data fields to report information. There are several types of fields, and you can choose which to use, according to your requirements. You can add a new field in two ways:

-   Drag any field and drop it on the right-hand side of the screen.

-   Click on **Add Field** to add a new field.

Regardless of the method you use to add form fields, they have common options to be configured. For example, if you want to add a location field, the following options of the form field are available:

![](media/image114.png){width="4.940277777777778in" height="4.284027777777778in"}

Before you start configuring the form fields, it is recommended that you go through the following explanation (Table 6.1).

Table 6.1. Fields and descriptions

+------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Field**              | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
+========================+================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
| **Field label**        | ![](media/image115.png){width="3.665277777777778in" height="0.40069444444444446in"}                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                        | This shows what data/information the user needs to provide in the field.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                        | When previewing the form or completing the form in EWARS Mobile, the field label appears, as shown below:                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                        | ![](media/image116.png){width="3.5902777777777777in" height="0.6152777777777778in"}                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                        | When the field label is set as name of reporting health facility for a text-input field, you need to specify the reporting health facility name.                                                                                                                                                                                                                                                                                                                                                                                               |
|                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                        | Use an appropriate field label.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
+------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Export label**       | ![](media/image117.png){width="3.326388888888889in" height="0.45in"}                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                        | Once you export the records of the form, the export label appears inside the CSV file as a data column label. Export label does not appear on the form.                                                                                                                                                                                                                                                                                                                                                                                        |
|                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                        | Give a name to the export label. If left blank while exporting, the column name becomes the field name.                                                                                                                                                                                                                                                                                                                                                                                                                                        |
+------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Field name**         | ![](media/image118.png){width="3.535416666666667in" height="0.4583333333333333in"}                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                        | This is an ID for the field, so it should be unique. For this purpose, when a user creates a new field, the field name is specified by the system automatically as, for example, "untitled_c6663d32". It is recommended that users should change the first part ("untitled") to an appropriate label to identify the field and leave the second part as it is.                                                                                                                                                                                 |
+------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Show on mobile?**    | ![](media/image119.png){width="2.0416666666666665in" height="0.4in"}                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                        | This can be set as **Yes** or **No**. If set as **Yes**, the field is visible on a mobile phone or tablet while the Reporting User is filling in the form. If set as **No**, the field is not visible while the form is being filled in on a mobile phone or tablet.                                                                                                                                                                                                                                                                           |
+------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Conditional logic**  | ![](media/image120.png){width="2.066666666666667in" height="0.4in"}                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                        | This can be set as **Yes** or **No**. If set as **Yes**, you can display or hide the field based on the set conditions. If the condition is satisfied, the selected field is visible; otherwise the field is hidden. If set as **No**, you can't set up the conditions.                                                                                                                                                                                                                                                                        |
|                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                        | To set up conditional logic, select **Yes**, and the rules editor appears, as shown below:                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                        | ![](media/image121.png){width="4.950694444444444in" height="0.41597222222222224in"}                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                        | -   Click on the **add** ![](media/image122.png){width="0.375in" height="0.3416666666666667in"} icon to add a rule, based on which the field will appear (or not) in the form. Select from the left-hand drop-down menu which field in the form needs be linked to the rule (e.g. Age), then select from the middle drop-down menu the relevant level for that rule (e.g. Greater than), and add the last section (e.g. 5). In this example, the field will only appear in the form when the person in the form is aged over 5 years. |
|                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                        | ![](media/image123.png){width="5.0in" height="0.4166666666666667in"}                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                        | ![](media/image124.png){width="5.0in" height="0.4583333333333333in"}                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                        | You can repeat the process to add multiple rules.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                        | If multiple rules are added, you also need to select one of the options **All of the following are true** or **Any of the following are true**, according to your needs.                                                                                                                                                                                                                                                                                                                                                                       |
|                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                        | For example, in a line list, imagine that the previous question is about case outcomes with an array of responses as below:                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                        | -   Alive                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                        | -   Dead                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                        | -   Discharged                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                        | -   Unknown.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                        | You can make the next question a conditional one, based on the response.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                        | For example, you can request the date of death:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                        | ![](media/image125.png){width="4.95625in" height="0.4166666666666667in"}                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                        | Similarly, you can request the date of discharge:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                        | ![](media/image126.png){width="4.95625in" height="0.40694444444444444in"}                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
+------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Display in**         | ![](media/image127.png){width="2.4090277777777778in" height="0.44166666666666665in"}                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **Main Record**        | This feature is applicable only to sub forms: it enables inclusion of a sub form field in the main form field. It can be set as **Yes** or **No**. If set as **Yes**, this field of the sub form is automatically displayed in the main form. If set as **No**, this field is not included in the main form.                                                                                                                                                                                                                                   |
+------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Required**           | ![](media/image128.png){width="1.4916666666666667in" height="0.38333333333333336in"}                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                        | If you want this field to be mandatory in the form, select **Yes**; if not, select **No**. All mandatory fields should be completed in a form. Without filling them in, the form cannot be submitted.                                                                                                                                                                                                                                                                                                                                          |
+------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Field instructions** | This relates to extra information you add to a field that can be used to complete it easily. This option is used to specify the exact input type you require. In Report manager, hover and click on the field label to view the field instructions. For example, you could add an instruction of "Please fill in block capitals" under the name of the reporting health facility:                                                                                                                                                              |
|                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                        | ![](media/image129.png){width="4.8590277777777775in" height="0.5416666666666666in"}                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                        | In the reporting form, if you hover over the question, the specific instructions are displayed as below:                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                        | ![](media/image130.png){width="4.96875in" height="1.3416666666666666in"}                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
+------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Default value**      | This is a predefined value that is used by the field when a user has not specified the value. When reporting a new record in EWARS Mobile or previewing a form, the default value specified in the field is auto-populated.                                                                                                                                                                                                                                                                                                                    |
|                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                        | For example, imagine a selected field type "Treatment received" has four values:                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                        | -   Oral rehydration solution                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                        | -   Intravenous (IV) fluids                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                        | -   Antibiotics                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                        | -   Not applicable.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                        | The default value can be set as IV fluids, as shown below:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                        | ![](media/image131.png){width="3.3159722222222223in" height="0.44166666666666665in"}                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                        | When reporting a new record in EWARS Mobile, assuming that the user has not selected any value in the "Treatment Received" field, since the default value is set as IV fluids, this is considered the value for the field "Treatment Received".                                                                                                                                                                                                                                                                                                |
+------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Redacted**           | ![](media/image132.png){width="1.8333333333333333in" height="0.375in"}                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                        | This helps to confirm which fields will be exported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                        | If set as **Yes**, you won't be able to see this field in the export file while performing the export. The field will not be exported.                                                                                                                                                                                                                                                                                                                                                                                                         |
|                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                        | If set as **No**, you will be able to see this field in the export file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
+------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Placeholder**        | This attribute specifies a short hint that describes the expected value of an input field. For example, "Enter your comments on the case" is the placeholder for the comments text area field:                                                                                                                                                                                                                                                                                                                                                 |
|                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                        | ![](media/image133.png){width="3.8402777777777777in" height="0.45in"}                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                        | When reporting a record in the EWARS Web version or previewing a form, the placeholder is visible inside the input field in grey text, as shown below:                                                                                                                                                                                                                                                                                                                                                                                         |
|                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                        | ![](media/image134.png){width="3.5416666666666665in" height="0.6486111111111111in"}                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                        | Once you enter the field value, the placeholder disappears.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
+------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

The following topics set out how to add and configure different fields in the reporting form.

### 6.5.1 Configuring the header field

The header field is used to provide the heading for the form, but it is not used to enter data.

-   Drag **Header Field** from the left-hand side and drop it on the right-hand side. Click on the **expand** ![](media/image109.png){width="0.3125in" height="0.3125in"} icon of the **Header Field**, and the screen below appears:

![](media/image135.png){width="5.852777777777778in" height="2.8618055555555557in"}

-   Enter a **Field label** (e.g. "Lab Report") \> set **Field type** as **Header Field** if not set \> change the **Field name** (e.g. to "rs_478s883").

-   Select **Header style** as **Title**. The header is displayed with the Title style, as shown below:

![](media/image136.png){width="4.966666666666667in" height="0.4409722222222222in"}

-   Alternatively, select **Header style** as **Sub-title**. The header is displayed with the Sub-title style, as shown below:

![](media/image137.png){width="6.294444444444444in" height="0.3909722222222222in"}

-   Click on **Save Change(s)**.

### 6.5.2 Configuring the table/matrix

Table/matrix arranges the form field in a tabular manner. It is used not to capture data but to arrange the fields.

If you would like to add a number field to the table field, you need to add matrix row field and numeric field as explained in **6.5.3 Configuring the matrix row field** and **6.5.4 Configuring the numeric field**

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** "table" and "matrix" are the same in EWARS: the names are used interchangeably.
  --------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-   Drag **Table/Matrix** from the left-hand side and drop it on the right-hand side. Click on the **expand** ![](media/image109.png){width="0.3125in" height="0.3125in"} icon of the **Table/Matrix**, and the screen below appears:

![](media/image138.png){width="5.2027777777777775in" height="2.578472222222222in"}

-   Enter a **Field label** (e.g. "Morbidity and Mortality") \> set **Field type** as **Matrix** if not set \> change the **Field name** (e.g. to "mr_478s884").

-   Click on **Save Change(s)**.

### 6.5.3 Configuring the matrix row field

If you have a table/matrix, it should be filled with matrix row fields. These are used inside the table/matrix to define rows inside the table (matrix).

-   Click on the **add** ![](media/image122.png){width="0.375in" height="0.3416666666666667in"} icon of the matrix field (e.g. the **Morbidity and Mortality** table), **and** a new **Matrix Row Field** is added. Click on the **expand** ![](media/image109.png){width="0.3125in" height="0.3125in"} icon of the **Matrix Row Field**, and the screen below appears:

![](media/image139.png){width="4.863888888888889in" height="3.178472222222222in"}

-   Enter a **Field label** (e.g. "Acute Watery Diarrhoea (AWD)") \> change the **Field name** (e.g. to "awd_84622e92").

-   **Show row label:** by default, the row label won't be visible. By enabling this feature, you can see the specified row label, as shown below:

![](media/image140.png){width="4.948611111111111in" height="1.2166666666666666in"}

-   Click on **Save Change(s)**.

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** you can add fields inside the row by clicking the add icon of the row.
  --------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The screenshot below depicts the table (matrix) field as morbidity and mortality, the matrix row field as acute watery diarrhoea (AWD) and the numeric field under 5 cases is added inside the matrix row field.

> ![](media/image141.png){width="6.59375in" height="1.7083333333333333in"}

### 6.5.4 Configuring the numeric field

You can use this field type to capture numeric values in the form.

-   Drag **Numeric Field** from the left-hand side and drop it on the right-hand side. Click on the **expand** ![](media/image109.png){width="0.3125in" height="0.3125in"} icon of the **Numeric Field**, and the screen below appears:

![](media/image142.png){width="5.425in" height="4.45in"}

-   Enter a **Field label** (e.g. "Under 5") \> set **Field type** as **Numeric** **Field** if not set \> change the **Field name** (e.g. to "u5_4266379"). You can select other options according to your requirements.

-   **Allow negative**: if set as **Yes**, a negative value can be entered into the field.

-   **Barcode**: if set as **Yes**, you can scan the barcode to input a value into the field, although you also have the option to enter/type it manually.

-   Click on **Save Change(s)**.

### 6.5.5 Configuring the text field

Text fields can be used to input small text values, such as the name of a person. They also support barcode scanning, as explained in the numeric field topic above.

-   Drag **Text Field** from the left-hand side and drop it on the right-hand side. Click on the **expand** ![](media/image109.png){width="0.3125in" height="0.3125in"} icon of the **Text Field**, and the screen below appears:

![](media/image143.png){width="4.449305555555555in" height="3.7368055555555557in"}

-   Enter a **Field label** (e.g. "Laboratory name") \> set **Field type** as **Text Field** if not set \> change the **Field name** (e.g. to "ln_e0cb049").

-   **Barcode**: if set as **Yes**, you can scan the barcode to input a value into the field, although you also have the option to enter/type it manually.

```{=html}
<!-- -->
```
-   Click on **Save Change(s)**.

### 6.5.6 Configuring the text area field

The text area field can be used to capture descriptive text that is longer than that in the text field (e.g. describing patient complaints).

-   Drag **Text area Field** from the left-hand side and drop it on the right-hand side. Click on the **expand** ![](media/image109.png){width="0.3125in" height="0.3125in"} icon of the **Text area Field**, and the screen below appears:

![](media/image144.png){width="4.228472222222222in" height="3.5659722222222223in"}

-   Enter a **Field label** (e.g. "Laboratory details") \> set **Field type** as **Text area Field** if not set \> change the **Field name** (e.g. to "ld_e0cb049").

-   Click on **Save Change(s)**.

### 6.5.7 Configuring the select field

The select field is used to add the drop-down menu list options to the form. Alternatively, you can upload a CSV file containing these options. To add options, you need to provide stored values and display values for the options. Display values are visible to the users on the screen, whereas stored values cannot be seen.

-   Drag **Select Field** from the left-hand side and drop it on the right-hand side. Click on the **expand** ![](media/image109.png){width="0.3125in" height="0.3125in"} icon of the **Select Field**, and the screen below appears:

![](media/image145.png){width="6.163194444444445in" height="3.4875in"}

-   Enter a **Field label** (e.g. "Reporting person") \> set **Field type** as **Select Field** if not set \> change the **Field name** (e.g. to "rp_5a0b9ce2").

You can add drop-down options to the select field in two ways.

-   To add **Options** by entering the **Stored Value** and **Display Value**:

```{=html}
<!-- -->
```
-   Click on the **add** ![](media/image146.png){width="0.3020833333333333in" height="0.2916666666666667in"} icon in the **Options Editor** \> enter, for example, "SUR" in **Stored Value** and "Surveillance Officer" in **Display Value**.

As shown above, you can continue to add options according to your requirements.

-   To add **Options** by uploading a CSV file:

```{=html}
<!-- -->
```
-   Create a CSV file, as shown below, and add the **Options** as required:

![](media/image147.png){width="3.579861111111111in" height="1.3229166666666667in"}

-   Click on **Choose File** \> select the CSV file. The **Options** are populated from the CSV file as shown below:

![](media/image148.png){width="5.086805555555555in" height="2.13125in"}

-   **Multi-Select**: by enabling this, a Reporting User can select more than one option in this field. By default, a Reporting User can select a single option from the list.

-   Click on **Save Change(s)**.

### 6.5.8 Configuring the date field

This field can be used to capture a particular date, week, month or year.

-   Drag **Date field** from the left-hand side and drop it on the right-hand side. Click on the **expand** ![](media/image109.png){width="0.3125in" height="0.3125in"} icon of the date field, and the screen below appears:

![](media/image149.png){width="6.330640857392826in" height="3.5214195100612424in"}

-   Enter a **Field label** (e.g. "Birth Date") \> set **Field type** as **Date field** if not set. Change the **Field name** (e.g. to "BD_5386e894").

-   **Date type**: This has four values: **Day**, **Weekly**, **Month** and **Year**. The default option is **Day**.

```{=html}
<!-- -->
```
-   When the **Day** option is selected, the user can pick any date. The options in the reporting form appear as below:

![](media/image150.png){width="2.951388888888889in" height="1.8576388888888888in"}

-   When the **ISO8601 Weekly** option is selected, the user can pick any week of any year:

![](media/image151.png){width="2.9097222222222223in" height="2.9583333333333335in"}

-   When the **Month** option is selected, the user can pick any month of any year:

![](media/image152.png){width="2.9166666666666665in" height="1.1743055555555555in"}

-   When the **Year** option is selected, the user can pick any year:

![](media/image153.png){width="4.78125in" height="0.5902777777777778in"}

-   Select an appropriate option (e.g. Day (the default)).

-   **Allow future dates**: by default, the date picker does not allow you to select a future date. By enabling this feature, users can select any future date.

-   Click on **Save Change(s)**.

### 6.5.9 Configuring the time field

The time field can be used to capture time in hours and minutes.

-   Drag **Time Field** from the left-hand side and drop it on the right-hand side. Click on the **expand** ![](media/image109.png){width="0.3125in" height="0.3125in"} icon of the **Time Field**, and the screen below appears:

![](media/image154.png){width="5.9847222222222225in" height="3.2131944444444445in"}

-   Enter a **Field label** (e.g. "Duration") \> set **Field type** as **Time Field** if not set \> change the **Field Name** (e.g. to "TM_5386e894").

-   Click on **Save Change(s)**.

### 6.5.10 Configuring the location field

The location field is used to capture a location name in the form. The location drop-down menu populates all the available locations in the country.

-   Drag **Location** field from the left-hand side and drop it on the right-hand side. Click on the **expand** ![](media/image109.png){width="0.3125in" height="0.3125in"} icon of the location field, and the screen below appears:

![](media/image155.png){width="5.4534722222222225in" height="3.7756944444444445in"}

-   Enter a **Field label** (e.g. "Location") \> set **Field type** as **Location** if not set \> change the **Field name** (e.g. to "location_5a0b9ce2").

You can restrict location selection to a specific location type.

-   **Location type**: by default, this is set as **No selection** and no restrictions apply. You can select any location while reporting. By configuring **Location type**, you can restrict location selection based on the selected **Location type**. Locations that appear in your drop-down menu are the locations present in the account settings.

```{=html}
<!-- -->
```
-   Select a **Location type** to restrict the selection (e.g. **Health facility**).

-   Click on **Save Change(s)**.

### 6.5.11 Configuring the Lat/Long field

You may want to capture global positioning system (GPS) coordinates of the reporting locations. You can add a data field to the reporting form to capture latitudes and longitudes with the Lat/Long field. Once you configure Lat/Long field in the form, Reporting Users can enter latitude and longitudinal data either by double tapping on the Lat/Long reporting field (only if location identification is enabled) or manually.

-   Drag **Lat/Long field** from the left-hand side and drop it on the right-hand side. Click on the **expand** ![](media/image109.png){width="0.3125in" height="0.3125in"} icon of the **Lat/Long** **field**, and the screen below appears:

![](media/image156.png){width="5.660548993875765in" height="3.1722659667541557in"}

-   Enter a **Field label** (e.g. "GPS Coordinates") \> set **Field type** as **Lat/Long field** if not set \> change the **Field name** (e.g. to "gps_5a0b9ce2").

-   Click on **Save Change(s)**.

### 6.5.12 Configuring the calculated (display)

This field is used to compute the sum or concatenate the source field(s) added. While you are completing the form in Report manager, the value in the calculated field is displayed as a non-editable display value. You cannot edit it directly, but you can fill in values inside the source field(s), and those values are updated automatically inside the calculated field.

-   Drag **Calculated** field from the left-hand side and drop it on the right-hand side. Click on the **expand** ![](media/image109.png){width="0.3125in" height="0.3125in"} icon of the **Calculated** field, and the screen below appears:

![](media/image157.png){width="6.395138888888889in" height="4.0993055555555555in"}

-   Enter a **Field label** (e.g. "Total AWD cases") \> set **Field type** as **Calculated (Display)** if not set \> change the **Field name** (e.g. to "total_awd_cases_9m99999").

-   To add **Source field(s)**, click on the **add** ![https://lh6.googleusercontent.com/yXcBM3eEtYFT4MLeQOKQV49pCgAJFd2pMykrQ8h9XIkmnPnPGdXrU4tEiNFX3_PqmxbS7X-P0-6QvBWcRNKkZhzF9hsODDk00WM0FqhNJCofHJ6H3OQknaEDa4NDGA](media/image104.png){width="0.21875in" height="0.20833333333333334in"} icon \> select a **Numeric Field** from the drop-down menu (e.g. Under 5 AWD Cases) \> click on the **add** ![https://lh6.googleusercontent.com/yXcBM3eEtYFT4MLeQOKQV49pCgAJFd2pMykrQ8h9XIkmnPnPGdXrU4tEiNFX3_PqmxbS7X-P0-6QvBWcRNKkZhzF9hsODDk00WM0FqhNJCofHJ6H3OQknaEDa4NDGA](media/image104.png){width="0.21875in" height="0.20833333333333334in"} icon \> select another **Numeric Field** from the drop-down menu (e.g. Over 5 AWD Cases). Select **Sum** as the **Operator type**:

![](media/image158.png){width="4.5256944444444445in" height="1.8833333333333333in"}

When previewing the form field, you can enter the numeric values in Under 5 AWD Cases and Over 5 AWD Cases, and the total is counted automatically in the **Calculated** field:

![](media/image159.png){width="3.1180555555555554in" height="2.0743055555555556in"}

-   Alternatively, you can click on the **add** ![https://lh6.googleusercontent.com/yXcBM3eEtYFT4MLeQOKQV49pCgAJFd2pMykrQ8h9XIkmnPnPGdXrU4tEiNFX3_PqmxbS7X-P0-6QvBWcRNKkZhzF9hsODDk00WM0FqhNJCofHJ6H3OQknaEDa4NDGA](media/image104.png){width="0.21875in" height="0.20833333333333334in"} icon \> select a text field from the drop-down menu (e.g. Case name). Click again on the **add** ![https://lh6.googleusercontent.com/yXcBM3eEtYFT4MLeQOKQV49pCgAJFd2pMykrQ8h9XIkmnPnPGdXrU4tEiNFX3_PqmxbS7X-P0-6QvBWcRNKkZhzF9hsODDk00WM0FqhNJCofHJ6H3OQknaEDa4NDGA](media/image104.png){width="0.21875in" height="0.20833333333333334in"} icon \> select **CONCATE** in **Operator type** \> enter a **Separator** for concatenation (e.g. "-").

![](media/image160.png){width="4.385416666666667in" height="2.2416666666666667in"}

-   While previewing the form field, you can enter text in **Case name**, and a numeric value in age; the concatenated string is displayed automatically in the **Calculated** field:

![](media/image161.png){width="3.0076388888888888in" height="2.442361111111111in"}

-   Click on **Save Change(s)**.

## 6.6 Adding logic in the form

After successfully creating a form with the form fields above, you need to connect the form fields with the indicators in the system. Otherwise, EWARS cannot link or make data accessible for analysis.

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** form fields and indicators should be pre-created in the system before adding the logic.
  --------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The following sections illustrate how you can match form fields with the indicators.

-   Select **Menu** \> **Forms**. Click on the **edit** ![https://lh3.googleusercontent.com/zDFDg2XQMCZonzvBeIA69lhtqEPuyWBMMAf2wCVyaAfia5Cc7ja3n58o6y32WZSZKQQTmoUPmxDxWuX1MD2p58pwB7oDY6fDXVnpMHfuWcfepd1l0pTv8txJPmidv-W5ZoTIw8Q](media/image162.png){width="0.23958333333333334in" height="0.23958333333333334in"} icon in your desired form \> click on the **Logic** tab.

Click on the **folder** ![](media/image88.png){width="0.25833333333333336in" height="0.23194444444444445in"} icon to expand that folder, and you will see the form fields you have created in the new form, as shown below:

![](media/image163.png){width="6.2243055555555555in" height="2.839583333333333in"}

For demonstration purposes, this guide uses the following three examples.

**Example 1.** You have a form field that collects under 5 AWD cases, and you want to link the data with the under 5 AWD indicator.

-   Click on **Add Indicator** \> expand the indicator using the **expand** ![https://lh6.googleusercontent.com/LRl8Gl6tvpojKNk6zr5D8wjnifmkq9zck43NOCqhoHHfmVQ8un7jecw8oKFro7R0v1no3cb9Ria24HOb7cecB537TU4UffmglhQrJ2YfOFg2czcNtWpBtnvlXZz-Gg](media/image105.png){width="0.21875in" height="0.21875in"} icon \> select the indicator from the drop-down menu (e.g. AWD Under 5). Drag the relevant form field from the left-hand side and drop it on the right-hand side.

![](media/image164.png){width="5.8902777777777775in" height="2.025in"}

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** indicators can hold only numeric values, so you can only drag a numeric field.
  --------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-   Click on **Save Change(s)**.

The two examples below illustrate how a complex set in the form logic can be used to connect data fields to indicators. A complex set is used when the connection between data field and the indicator is not simple or straightforward. Example 2 illustrates how a complex set can be used to connect a text field with an indicator. Example 3 is about connecting several data fields in the same form with one indicator.

**Example 2.** You have a text field that collects information on cholera from the event-based surveillance form, and you want to link these data with the disease indicator Cholera total cases, which usually collects suspected cholera from the weekly EWARS form.

-   Select **Event-Based Surveillance Form** \> click on the **edit** ![https://lh3.googleusercontent.com/zDFDg2XQMCZonzvBeIA69lhtqEPuyWBMMAf2wCVyaAfia5Cc7ja3n58o6y32WZSZKQQTmoUPmxDxWuX1MD2p58pwB7oDY6fDXVnpMHfuWcfepd1l0pTv8txJPmidv-W5ZoTIw8Q](media/image162.png){width="0.23958333333333334in" height="0.23958333333333334in"} icon \> click on the **Logic** tab \> click on the **folder** ![](media/image88.png){width="0.25833333333333336in" height="0.23194444444444445in"} icon to expand the **Form** folder and then the **Data \[root\]** folder to view the form fields.

-   Click on **Add Indicator** \> click on the **expand** ![](media/image109.png){width="0.3125in" height="0.3125in"} icon to expand the indicator \> select the indicator Total Cholera Cases from the drop-down menu. Drag and drop **Complex Set** from the left-hand side to the right-hand side of the expanded indicator.

-   Click on the **add** ![https://lh6.googleusercontent.com/yXcBM3eEtYFT4MLeQOKQV49pCgAJFd2pMykrQ8h9XIkmnPnPGdXrU4tEiNFX3_PqmxbS7X-P0-6QvBWcRNKkZhzF9hsODDk00WM0FqhNJCofHJ6H3OQknaEDa4NDGA](media/image104.png){width="0.21875in" height="0.20833333333333334in"} icon to add a condition. In the added condition, select the matching text field from the left-hand drop-down menu (e. g. Likely Disease) \> select **Is equal to** in the middle comparator \> enter the text you wish to compare (e. g. "Cholera") in the text box, as shown below:

![](media/image165.png){width="6.307692475940508in" height="1.7836920384951882in"}

This ensures that any text field in the event-based surveillance form or any other form can be matched with the existing indicator.

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** you can apply conditions to the date field, numeric field and select field as well.
  --------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If the condition is satisfied, the indicator value is the value of the field mapped; otherwise, a null value is returned.

-   Click on **Save Change(s)**.

**Example 3.** You have an indicator in the system called "Cholera deaths 15--44", but there is no single data field in the cholera line list form that collects these data. You have to constitute the data on cholera deaths in the age range 15--44 years to feed in to the indicator with a complex set. A complex set will allow you to set conditions, enabling capturing deaths in the age range 15--44 years that will eventually feed in to the indicator.

-   Select the **Cholera Line List** form \> click on the **edit** ![https://lh3.googleusercontent.com/zDFDg2XQMCZonzvBeIA69lhtqEPuyWBMMAf2wCVyaAfia5Cc7ja3n58o6y32WZSZKQQTmoUPmxDxWuX1MD2p58pwB7oDY6fDXVnpMHfuWcfepd1l0pTv8txJPmidv-W5ZoTIw8Q](media/image162.png){width="0.23958333333333334in" height="0.23958333333333334in"} icon \> click on the **Logic** tab \> click on **Add Indicator** \> select the indicator Cholera deaths 15-44 from the drop-down menu \> drag and drop **Complex Set** from the left-hand side to the right-hand side of the expanded indicator.

-   Click on the **add** ![](media/image166.png){width="0.2916666666666667in" height="0.3125in"} icon to add a condition row. Select the data field Age from the form's drop-down menu \> select the comparator **Is greater than or equal to** \> enter "15" in the final cell.

-   To add the next condition click on the **add** ![](media/image166.png){width="0.2916666666666667in" height="0.3125in"} icon, and one more condition row is added. Select the data field Age from the form's drop-down menu \> select the comparator **Is less than** \> enter "45" in the final cell.

-   Click on the **add** ![](media/image166.png){width="0.2916666666666667in" height="0.3125in"} icon to add the third condition \> select the data field Outcome from the form's drop-down menu \> select the comparator **Is equal to** \> select Dead in the final cell.

-   As you want all three conditions to be fulfilled to connect the data with the indicator, select **ALL of the following are TRUE** from the **Complex Set** options. Information will be fed to the indicator when only conditions that fulfil your instructions are met, as shown below:

![](media/image167.png){width="6.114583333333333in" height="2.732638888888889in"}

Each added condition is evaluated independently with the result TRUE or FALSE, and then based on the ALL or ANY selection, the result is obtained.

-   Click on **Save Change(s)**.

## 6.7 Translating the form into a preferred language

The translation tab is used to provide multilingual labels for the form and its field labels. This is needed when the user interface of your account is displayed in one language (such as English), but the reporting forms in the EWARS Mobile version will be completed by people who use another language (such as French).

If your account is created in a language other than English, only the system labels are translated at the time of account creation: the form fields that are dynamic need to be translated.

-   Select **Menu** \> **Forms**. Click on the **edit** ![https://lh3.googleusercontent.com/zDFDg2XQMCZonzvBeIA69lhtqEPuyWBMMAf2wCVyaAfia5Cc7ja3n58o6y32WZSZKQQTmoUPmxDxWuX1MD2p58pwB7oDY6fDXVnpMHfuWcfepd1l0pTv8txJPmidv-W5ZoTIw8Q](media/image162.png){width="0.23958333333333334in" height="0.23958333333333334in"} icon in your desired form \> click on the **Translation** tab, and the screen below appears:

![](media/image168.png){width="5.7in" height="3.441666666666667in"}

This is where you can provide multilingual labels to the form and fields, according to the language set in the account settings.

For example, if form field labels are configured in English and you require them in French, you need to translate them from English to French as follows.

-   Select a **preferred language** (e.g. French) from the language drop-down menu. Check all the **Labels** to translate \> click on **Auto-translate,** and the labels are translated into the new language. Go through and **make changes** if required \> click on **Save Change(s)**.

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** if you do not see the desired language in the language drop-down menu, it needs to be added to the account.
  --------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To find out more about adding languages, refer to **Chapter 10. EWARS account settings**, topic **10.6.4 Adding a new language to your account**.

## 6.8 Enabling specific features

Once you have created the new form, you can enable specific features such as interval-based reporting, set up overdue thresholds and location-based reporting, and enable unique ID generation and amendments, as shown below:

![](media/image169.png){width="5.256944444444445in" height="2.848611111111111in"}

Interval-based reporting and location-based reporting have an impact on data analysis -- for example, if you enable interval-based reporting, the report date field is added to the form automatically, and if you enable location-based reporting, you don't need to add a location field explicitly as the location field with its options is generated automatically.

### 6.8.1 Enabling interval-based reporting

When you enable interval-based reporting, the reporting must be done on a predefined basis (e.g. daily, weekly, monthly or yearly).

-   Select **Menu** \> **Forms**. Click on the **edit** ![https://lh3.googleusercontent.com/zDFDg2XQMCZonzvBeIA69lhtqEPuyWBMMAf2wCVyaAfia5Cc7ja3n58o6y32WZSZKQQTmoUPmxDxWuX1MD2p58pwB7oDY6fDXVnpMHfuWcfepd1l0pTv8txJPmidv-W5ZoTIw8Q](media/image162.png){width="0.23958333333333334in" height="0.23958333333333334in"} icon of the form (e.g. Weekly EWARS Reporting Form). Look for **Interval-Based Reporting** visible under **Features** \> click on the **toggle** ![](media/image170.png){width="0.38819444444444445in" height="0.27708333333333335in"} icon to enable it, and the icon colour changes to green. Click on the **expand** ![https://lh6.googleusercontent.com/LRl8Gl6tvpojKNk6zr5D8wjnifmkq9zck43NOCqhoHHfmVQ8un7jecw8oKFro7R0v1no3cb9Ria24HOb7cecB537TU4UffmglhQrJ2YfOFg2czcNtWpBtnvlXZz-Gg](media/image105.png){width="0.21875in" height="0.21875in"} icon \> select an interval (Daily, Weekly, Monthly or Yearly) from the **Reporting Interval** drop-down menu. Click on **Save Change(s)**.

### 6.8.2 Setting an overdue threshold for interval-based reporting

The overdue threshold is the extra time interval you are allowed after the reporting due date for submission is reached. Note that you can still submit a report, even if the overdue threshold time interval is exceeded. This will have an impact on the timeliness of reporting, however, as this will decrease as the threshold time increases.

-   Select **Menu** \> **Forms**. **C**lick on the **edit** ![https://lh3.googleusercontent.com/zDFDg2XQMCZonzvBeIA69lhtqEPuyWBMMAf2wCVyaAfia5Cc7ja3n58o6y32WZSZKQQTmoUPmxDxWuX1MD2p58pwB7oDY6fDXVnpMHfuWcfepd1l0pTv8txJPmidv-W5ZoTIw8Q](media/image162.png){width="0.23958333333333334in" height="0.23958333333333334in"} icon of the form (e.g. Weekly EWARS Reporting Form). Look for **Overdue Thresholds** visible under **Features** \> click on the **toggle** ![](media/image170.png){width="0.38819444444444445in" height="0.27708333333333335in"} icon to enable it, and the icon colour changes to green. Click on the **expand** ![https://lh6.googleusercontent.com/LRl8Gl6tvpojKNk6zr5D8wjnifmkq9zck43NOCqhoHHfmVQ8un7jecw8oKFro7R0v1no3cb9Ria24HOb7cecB537TU4UffmglhQrJ2YfOFg2czcNtWpBtnvlXZz-Gg](media/image105.png){width="0.21875in" height="0.21875in"} icon \> select an overdue interval type (Day(s), Week(s), Month(s) or Year(s)) \> enter the **Overdue Threshold** value as the number of intervals of the selected type. Click on **Save Change(s)**.

For example, to set an overdue threshold of three days, set overdue interval type as day(s) and the overdue threshold value as "3".

If the EWARS epidemiological week (epi week) is set from Sunday to Saturday in the system and the overdue threshold is set as three days (i.e. Tuesday), any forms submitted after Tuesday are considered late submissions. If you don't set the overdue threshold, any report submitted after Saturday is considered late.

### 6.8.3 Restricting reporting to a particular location type

If this feature is not enabled, then the Reporting User can select any location as they report, but you can restrict reporting to administrative locations.

For example, you can restrict reporting to the health facility location type as follows.

-   Select **Menu** \> **Forms**. Click on the **edit** ![https://lh3.googleusercontent.com/zDFDg2XQMCZonzvBeIA69lhtqEPuyWBMMAf2wCVyaAfia5Cc7ja3n58o6y32WZSZKQQTmoUPmxDxWuX1MD2p58pwB7oDY6fDXVnpMHfuWcfepd1l0pTv8txJPmidv-W5ZoTIw8Q](media/image162.png){width="0.23958333333333334in" height="0.23958333333333334in"} icon in your desired form (e.g. Weekly EWARS Reporting Form). Look for **Location-Based Reporting** visible under **Features** \> click on the **toggle** ![](media/image170.png){width="0.38819444444444445in" height="0.27708333333333335in"} icon to enable it, and the icon colour changes to green. Click on the **expand** ![](media/image109.png){width="0.3125in" height="0.3125in"} icon \> select the **Location type** Health Facility from the drop-down menu. Click on **Save Change(s)**.

### 6.8.4 Enabling unique ID generation for the form

You can configure a unique ID in two ways, as outlined below.

#### 6.8.4.1 Using the field of the form as a unique ID

This method is useful in cases of line listing, where you are capturing a government-issued ID card number as part of the form (e.g. a social security number, tax registration number, health card ID or similar).

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** to use the field of the form as a unique ID, you should have a unique ID field in the reporting form.
  --------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-   Select **Menu** \> **Forms**. Click on the **edit** ![](media/image108.png){width="0.3020833333333333in" height="0.3020833333333333in"} icon in your desired form (e.g. Weekly EWARS Reporting Form). Look for **Enable Unique ID Generation** visible under **Features** \> click on the **toggle** ![](media/image170.png){width="0.38819444444444445in" height="0.27708333333333335in"} icon to enable it, and the icon colour changes to green. Click on the **expand** ![](media/image109.png){width="0.3125in" height="0.3125in"} icon \> select a field from the **Unique ID Field Name** drop-down menu. Click on **Save Change(s)**.

#### 6.8.4.2 Auto-generating a unique ID on form submissions

This method is useful when no unique information is being captured as part of the form, but it needs to be generated automatically, based on the reporting form prefix, location prefix and serial number. Decide what prefix should be used for locations and forms before generating the unique ID. Prefixes can be easily understood abbreviated names for forms and locations (e.g. "CCRF" for Community Case Reporting Form and "AIM" for Aimal province), followed by a serial number with five digits (e.g. 00001).

-   Select **Menu** \> **Forms**. Click on the **edit** ![https://lh3.googleusercontent.com/zDFDg2XQMCZonzvBeIA69lhtqEPuyWBMMAf2wCVyaAfia5Cc7ja3n58o6y32WZSZKQQTmoUPmxDxWuX1MD2p58pwB7oDY6fDXVnpMHfuWcfepd1l0pTv8txJPmidv-W5ZoTIw8Q](media/image162.png){width="0.23958333333333334in" height="0.23958333333333334in"} icon in your desired form (e.g. Weekly EWARS Reporting Form). Look for **Enable Unique ID Generation** visible under **Features** \> click on the **toggle** ![](media/image170.png){width="0.38819444444444445in" height="0.27708333333333335in"} icon to enable it, and the icon colour changes to green. Click on the **expand** ![https://lh6.googleusercontent.com/LRl8Gl6tvpojKNk6zr5D8wjnifmkq9zck43NOCqhoHHfmVQ8un7jecw8oKFro7R0v1no3cb9Ria24HOb7cecB537TU4UffmglhQrJ2YfOFg2czcNtWpBtnvlXZz-Gg](media/image105.png){width="0.21875in" height="0.21875in"} icon \> click on the **toggle** ![](media/image170.png){width="0.38819444444444445in" height="0.27708333333333335in"} icon to enable **Generate unique sequence** on form submissions, and the icon colour changes to green.

-   Select the location type (e.g. Provinces) from the **Prefix Location type** drop-down menu.

-   Set a location prefix for each province as follows:

```{=html}
<!-- -->
```
-   Select **Menu** \> **Locations**. Expand the location hierarchy by clicking on the **folder** ![](media/image171.png){width="0.275in" height="0.31527777777777777in"} icon \> click on location name, and the location details appear at the right-hand side. Enter the location **Prefix** (e.g. "AIM" for Aimal). Click on **Save Change(s)**.

```{=html}
<!-- -->
```
-   Select the required number of digits from the **Serial number length** drop-down menu (e.g. 5), and the serial numbers will have five digits (e.g. 00001).

```{=html}
<!-- -->
```
-   Enter the **Form Prefix** (e.g. "CCRF").

```{=html}
<!-- -->
```
-   Click on **Save Change(s)**.

On submission of the form report, the system auto-generates a unique ID based on the above configuration.

The format of unique IDs is form prefix-location prefix-serial number. For example, in the Unique ID CCRF-AIM-PHC1-000001, CCRF is the form prefix, AIM-PHC1 is the location prefix and 000001 is the serial number.

### 6.8.5 Enabling approval requirement for amendments

You can require the Account Administrator's approval to enable an amendment to a report that has already been submitted. By default, this is disabled, and approval is not required.

This feature allows you to ensure that submitted data cannot be changed without the approval of the Account Administrator.

-   Select **Menu** \> **Forms**. Click on the **edit** ![https://lh3.googleusercontent.com/zDFDg2XQMCZonzvBeIA69lhtqEPuyWBMMAf2wCVyaAfia5Cc7ja3n58o6y32WZSZKQQTmoUPmxDxWuX1MD2p58pwB7oDY6fDXVnpMHfuWcfepd1l0pTv8txJPmidv-W5ZoTIw8Q](media/image162.png){width="0.23958333333333334in" height="0.23958333333333334in"} icon in your desired form (e.g. Weekly EWARS Reporting Form). Look for **Amendments** visible under **Features** \> click on the **toggle** ![](media/image170.png){width="0.38819444444444445in" height="0.27708333333333335in"} icon to enable it, and the icon colour changes to green. Click on the **expand** ![](media/image109.png){width="0.3125in" height="0.3125in"} icon \> click on the **toggle** ![](media/image170.png){width="0.38819444444444445in" height="0.27708333333333335in"} icon to enable **Require approval**, and the icon colour changes to green. Click on **Save Change(s)**.

For more information, refer to **Chapter 9. User profiles, tasks and notifications**, topic **9.5.4 Performing amendment requests**.

## 6.9 Creating a sub form

In EWARS, two or more forms can be linked together. They can be categorized as main forms and sub forms, based on their lineage. For example, cholera line list is the main form, which can have sub forms of cholera laboratory confirmation form under each patient.

Sub forms are used to capture additional information for the main form. They are associated with a main form via an identity field. Examples of identity fields are government-issued unique card numbers, health card numbers, tax registration numbers, mobile phone numbers and any other unique generated codes.

If the main form does not have any such identity field, you need to enable the feature enable unique ID generation. Refer to topic **6.8.4 Enabling unique ID generation for the form** for more information.

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** to create a sub form, ensure that the main form is already created.
  --------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Follow the steps below to create and configure a sub form.

**Step 1.** Create a sub form and set its options.

-   Select **Menu** \> **Forms**. Click on **New Form**, and the screen below appears:

![](media/image172.png){width="5.872916666666667in" height="3.807638888888889in"}

-   Add the **Form Title** (e.g. "Cholera Laboratory confirmation form").

-   Set **Status** as **Active**.

-   Click on the **toggle** ![](media/image170.png){width="0.38819444444444445in" height="0.27708333333333335in"} icon to enable **Is Sub Form?** ![](media/image173.png){width="1.3430555555555554in" height="0.35in"}

After the **Is Sub Form?** option is enabled, the form is categorized as a sub form and you need to select a main form for it.

-   Select a **Main Form** from the drop-down menu (e.g. "Cholera Line List").

-   Enter a **Description** for the form.

-   Leave the **Submission EID Prefix** and **Tag** fields blank.

-   Click on the **toggle** ![](media/image170.png){width="0.38819444444444445in" height="0.27708333333333335in"} icon to enable **Allow Export**, allowing the export of the form records via **Menu** \> **Exports**. By default, this feature is disabled.

-   Click on **Save Change(s)**.

**Step 2.** Add the identity field of the main form to the sub form.

-   Click on the ![https://lh4.googleusercontent.com/uhilYtkh7LvZboXeTX3g51518mO6ST7AJCI20HWFDUGVK3VVERKAIMOerGDD8sQEZDfXExZWsrwwtJ6haksnR5EVMA7KwyfUGlkpwX_vJ7FVxErNoe29Ua8OVu2NvKQANRKpqQM](media/image174.png){width="0.6145833333333334in" height="0.2604166666666667in"} tab \> click on **Add Field** \> look for the newly added field and click on the **expand** ![](media/image175.png){width="0.28125in" height="0.2916666666666667in"} icon. Enter a **Field label** (e.g. "Patient ID") \> set **Field type** to **Main form field** \> select an identity field from the **Main form fields** drop-down menu (e.g. Patient ID) \> set **Is Editable** as **Yes** \> set all other field options as **No**.

-   Click on **Save Change(s)**.

**Step 3.** Configure the sub form.

For additional configuration of the sub form refer to the relevant topics below.

-   To add and configure the fields, refer to topic **6.5 Adding and configuring data fields in the form**.

-   To add **Logic**, refer to topic **6.6 Adding logic in the form**.

-   To add **Translations**, refer to topic **6.7 Translating the form into a preferred language**.

-   To enable **Interval-Based Reporting**, refer to topic **6.8.1 Enabling interval-based reporting**.

-   To set **Overdue Thresholds** for **Interval-Based Reporting**, refer to topic **6.8.2 Setting an overdue threshold for interval-based** **reporting**.

-   To restrict a reporting form to a particular location type, such as Health Facility, refer to topic **6.8.3 Restricting reporting to a particular location type**.

-   To enable **Unique ID Generation**, refer to topic **6.8.4 Enabling unique ID generation for the form**

-   To enable **Approval** requirement for Amendments, refer to topic **6.8.5 Enabling approval requirement for amendments**.

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** when you update a sub form, the main form is updated automatically.
  --------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 6.10 Duplicating a form

This feature allows you to duplicate a form and modify that form in the same account, according to your needs.

-   Select **Menu** \> **Forms**. Look for the form (e.g. Weekly EWARS Reporting Form). Click on the **duplicate** ![](media/image176.png){width="0.3229166666666667in" height="0.3333333333333333in"} icon. Click on **Confirm**. A form with the name "Weekly EWARS Reporting Form copy" is created, as shown below:

![](media/image177.png){width="6.3902777777777775in" height="0.15416666666666667in"}

You can then rename the form as follows.

-   Select the duplicated form Weekly EWARS Reporting Form copy \> click on the **edit** ![https://lh3.googleusercontent.com/zDFDg2XQMCZonzvBeIA69lhtqEPuyWBMMAf2wCVyaAfia5Cc7ja3n58o6y32WZSZKQQTmoUPmxDxWuX1MD2p58pwB7oDY6fDXVnpMHfuWcfepd1l0pTv8txJPmidv-W5ZoTIw8Q](media/image162.png){width="0.23958333333333334in" height="0.23958333333333334in"} icon \> change the **Form Title**, and the form is renamed. Click on **Save Change(s)**.

## 6.11 Downloading and uploading forms

This feature allows you to download a form from EWARS and upload it to an EWARS account when needed.

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** the uploaded/imported form will not contain the fields and logic set under the settings and logic tabs, so you will need to reconfigure them.
  --------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Step 1.** Download an existing form to the user's system.

-   Select **Menu** \> **Forms**. Go to the Weekly EWARS Reporting Form \> click on the **export** ![](media/image178.png){width="0.2916666666666667in" height="0.2916666666666667in"} icon. The exported form (**form_export.ewars_form**) is downloaded to the desktop, as shown below:

![](media/image179.png){width="2.3381944444444445in" height="0.4638888888888889in"}

**Step 2.** Upload the downloaded form to an EWARS account.

-   Select **Menu** \> **Forms**. Click on **Import Form** at the top right-hand corner. Click on **Choose File**, and the file chooser option opens. Select **form_export.ewars_form** from the local directory structure. Click on **Open**, and **form_export.ewars_form** is uploaded. The screen below appears:

![](media/image180.png){width="4.863194444444445in" height="2.8631944444444444in"}

-   Click on **Save Change(s)**.

## 6.12 Pinning and grouping forms for Report manager

Forms within EWARS can be grouped into categories, based on their common characteristics. These groups are visible to users inside Report manager.

The screenshot below shows the Model account/Report manager, outlining the pinned form and form groups.

![](media/image181.png){width="3.4974551618547682in" height="3.1566994750656168in"}

The following topics set out how to pin and group the forms.

### 6.12.1 Pinning a form

Forms added to the pinned group appear at the top of Report manager. All other groups appear below this.

-   Select **Menu** \> **Forms**. Click on **Form Groups**, and the screen below appears:

![](media/image182.png){width="5.832638888888889in" height="2.8270833333333334in"}

The forms are listed at the left-hand side, a default pinned group is set up, and a manually added early warning group is below this.

-   Drag a form (e.g. Weekly EWARS Reporting Form) from the left-hand side to the **Drop Forms Here** box on the pinned section, and the form is pinned, as shown below:

![](media/image183.png){width="5.76875in" height="1.304861111111111in"}

-   Click on **Save Change(s)**.

You can then view pinned forms in Report manager.

-   Select **Menu** \> **Report manager** \> Look for pinned forms at the left-hand side, as shown below:

![](media/image184.png){width="4.229861111111111in" height="1.9701388888888889in"}

The forms are listed at the left-hand side, and the form is available in the **Pinned** group at the top, as shown in the screenshot above.

### 6.12.2 Adding a new form group

You can add new groups to organize the forms, based on common characteristics.

-   Select **Menu** \> **Forms**. click on the **Form Groups** tab \> click on **Add Group at** the top right-hand corner, and a **New Group** is added. Click on the added group name \> change it to "Early Warning", and the group is added, as shown below:

![](media/image185.png){width="5.39798009623797in" height="2.6359076990376202in"}

-   Click on **Save Change(s)**.

### 6.12.3 Adding forms to a form group

-   Select **Menu** \> **Forms**. Click on the **Form Groups** tab \> drag the forms (e.g. Weekly EWARS Reporting Form and Event-Based Surveillance Form) from the left-hand side to the **Drop Forms Here** box under the **Early Warning** group, as shown below:

![](media/image186.png){width="5.295138888888889in" height="1.3555555555555556in"}

-   Click on **Save Change(s)**, and the forms are added to the group.

### 6.12.4 Ordering a form group

You can change the order of the form group, and it will be reflected in the Report manager menu. The top-most group is always the pinned group; other groups are ordered below it.

-   Select **Menu** \> **Forms**. Click on the **Form Groups** tab \> click on the **up** ![](media/image187.png){width="0.25in" height="0.21875in"} icon to **Move Up** or click on the **down** ![](media/image188.png){width="0.23958333333333334in" height="0.23958333333333334in"} icon to **Move Down**.

### 6.12.5 Removing a form group

-   Select **Menu** \> **Forms**. Click on the **Form Groups** tab \> click on the **delete** ![https://lh3.googleusercontent.com/v8XgJTkOt4eSwXEfV8CX-5lKCHON6B1D97JMVxDEbD4Jc67e-RBNlB1BhWfeEruQbdmLhaiMD3jJlvF7ZX3ablDBpeBppMmZfOtoio7fhDUCulkBewsHqm6mYAG8kA](media/image189.png){width="0.23958333333333334in" height="0.2604166666666667in"} icon at the right-hand side of the form group name (e.g. Early Warning), and the group is removed. Click on **Save Change(s)**.

### 6.12.6 Removing forms from a form group

-   Select **Menu** \> **Forms**. Click on the **Form Groups** tab \> click on the **delete** ![https://lh3.googleusercontent.com/v8XgJTkOt4eSwXEfV8CX-5lKCHON6B1D97JMVxDEbD4Jc67e-RBNlB1BhWfeEruQbdmLhaiMD3jJlvF7ZX3ablDBpeBppMmZfOtoio7fhDUCulkBewsHqm6mYAG8kA](media/image189.png){width="0.23958333333333334in" height="0.2604166666666667in"} icon at the right-hand side of the form name (e.g. Weekly EWARS Reporting Form under the **Early Warning** group), and the form is removed. Click on **Save Change(s)**.

After creating forms and setting up indicators, you can proceed to configure alarms. The following chapter gives an overview of how to set up alarms based on different criteria.

# Chapter 7. Alarms

[Alarms are one of the key features of]{.mark} Early Warning, Alert and Response System ([EWARS]{.mark})[, as they help to raise early awareness of potential outbreaks, thereby facilitating prompt action from stakeholders. By leveraging the alarms function, users can set predefined criteria to detect unusual trends. When these trends are detected, the system can alert other users and initiate necessary actions to achieve resolution. This chapter will help users create, configure, edit and turn off alarms, as appropriate. Stakeholders are thus empowered to take swift action, saving lives in the process.]{.mark}

## 7.1 Alarms and their uses

Fig. 7.1. shows how alerts are triggered, based on criteria set in alarms.

Fig. 7.1. How alarms work

![](media/image190.png){width="4.5472222222222225in" height="5.053472222222222in"}

Alarms are set based on the criteria users allocate to each disease or event, based on the prevailing conditions. To put this in perspective, one case of suspected viral haemorrhagic fever (VHF) or a doubling of acute watery diarrhoea (AWD) cases in a primary health-care centre (PHCC), should sound an alarm in the system.

The alarm can be attached to any disease, condition or event. The alert threshold is the level at which point the alarm bell should be ringing, alerting everyone responsible. There is no real alarm bell, and no audible ringing as such, but the bell sign is used to indicate "alarm" in the system. For example, a suspected case of acute flaccid paralysis (AFP) should ring an alarm. Rumours of clusters of deaths should also ring an alarm.

How to manage raised alerts is dealt with in **Chapter 13. Alert log**. Alert thresholds are generally standardized -- especially for immediately notifiable diseases. Refer to national, regional or global surveillance guidance for more information on setting alert thresholds.

EWARS provides some sample alarms in the Model account, which you can copy and then make required changes. Alternatively, you can set new alarms relevant to [your country]{.mark}.

## 7.2 Copying sample alarms

You can copy the sample alarms in the Model account and make changes according to your country's requirements.

-   Select **Menu** \> **Configuration Transfer**. Select **Model account** from the **Source Account** drop-down menu. The system lists all transferable items. Search and select the sample alarms(e.g. Measles)*.* Click on the **transfer** ![](media/image191.png){width="0.34375in" height="0.3125in"} icon, and the chosen alarms are copied to your account.

## 7.3 Creating and configuring an alarm

You can set up new alarms from scratch according to [your country's epidemiological profile]{.mark}. First, identify which priority diseases/conditions/events you need to set an alarm for. Next, define a threshold: this is the level at which the system will inform epidemiologists and surveillance officers that a potential threat has been detected. This threshold can be a report of a single case, an event or a worrying trend, based on an analysis of data over a period.

### 7.3.1 Creating an alarm

You can set an alarm based on submission of a report (**record-based alarm**) or on a departure from the trend (**aggregate-based alarm**). Fig. 7.2 shows the flowcharts for these two methods.

Fig. 7.2. Ways to set an alarm

![](media/image192.png){width="5.917191601049868in" height="5.226851487314086in"}

  ---------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![](media/image43.png){width="0.65625in" height="0.3541666666666667in"}   Go through the reporting forms in EWARS and decide which diseases, events or conditions you need to set up alarms for. Then, refer to surveillance and early warning guidance documents to identify the standard alert thresholds for each disease, condition or event. An "alert" is the first hint of a larger public health problem. Once an alarm is set for a particular disease or condition, all individuals in the reporting pathway are informed of the potential threat.

  ---------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-   Select **Menu** \> **Alarms**. Click on ![](media/image193.png){width="0.7395833333333334in" height="0.3541666666666667in"}, and the screen below appears:

![](media/image194.png){width="5.0in" height="2.5833333333333335in"}

-   Populate the details in the **General** tab as set out below.

```{=html}
<!-- -->
```
-   **Name** \[Mandatory\]: enter the name of the alarm. It is usual to add the name of the disease or the condition to the alarm (e.g. Malaria or VHF).

-   **Status** \[Mandatory\]: set status as active.

    **Active** alarms can trigger alerts.

    **Inactive** alarms cannot trigger alerts.

-   **Description**: enter a description of the alarm (e.g. "Raise an alert when a Reporting User reports more than 10 malaria cases"). Ideally, include the alert threshold in the description.

-   **Alert electronic identification (EID) Prefix**: set an alert EID prefix. The prefix is concatenated with the alert EID; this helps to create a unique identification for an alert. For example, if the prefix is set as SARS, the alert EID is SARS-0A-354C-5230-3462.

-   **Tags**: enter tags for the alarm. A tag is an identifier that will help you find your alarm in the Configuration Transfer. You can add one or more tags.

```{=html}
<!-- -->
```
-   Click on **Save Change(s)**, and an alarm is created.

### 7.3.2 Configuring an alarm as a record-based alarm

For record-based alarms, the data source is a single report. In brief, every report will trigger an alarm in the system. This is vital for event-based surveillance or surveillance reporting from the community on clusters of cases and deaths or unknown diseases.

The following example shows how to raise an alert when a Reporting User reports an event using an event-based form.

-   Select **Menu** \> **Alarms**. Click on the **edit** ![](media/image195.png){width="0.25in" height="0.25in"} icon of alarm (e.g. Measles) \> click on the **Monitoring** tab \> click on **Record-based**.

-   Set **Monitored By** as **Indicator** \> select **System** \> **Form submissions** from the **Source Indicator** drop-down menu \> select **Event-Based Surveillance Form** from the **Form** drop-down menu \> select **Submitted** from the **Dimension** drop-down menu \> keep **Source** as **No selection**.

![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"} **Note:** if you don't specify the source (i.e. no selection), it will include reports submitted from EWARS Web as well as EWARS Mobile.

![](media/image196.png){width="5.0in" height="3.6875in"}

-   Select the **Comparator** (e.g. \>=) \> enter the threshold **Value** (e.g. 1).

-   Click on **Save Change(s)**, and the alarm is configured.

### 7.3.3 Configuring an alarm as an aggregate-based alarm

For aggregate-based alarms, the data are sourced from multiple reports. Data submitted during a specific period are used to evaluate the alarms. This is vital to acquire information about whether a particular disease or condition is on the rise at greater than expected levels for the location and season. Similarly, it is needed to detect diseases whose presence (even one suspected case) is important and needs notification (e.g. cases of VHF, AFP and similar).

The following steps show how to set up aggregate-based alarms using the various source specifications.

-   Select **Menu** \> **Alarms**. Click on the **edit** ![](media/image195.png){width="0.25in" height="0.25in"} icon of the relevant alarm (e.g. Malaria) \> click on the **Monitoring** tab \> click on **Aggregate-based**, and the screen below appears:

![](media/image197.png){width="5.78125in" height="2.15625in"}

#### 7.3.3.1 Specifying the monitoring location or groups

-   **Either** set **Monitor For** as **Location** if an alarm is to monitor a particular geographical location \> select the geographical locations you want to monitor from the drop-down menu (e.g. country, province or district)

-   **Or** set **Monitor For** as **Location Group(s)** if an alarm is to monitor a group of locations (e.g. a group of PHCCs managed by a nongovernmental organization (NGO) such as Médecins Sans Frontières or the International Committee of the Red Cross).

#### 7.3.3.2 Specifying the location type

-   Select the **location type** for which you want to set the alarm. The alarm is set for the entire location type selected, as follows:

```{=html}
<!-- -->
```
-   for country-level alarms, set location type to **Country**

-   for province-level alarms, set location type to **Province**

-   for health facility-level alarms, set location type to **Health Facility**.

#### 7.3.3.3 Restricting the data source

-   **Either** set **Restrict data source** to **No**, and all reports submitted are considered for alarm evaluation

-   **Or** set **Restrict data source** to **Yes**, and only the reports of the selected **location type** are considered for alarm evaluation. You can select the location type in the **Data reported on location type** field.

```{=html}
<!-- -->
```
-   For example, if location type is set as health facility, only those reports with reporting location type health facility are considered for alarm evaluation.

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** when you set an alarm for location type, the alarm is evaluated based on specification of the location type (e.g. a mobile clinic, laboratory or health post). In this situation, an alarm will be triggered for each location type, whereas if you set the source of data by location type, you indicate what data sources should be considered for triggering alarms; for example, select PHCC if you want to use data reported from PHCCs to trigger the alarm, or select mobile clinics if you want to aggregate data reported from mobile clinics for this alarm.
  --------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#### 7.3.3.4 Configuring the data source interval

The data source interval can be set as a fixed **Interval** (daily, weekly, monthly or yearly). The example below shows the data source interval set as the current calendar week:

> ![](media/image198.png){width="3.5625in" height="0.84375in"}

The data source interval can also be set as a specified **Range of Intervals** (biweekly, quarterly, every three months and so on). If set as a range, you also need to provide a figure for the number of intervals. The example below shows the data source interval set as three-monthly:

> ![](media/image199.png){width="3.5520833333333335in" height="1.2083333333333333in"}

![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"} **Note:** the three-month interval includes the current calendar month and the previous two months.

The example below shows the data source interval set as every 10 days:

> ![](media/image200.png){width="3.5833333333333335in" height="1.34375in"}

#### 7.3.3.5 Configuring the data aggregation

-   **Either** set **Aggregation** as **Sum**, and data from all the reports for the specified interval are aggregated as a sum

-   **Or** set **Aggregation** as **Average**, and data from all the reports for the specified interval are aggregated as a sum and then divided by the number of submitted reports in the specified interval, creating an average per report.

#### 7.3.3.6 Configuring the monitored by field

The form field monitored by has three options: **Indicator**, **Complex** and **SD/Mean/Percentile**. These are set out below with their sub-options.

If **Monitored** by is set as **Indicator**, this sets a threshold for a single indicator.

-   Set **Monitored by** as **Indicator** \> select the **Source Indicator** from the drop-down menu.

If **Monitored** by is set as **Complex**, this sets a threshold for a complex indicator.

-   Set **Monitored by** as **Complex**, and you can consider more than one indicator and formula -- for example the COVID-19 test positivity rate = (number of cases/number of tests) × 100.

If **Monitored** by is set as **SD/Mean/Percentile**, the standard deviation (SD), Mean average and Percentile of historical data for a given date range or specified weeks are automatically calculated. For this option to work, you have to input historical data into the system. It will not work without existing data to refer to.

-   Set **Monitored by** to **SD/Mean/Percentile** \> select the **Source Indicator** from the drop-down menu. The **Interval** is pre-set as **Week**: this can't be changed. Select a **Pre-Configured Formula** or enter a **Formula** manually.

```{=html}
<!-- -->
```
-   For example, to establish whether the **Indicator** value is Higher than 1SD, select the **Pre-Configured Formula** for **Higher than 1SD**, \[IDV -- (MEAN + SD)\] from the drop-down menu.

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** when you want to develop your own formulas, use the following abbreviations to indicate commonly use statistical terms: SD for standard deviation, MEAN for mean, IDV for indicator value (i.e. the value you want to compare against data), and PERCENTILE for percentile. Always add absolute values (positive values), the use of the abs () function is allowed in the formula.
  --------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-   **Either** set **Exclude zero value** to **Yes**, and any zero value intervals within the specified interval are ignored in the calculation of SD, Mean and Percentile

-   **Or** set **Exclude zero value** to **No**, and no intervals are ignored in the calculation.

#### 7.3.3.7 Configuring seasonal variation

-   **Either** set **Seasonal Variation** to **No** and provide a **Date Range** -- historical data from the date range specified are considered in the calculation of SD, Mean and Percentile

-   **Or** set **Seasonal Variation** to **Yes** and populate the **No. of +/- Weeks** and **No. of previous years** fields. Historical data from the weeks and years specified are considered in the calculation of SD, Mean and Percentile. If you set **Seasonal Variation** as **Yes**, the system calculates the average of the previous years. For example, if the number of previous years is set as 3 and the current year is 2021, the system considers the averages of June 2020, June 2019 and June 2018.

#### 7.3.3.8 Specifying the criteria for triggering alerts

-   Select the **Comparator** (e.g. \>) and enter a value to be compared (e.g. 0), as show below:

> ![](media/image201.png){width="4.84375in" height="1.5in"}

-   Click on **Save Change(s)**.

#### 7.3.3.9 Examples of aggregate-based alarms

For demonstration purposes, this guide uses the following six examples.

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Example 1.** Raise an alert when there are more than five malaria cases in a month.                                                                                                                                                                  |
|                                                                                                                                                                                                                                                        |
| -   Select **Menu** \> **Alarms**. Click on the **edit** ![](media/image195.png){width="0.25in" height="0.25in"} icon of the relevant alarm (Malaria) \> click on the **Monitoring** tab \> click on **Aggregate-based**.                     |
|                                                                                                                                                                                                                                                        |
| -   Set **Monitor For** as **Location** \> select the country name in the **Location** drop-down menu \> select a reporting location from the **Set alarm for location type** drop-down menu (e.g. Country) \> set **Restrict data source** as **No**. |
|                                                                                                                                                                                                                                                        |
| -   Set **Monitored By** as **Indicator** \> set **Data Source Interval** as **Interval** \> set **Data Source Interval** as **Month** \> set **Aggregation** as **Sum** \> select the **Source Indicator** **Malaria Total Cases**.                   |
|                                                                                                                                                                                                                                                        |
| -   Select the **Comparator** as \>= \> enter the threshold **value** "5").                                                                                                                                                                            |
|                                                                                                                                                                                                                                                        |
| -   Click on **Save Change(s)**, and the alarm is configured.                                                                                                                                                                                          |
+========================================================================================================================================================================================================================================================+
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Example 2.** Set an alarm to trigger an alert on malaria total cases.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| -   Select **Menu** \> **Alarms**. Click on the **edit** ![](media/image195.png){width="0.25in" height="0.25in"} icon of the relevant alarm (Malaria) \> click on the **Monitoring** tab \> click on **Aggregate-based**.                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| -   Set **Monitor For** as **Location** \> select the country name in the **Location** drop-down menu \> select a reporting location from the **Set alarm for location type** drop-down menu (e.g. Country) \> set **Restrict data source** as **No**.                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| -   Set **Monitored By** as **Complex** \> set **Data Source Interval** as **Interval** \> set **Data Source Interval** as **Month** \> set **Aggregation** as **Sum**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| -   Add two variables: one for under 5 cases and another for over 5 cases \> click on **Add** **Variable** \> click on the **edit** ![](media/image195.png){width="0.25in" height="0.25in"} icon \> enter the **Variable Name** "under_5" \> select **Malaria under 5 cases** from the **Indicator** drop-down menu \> click on **Add Variable** \> click on the **edit** ![](media/image195.png){width="0.25in" height="0.25in"} icon \> enter the **Variable Name** "over_5" \> select **Malaria over 5 cases** from the **Indicator** drop-down menu \> enter a **Formula** using the **Variable** **Names** (e.g. "Under_5 + Over_5") in the **Formula** field. |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|   -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                                                                                                                                                                                                                                                                                                                                                                                           |
|   ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** the system sets **Comparator** as \> and **Value** as 0 automatically. Thus, if the formula returns a positive value, the alert is triggered.                                                                                                                                                                                                                                                                                                                                                                                                             |
|   --------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|   -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| -   Click on **Save Change(s)**, and the alarm is configured.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
+=======================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Example 3.** Trigger an alert when malaria total cases are higher than 110% of the average of the last three weeks.                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                          |
| -   Select **Menu** \> **Alarms**. Click on the **edit** ![](media/image195.png){width="0.25in" height="0.25in"} icon of the relevant alarm (Malaria) \> click on the **Monitoring** tab \> click on **Aggregate-based**.                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                          |
| -   Set **Monitor For** as **Location** \> select the country name in the **Location** drop-down menu \> select a reporting location from the **Set alarm for location type** drop-down menu (e.g. Country) \> set **Restrict data source** as **No**.                                                                                   |
|                                                                                                                                                                                                                                                                                                                                          |
| -   Set **Monitored By** as **SD/Mean/Percentile**, as shown below:                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                          |
| > ![](media/image202.png){width="5.833333333333333in" height="3.1875in"}                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                          |
| -   Select the **Source Indicator** **Malaria Total Cases** \> enter the **Formula** "IDV -- (1.10\*MEAN)". Set **Exclude zero value** and **Seasonal Variation** as **No**. In the **Date Range** field, select **This week** from the **Quick Ranges**: **From** is set as **This week start** and **To** is set as **This week end**. |
|                                                                                                                                                                                                                                                                                                                                          |
| -   Enter "-3W" in the **Offset** field of the **From** field date picker, and **From** is updated to **This week start - 3 week(s)** \> enter "-3W" in the **Offset** field of the **To** field date picker, and **To** is updated to **This week end - 3 week(s)**.                                                                    |
|                                                                                                                                                                                                                                                                                                                                          |
|   -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                                              |
|   ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** the system sets **Comparator** as \> **and Value** as 0 automatically. Thus, if the formula returns a positive value, the alert is triggered.                                                                |
|   --------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------                                                              |
|                                                                                                                                                                                                                                                                                                                                          |
|   -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                                              |
|                                                                                                                                                                                                                                                                                                                                          |
| -   Click on **Save Change(s)**, and the alarm is configured.                                                                                                                                                                                                                                                                            |
+==========================================================================================================================================================================================================================================================================================================================================+
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Example 4.** Trigger an alert when the current week's count for under 5 years malaria cases is greater than the 110% of the mean value for the previous 52 weeks.                                                                                                         |
|                                                                                                                                                                                                                                                                             |
| -   Select **Menu** \> **Alarms**. Click on the **edit** ![](media/image195.png){width="0.25in" height="0.25in"} icon of the relevant alarm (Malaria) \> click on the **Monitoring** tab \> click on **Aggregate-based**.                                          |
|                                                                                                                                                                                                                                                                             |
| -   Set **Monitor For** as **Location** \> select the country name in the **Location** drop-down menu \> select a reporting location from the **Set alarm for location type** drop-down menu (e.g. Country) \> set **Restrict data source** as **No**.                      |
|                                                                                                                                                                                                                                                                             |
| -   Set **Monitored By** as **SD/Mean/Percentile**, as shown below:                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                             |
| > ![](media/image203.png){width="5.0in" height="2.4791666666666665in"}                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                             |
| -   Select the **Source Indicator** **Malaria under 5 cases** \> enter the **Formula** "IDV -- (1.10\*MEAN)". Set **Exclude zero value** and **Seasonal Variation** as **No**. In the **Date** **Range** field select **Previous 52 weeks** from **Quick Ranges**.          |
|                                                                                                                                                                                                                                                                             |
|   ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** the system sets the comparator as \> and the value as 0 automatically. Thus, if the formula returns a positive value, the alert is triggered.   |
|   --------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                                                                                                                                                                                                                                                             |
|   ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                                                                                                                                                                                                                                                             |
| -   Click on **Save Change(s)**, and the alarm is configured.                                                                                                                                                                                                               |
+=============================================================================================================================================================================================================================================================================+
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Example 5.** Trigger an alarm if current reporting is more than the 75th percentile for the last three years.                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                            |
| -   Select **Menu** \> **Alarms**. on the **edit** ![](media/image195.png){width="0.25in" height="0.25in"} icon of the relevant alarm (Malaria) \> click on the **Monitoring** tab \> click on **Aggregate-based**.                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                            |
| -   Set **Monitor For** as **Location** \> select the country name in the **Location** drop-down menu \> select a reporting location from the **Set alarm for location type** drop-down menu (e.g. Country) \> set **Restrict data source** as **No**.                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                            |
| -   Set **Monitored By** as **SD/Mean/Percentile**, as shown below:                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                            |
|     ![](media/image204.png){width="5.0in" height="3.09375in"}                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                            |
| -   Select the **Source Indicator** **Malaria Total Cases** \> enter the **Formula** "PERCENTILE - 75". Set **Exclude zero value** and **Seasonal Variation** as **No**. In the **Data Range** field, select **Today** from **Quick Ranges**, and **Today** is set as the **From** and **To** fields. Enter "-3Y" in the **Offset** field of the **From** field date picker, and **From** is set as **Today - 3 year(s)**. |
|                                                                                                                                                                                                                                                                                                                                                                                                                            |
|   -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                                                                                                                                |
|   ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** the system sets the comparator as \> and the value as 0 automatically. Thus, if the formula returns a positive value, the alert is triggered.                                                                                                                                                  |
|   --------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                            |
|   -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                            |
| -   Click on **Save Change(s)**, and the alarm is configured.                                                                                                                                                                                                                                                                                                                                                              |
+============================================================================================================================================================================================================================================================================================================================================================================================================================+
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Example 6:** Trigger an alert when the under 5 years count of malaria cases is greater than the corresponding moving average of three weeks for the last three years (\> mean + 2SD). This is for seasonality, to see whether the value is statistically different from the corresponding weeks of the last three years.                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                            |
| -   Select **Menu** \> **Alarms**. Click on the **edit** ![](media/image195.png){width="0.25in" height="0.25in"} icon of the relevant alarm (Malaria) \> click on the **Monitoring** tab \> click on **Aggregate-based**.                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                            |
| -   Set **Monitor For** as **Location** \> select country name in the **Location** drop-down menu \> select a reporting location from the **Set alarm for location type** drop-down menu (e.g. Country) \> set **Restrict data source** as **No**.                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                            |
| -   Set **Monitored By** as **SD/Mean/Percentile**.                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                            |
| -   Select the **Source Indicator** **Malaria Under 5 Cases** \> enter the **Formula** "IDV -- (MEAN + 2SD)". Set **Exclude zero value** as **No** \> set **Seasonal Variation** as **Yes**. Enter "1" in **No. of +/- Weeks** \> enter "3" in **No.** **of previous years**. The data considered for this are thus from the last three years, with week range (x+1), where x = week of report submission. |
|                                                                                                                                                                                                                                                                                                                                                                                                            |
|   -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                                                                                                                |
|   ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** the system sets the comparator as \> and the value as 0 automatically. Thus, if the formula returns a positive value, the alert is triggered.                                                                                                                                  |
|   --------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                            |
|   -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                            |
| -   Click on **Save Change(s)**, and the alarm is configured.                                                                                                                                                                                                                                                                                                                                              |
+============================================================================================================================================================================================================================================================================================================================================================================================================+
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

## 7.4 Enabling auto-discard of an alert

Once an alert is triggered, you are expected to conduct a verification rapidly. Therefore, you are not expected to discard alerts without verification. However, after a long lapse of time, the system allows you to auto-discard alerts. For example, if an alert is not verified after three months, you may set the conditions to discard it. When discarded it will not appear under open alerts, indicating that you need to take action.

By default, the auto-discard setting is off, but when enabled, the system automatically discards a specified alert after a defined period.

The following example shows you how to auto-discard an alert after two weeks.

-   Select **Menu** \> **Alarms** \> click on the **edit** ![](media/image195.png){width="0.25in" height="0.25in"} icon of the relevant alarm (e.g. Malaria) \> click on the ![](media/image205.png){width="1.0625in" height="0.375in"} tab, and the screen below appears:

![](media/image206.png){width="5.489584426946632in" height="2.875in"}

-   Click on the **toggle** ![](media/image207.png){width="0.38782589676290463in" height="0.27701771653543306in"} icon to enable it, and the icon colour changes to green.

-   Set **Auto-discard interval** to **Week(s)** \> set **No. of Intervals** to "2".

-   Click on **Save Change(s)**.

## 7.5 Running an evaluation of an alarm manually

An alarm evaluation is done by the system automatically whenever a new report is submitted, but the Account Administrator can also evaluate it manually.

-   Select **Menu** \> **Alarm**. Click on the **edit** ![](media/image208.png){width="0.2916666666666667in" height="0.3125in"} icon of the relevant alarm (e.g. Malaria) \> click on the ![](media/image209.png){width="1.0520833333333333in" height="0.375in"} tab, and the screen below appears:

![](media/image210.png){width="5.5625in" height="2.53125in"}

-   **Either** click on **Run evaluation** to evaluate the reports submitted within the last 10 days -- if the evaluation meets the alarm criteria, it triggers an alert and sends an email notification for the triggered alerts

-   **Or** click on **Run evaluation \[Silent\]**, which evaluates the reports submitted within the last 10 days but does not send any email notifications for the triggered alerts, if any.

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** silent action won't override email alert notification settings set in the profile.
  --------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 7.6 Editing an alarm

-   Select **Menu** \> **Alarm**. Click on the **edit** ![](media/image208.png){width="0.2916666666666667in" height="0.3125in"} icon of the relevant alarm (e.g. Malaria) \> make the desired changes. Click on **Save Change(s)**.

## 7.7 Turning off an alarm

-   Select **Menu** \> **Alarm**. Click on the **edit** ![](media/image208.png){width="0.2916666666666667in" height="0.3125in"} icon of the relevant alarm (e.g. Malaria) \> set **Status** as **Inactive**, and the alarm is inactivated. Click on **Save Change(s)**.

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** if you don't want an alarm, it is recommended that you make the alarm inactive.
  --------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 7.8 Deleting an alarm

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image211.png){width="0.41060695538057745in" height="0.3875in"}**WARNING:**   Deleting an alarm will also delete all the alerts and the alert data associated with it.
  --------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-   Select **Menu** \> **Alarm**. Click on the **delete** ![](media/image212.png){width="0.25in" height="0.23958333333333334in"} icon of the relevant alarm (e.g. Measles) \> click on **Confirm**, and the alarm with its associated alert/alert data is deleted.

The following chapter gives further information about the different user profiles in EWARS and how to add assignments for them.

# Chapter 8. Users and their assignments

This chapter provides an overview of user management, an integral part of Early Warning, Alert and Response System (EWARS). It will help you to understand the different hierarchies of user profiles in EWARS. Further, it will help you perform key actions with ease, such as setting up organizational profiles, creating/editing user accounts, adding assignments, and managing user access and passwords. Through this, you can manage different hierarchies of users effectively in close alignment with the overall goals of EWARS in any given setting.

## 8.1 Types of user profiles in EWARS

Only registered users can access EWARS. There are three types of user profiles in EWARS (Fig. 8.1).

Fig. 8.1. User profiles in EWARS

![](media/image213.png){width="5.165354330708661in" height="4.566929133858268in"}

-   **Reporting Users** are EWARS users who report data from primary health-care centres (PHCCs), field hospitals, health posts or the community. Reporting Users mostly use EWARS Mobile for reporting. In any context, there are more Reporting Users than other type. For example, if 200 PHCCs are registered under EWARS, there may be 200 or more Reporting Users.

-   **Geographical Administrators** manage the early warning, alert and response functions for a specific geographical area -- such as a province or district. If you have five provinces in your EWARS, there may be five Geographical Administrators, each overseeing the functions of one province.

-   **Account Administrators** are usually one or two individuals who oversee overall EWARS activities encompassing all provinces and districts.

For more information about different types of users, refer to **Chapter 1. Overview of EWARS in a box**, topic **1.4 Types of users**.

[EWARS users may belong to different organizations, ministries of health and agencies. Therefore, each user and organization should be registered in EWARS to access and report to it successfully. Registration provides a unique username and password for each user to access EWARS.]{.mark}

[The following sections illustrate the key actions under user management.]{.mark}

## 8.2 Setting up user organizations

Before setting up individual EWARS user profiles, set up organizational profiles for the users in the system. Several agencies and organizations may be involved in managing EWARS in your context. For example, all Reporting Users may belong to the ministry of health or the United Nations Children's Fund, while all administrative users (Account Administrators and Geographical Administrators) may represent the ministry of health and WHO.

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** an organization is mandatory for user setup, so it should be added to the system before adding users.
  --------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can follow the steps below to set up organizations.

-   Click on the **settings** ![](media/image214.png){width="0.25in" height="0.275in"} icon \> click on ![](media/image215.png){width="1.05in" height="0.3333333333333333in"} \> click on ![](media/image216.png){width="0.9416666666666667in" height="0.35833333333333334in"}, and the screen below appears:

![](media/image217.png){width="6.468297244094488in" height="2.4795133420822397in"}

-   Enter the **Organization** **Name** (e.g. Women's Refugee Commission) \> enter the **Acronym** for the organization (e.g. WRC) \> enter the **Web Site** link \> set **Status** as **Active**.

-   Click on **Save Change(s)**.

-   Repeat the steps above to add other organizations.

Added organizations are visible, as in the screenshot below:

![](media/image218.png){width="5.78333552055993in" height="1.7416666666666667in"}

-   To **edit** an existing organization, click on the **edit** ![](media/image219.png){width="0.325in" height="0.275in"} icon \> make the required changes. Click on **Save Change(s)**, and a notification appears that the organization is edited.

-   To **delete** an existing organization, click on the **delete** ![](media/image220.png){width="0.2916666666666667in" height="0.3in"} icon \> click on **Confirm**, and a notification appears that it is deleted.

## 8.3 Creating users

Electronic reporting using EWARS Mobile is the most important step in EWARS. During emergencies, it is paramount to register all health facilities, health posts and community members who want to report to the system rapidly.

There are two methods of registering or creating users in the system.

-   You can create users manually -- each Reporting User is created by entering their data manually in the system:

    -   **Either** they are registered via an invitation to join the system

    -   **Or** they are registered via system-generated emails.

-   You can import Reporting User data in bulk -- you can add data for a large number of Reporting Users as a single comma-separated values (CSV) file.

To find more about different types of users and their general responsibilities, refer to **Chapter 1. Overview of EWARS in a box**, topic **1.4 Types of users**.

### 8.3.1 Creating users manually -- via invitation

  ---------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![](media/image43.png){width="0.65625in" height="0.3541666666666667in"}   This method is best reserved for registering/creating Account Administrators and Geographical Administrators. As they represent a small number of users, sending invitations is not a difficult process. Please note that this method will only work if the person invited to register in the system has a valid email address that they can access easily during an emergency.

  ---------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** the Account Administrator decides the role of any users created manually.
  --------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-   Select **Menu** \> **Users** \> **Create User**. Click on the **Send Invitation** tab, and the screen below appears:

![](media/image221.png){width="5.760416666666667in" height="3.15625in"}

-   Enter the **Email** address of the user (e.g. johnsmith@gmail.com) \> select the **Role** for the new user (e.g. Geographical Administrator) \> set **Status** as **Active** \> select the **Location** to be assigned to the new user (e.g. Aimal Province).

-   Click on **Send Invite**. An invitation email is sent to the user. If a user has not received an invitation email, ask them to check their Spam folder.

You can repeat the steps above to create more users via invitation.

An EWARS invitation looks like this:

![](media/image222.png){width="5.0in" height="2.71875in"}

Once the user clicks on the link, the EWARS Invitation screen below appears:

![](media/image223.png){width="5.893458005249344in" height="3.6023064304461943in"}

-   The user needs to enter the following details:

```{=html}
<!-- -->
```
-   **Name** (e.g. John Smith)

-   **Email** (e.g. johnsmith@gmail.com)

-   **Confirm Email** (e.g. johnsmith@gmail.com)

-   **Password** (e.g. mv6u741) (Users can customize the password as there are no set rules for it.)

-   **Confirm Password** (e.g. mv6u741)

-   **Organization** (e.g. Ministry of Health)

```{=html}
<!-- -->
```
-   The user should then click on **Complete Registration**, and an account is created**.**

  ---------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![](media/image43.png){width="0.65625in" height="0.3541666666666667in"}   The email and password used for registration are used to access the system each time you want to log in. Alert notifications are also sent to the email address specified, if you enable receiving notifications.

  ---------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### 8.3.2 Creating users manually -- via system-generated login details

If a user who wishes to have access to EWARS does not have an email address, he/she can proceed as follows.

The system can generate login details, email addresses and passwords for users without using their own valid email addresses. As these emails addresses are not valid, they can only be used to log in to EWARS. Users created in this way are called "custom users". All system-generated email addresses follow a uniform pattern, and all end with "@ewars.ws".

  ---------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![](media/image43.png){width="0.65625in" height="0.3541666666666667in"}   Use this method when you want to generate login details for Reporting Users, who are reporting from PHCCs, health posts and the community. They may not have access to desktops or laptops and may not have valid email addresses -- especially during an emergency.

  ---------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Follow the steps below to create users using system-generated login details.

-   Select **Menu** \> **Administration** \> **Users** \> **Create User**. Click on the **Custom User** tab, and the screen below appears:

![](media/image224.png){width="5.775in" height="3.15in"}

-   Populate the details of the user as set out below.

```{=html}
<!-- -->
```
-   **Email** \[Mandatory\]: enter the name/prefix for the email. The domain will automatically be added as \@ewars.ws. For example, enter "johndavis" and the email address will be johndavis@ewars.ws. It should be a unique ID or a warning is triggered by the system.

    In most instances, the system-generated login details will not be under an individual's name, but under a reporting site (e.g. a health facility first name, such as Aimal or Bilnula). In these cases, the system-generated email address would be [[aimal@ewars.ws]{.underline}](mailto:aimal@ewars.ws) or [[bilnula@ewars.ws]{.underline}](mailto:bilnula@ewars.ws). Any clinician, nurse or reporting officer can report data under the health facility using these login details. You will, however, lose the resolution of knowing which data were sent by which individual.

-   **Name** \[Mandatory\]: enter the name of the user (e.g. John Davis or Birigo health post).

-   **Password** \[Mandatory\]: enter a password that must be at least six characters long and must contain one number or non-standard character (e.g. "john66@d").

-   **Confirm password** \[Mandatory\]: re-enter the password for confirmation.

-   **Organization** \[Mandatory\]: select the organization of the custom user (e.g. International Rescue Committee).

-   **Phone:** enter the phone number of the user.

-   **Occupation:** enter an occupation of the user.

-   **Role** \[Mandatory\]: select the role of the user (e.g. Reporting User).

-   **Status** \[Mandatory\]: set status as active.

```{=html}
<!-- -->
```
-   Click on **Add user**, and the user is created.

Repeat the steps above to create more users via system-generated login details.

### 8.3.3 Creating users in bulk

You can register a large number of EWARS users at once by uploading user details as a CSV file. This saves time during emergencies.

  ---------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![](media/image43.png){width="0.65625in" height="0.3541666666666667in"}   Use this method when you are creating a large number of Reporting Users. It would be best to have all the necessary details ready in a CSV file before importing the data. Download the Template from the system, as shown below to create your CSV file.

  ---------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Follow the steps below to create users in bulk.

**Step 1.** Select **Menu** \> **Administration** \> **Users**. Click on **Import Users**, and the screen below appears:

![](media/image225.png){width="5.98333552055993in" height="2.066666666666667in"}

**Step 2.** Click on **Download** **Template CSV** and open it in Excel:

![](media/image226.png){width="5.03333552055993in" height="1.4583333333333333in"}

**Step 3.** Populate the CSV file columns, as shown below:

-   **Name** \[Mandatory\]: enter the name of the user (e.g. User A).

-   **Role** \[Mandatory\]: enter the role for the new user (e.g. Reporting User).

-   **Email** \[Mandatory\]: enter the email address of the user (e.g. usera@gmail.com). If you want to create a user with a system-generated email address, use the user id with \@ewars.ws (e.g. "userx@ewars.ws").

-   **Password** \[Mandatory\]: enter a password for the user (e.g. "mb@7fg1").

-   **Organization.en** \[Mandatory\]: enter the organization name in English. If you want to add a name in French, change the column name from Organization.en to Organization.fr. Here, "en" and "fr" denote the standard language codes. For more information about codes for other languages, click on the **settings** ![](media/image35.png){width="0.35833333333333334in" height="0.375in"} icon \> [click on]{.mark} ![](media/image53.png){width="0.8666666666666667in" height="0.2833333333333333in"}[.]{.mark}

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** the organization must exist in the system, or the import will be unsuccessful.
  --------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-   **Occupation**: enter the occupation of the user.

-   **Phone**: enter the phone number of the user.

-   **Status**: keep the status column blank. By default, the status is set as ACTIVE. If you want to create a user with inactive status, add "INACTIVE" to the status column:

![](media/image227.png){width="6.177083333333333in" height="1.4784962817147858in"}

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** please be [mindful of the typographic use of uppercase and lowercase letters, and correct spellings of the organizations, as these will affect the import process]{.mark}.
  --------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Step 4.** Click on ![](media/image228.png){width="0.675in" height="0.275in"} \> browse and select the prepared CSV file. **Status_of_imported_records.csv** file is downloaded.

**Step 5.** Analyse the **Status_of_imported_records.csv** file as below:

![](media/image229.png){width="6.895606955380577in" height="1.8256506999125108in"}

The downloaded file is the same as the uploaded file with two additional columns: **import_status** and **import_description**.

The import_status column shows the success or failure of the imported records, with reasons for any failures indicated in the import_description column.

As shown in the above screenshot, three users have been successfully imported and two users have failed to import. For "user a", the import description states "USER_EXISTS_IS_ACTIVE", which means that "user a" with the specified email address already exists in the system.

Similarly, for "user d", the import description states "organization: NGO C does not exist or is empty", which means the provided organization is not available in the system. You therefore need to create the organization ("NGO C" in this example) first and then import "user d".

To reimport users that could not be imported during the first attempt, make the appropriate corrections to the failed user details according to the instructions in the import_description column, and import it again.

**Step 6.** After creating all users, select **Menu** \> **Users**, and the imported users appear, as shown below:

![](media/image230.png){width="6.413792650918635in" height="3.1217432195975503in"}

## 8.4 Editing users

In EWARS, you can edit the login information of users with system-generated email addresses, but you cannot edit user details with valid personal email addresses: that is the responsibility of the users themselves.

You can edit user details individually or in bulk.

### 8.4.1 Editing user details individually

-   Select **Menu** \> **Users**. Click on the **edit** ![](media/image231.png){width="0.2916666666666667in" height="0.2833333333333333in"} icon \> make the desired changes. Click on **Save Change(s)**.

### 8.4.2 Editing user details in bulk

This function allows you to edit details including name, role, password, organization, occupation, phone and status, but not email address. The email address is the user identifier and is a mandatory column.

  ---------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![](media/image43.png){width="0.65625in" height="0.3541666666666667in"}   Some reporting sites may change ownership, name or phone numbers as time passes. A process to edit user details in the system without disrupting their access is therefore essential.

  ---------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Follow the steps below to edit user details in bulk.

**Step 1.** Select **Menu** \> **Administration** \> **Users** \> **Import Users**. Click on **Download Template CSV** and open it in Excel:

![](media/image226.png){width="5.03333552055993in" height="1.4583333333333333in"}

**Step 2.** Populate the details in the CSV file, including the user email addresses, as shown below:

![](media/image232.png){width="4.95in" height="1.4166666666666667in"}

The system will match provided email addresses with existing users' email addresses. If the email address matches, the user details are updated with the details provided in the relevant columns in the file.

**Step 3.** Click on ![](media/image233.png){width="1.2583333333333333in" height="0.275in"} \> click on ![](media/image234.png){width="0.65in" height="0.25in"} \> browse and select the prepared CSV file. The **Status_of_imported_records.csv** file is downloaded.

**Step 4.** Analyse the **Status_of_imported_records.csv** file as below:

![](media/image235.png){width="5.29166447944007in" height="1.3166666666666667in"}

The downloaded file is the same as the uploaded file with two additional columns: **import_status** and **import_description**.

The import_status column shows the success or failure of the imported records, with reasons for any failures indicated in the import_description column.

If some of the user details are not updated successfully, make the appropriate corrections to the failed user details in the CSV file according to the instructions in the import_description column, and import it again.

## 8.5 User assignments

Assignments refer to the reporting forms each location is responsible for reporting to EWARS. One location can have multiple assignments.

For example, Dondo PHCC has two assignments:

-   submit a weekly reporting form every Monday morning for the previous completed epi week

-   submit an immediate notification form every time an immediately notifiable disease is seen at the PHCC.

If an outbreak is ongoing, they may also have outbreak line lists as assignments.

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** Geographical Administrators and Account Administrators do not have assignments under them.
  --------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In EWARS, Reporting Users are not directly associated with locations. Instead, once you assign a form to a user, the location is associated with the user indirectly. When you report the form, the list of associated locations appears for selection.

There are three methods to add assignments to users.

-   You can add assignments to Reporting Users manually.

-   You can add assignments in bulk via a CSV file.

-   You can add assignments to existing users with other assignments.

### 8.5.1 Adding assignments to Reporting Users manually

-   [Select **Menu **]{.mark}\> **[Users]{.mark}**. []{.mark}Click on the **folder** ![](media/image236.png){width="0.3in" height="0.275in"} icon of the Reporting User (e.g. user d).

![](media/image237.png){width="4.975in" height="1.4583333333333333in"}

-   Click on **Add New Assignment**, and the screen below appears:

![](media/image238.png){width="5.975in" height="1.6083333333333334in"}

-   Select the **Form**.

-   Select the **Location** of the **Assignment** from the drop-down menu.

```{=html}
<!-- -->
```
-   **Specific location**: this indicates that the user must report from the location provided in the next drop-down menu (e.g. Bilnula PHCC).

-   **Location group** this indicates that the user is limited to reporting from any of the locations in the location group provided in the next drop-down menu.

-   **Reporting locations within:** this indicates that the user must report from any of the locations under the location provided in the next drop-down menu. Thus, if a province is selected, the user can report from any of the health facilities situated within that province (at any geographical level). In this instance, every time the Reporting User logs in to EWARS Mobile to report under this form, he or she is presented with a list of reporting locations within the administrative boundary chosen. The Reporting User can select anyone to report at a given time. This enables one Reporting User with a mobile phone or web access to report for multiple sites, as those sites may not have the required equipment or facilities.

```{=html}
<!-- -->
```
-   Set **Status** as **Active**. If the status is set as **Inactive**, reporting cannot be done.

-   Click on the **save** ![](media/image239.png){width="0.21666666666666667in" height="0.23333333333333334in"} icon, and the assignment is added.

You can repeat the steps above to add more such assignments.

#### 8.5.1.1 Editing or deleting an assignment

  ---------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![](media/image43.png){width="0.65625in" height="0.3541666666666667in"}   You can modify assignments to suit your needs. If an outbreak is declared, you can add line list assignments to Reporting Users, and you can remove such assignments when the outbreak is over.

  ---------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To edit an assignment, follow the steps below.

-   [Select **Menu **]{.mark}\> **[Users]{.mark}**. []{.mark}Click on the **folder** ![](media/image236.png){width="0.3in" height="0.275in"} icon of the Reporting User (e.g. user d). Click on the **edit** ![](media/image240.png){width="0.2916666666666667in" height="0.275in"} icon of the **Assignment**, and the row opens in edit mode. Make the desired changes \> click on the **save** ![](media/image239.png){width="0.21666666666666667in" height="0.23333333333333334in"} icon, and the changes are updated.

To delete an assignment, follow the steps below.

-   [Select **Menu **]{.mark}\> **[Users]{.mark}**. []{.mark}Click on the **folder** ![](media/image236.png){width="0.3in" height="0.275in"} icon of the Reporting User (e.g. user d). Click on the **delete** ![](media/image241.png){width="0.2916666666666667in" height="0.2916666666666667in"} icon of the **Assignment** \> click on **Confirm**, and the **Assignment** is deleted.

### 8.5.2 Adding assignments in bulk via a CSV file

  ---------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![](media/image43.png){width="0.65625in" height="0.3541666666666667in"}   When you have a large number of reporting sites and users, it can be time-consuming to add assignments one by one. Have a CSV file ready with user details to import to the system for efficiency. Use the CSV template to create your CSV file for import.

  ---------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can add assignments in bulk by uploading a CSV file populated with assignment details. Each row in the file indicates one assignment -- i.e. a reporting form assigned to a user at a location.

Follow the steps below to import assignments in bulk.

**Step 1.** Select **Menu** \> **Users** \> **Bulk Assignment**, and the screen below appears:

![](media/image242.png){width="5.841666666666667in" height="2.1333333333333333in"}

**Step 2.** [Click on **Download** **Template CSV** and open it in Excel:]{.mark}

![](media/image243.png){width="5.466666666666667in" height="1.2166666666666666in"}

**Step 3.** [Populate the CSV file columns as shown below:]{.mark}

![](media/image244.png){width="5.966666666666667in" height="1.6583333333333334in"}

-   **user_email** [\[Mandatory\]: enter the email address of the user]{.mark} to whom you want to assign the form. For an **Assignment** to be added successfully, the user's status must be **Active**, and the email address entered must match the user's email address.

-   **form_name.en** \[[Mandatory]{.mark}\]: enter the form name in English. If you want to add a name in French, change the column name from "form_name.en" to "form_name.fr".

![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"} **Note:** for an assignment to be added successfully, the form status needs to be **Active**, and it must be enabled for **Location-Based Reporting**.

-   **location_type** [\[Mandatory\]:]{.mark} enter the location type as "SPECIFIC" or "LOCATION_WITHIN" OR "GROUP".

> **SPECIFIC:** the form is assigned to a specific location, which is provided in the **location_uuid** column. Enter the location universally unique identifier (UUID) in the **location_uuid** column.
>
> ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"} **Note:** to obtain the location UUID, select **Menu** \> **Locations**. Click on the **folder** ![](media/image45.png){width="0.25in" height="0.23958333333333334in"} icon to expand the location hierarchy \> click on the location name, and the location details including the UUID are at the right-hand side.
>
> **LOCATION_WITHIN:** the form is assigned to locations that exist under the location provided in the **location_uuid** column. [Enter the location UUID in the]{.mark} **location_uuid** column.
>
> **GROUP:** the form is assigned to the group provided in the **location_group** column. Enter the group name in the **location_group** column.

-   **Status**[: keep the status column blank. By default,]{.mark} the **Status** is set as ACTIVE. If you want the assignment to be INACTIVE, set the status column value as "INACTIVE".

**Step 4.** [Click on]{.mark} ![](media/image245.png){width="0.65in" height="0.275in"} []{.mark}\> [browse and select the prepared CSV file. The **Status_of_imported_records.csv** file is downloaded.]{.mark}

**Step 5.** Analyse the **Status_of_imported_records.csv** file as below:

![](media/image246.png){width="5.825in" height="1.125in"}

[The downloaded file is the same as the uploaded file with two additional columns: **import_status** and **import_description**.]{.mark}

The import_status column shows the success or failure of the imported records, with reasons for any failures indicated in the import_description column.

[If an assignment has failed to import successfully,]{.mark} make corrections to the un[successful]{.mark} rows of the CSV file, and import it again.

### 8.5.3 Adding assignments to existing users with other assignments

The replicate assignments feature is used in a scenario where a form "X" is assigned to users at one location, and a new form "Y" needs to be assigned to those users at the same location.

  ---------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![](media/image43.png){width="0.65625in" height="0.3541666666666667in"}   You may want to add a second or third (or fourth) assignment to a user who is already assigned with one report -- for example, all PHCCs in Aimal Province are assigned with a weekly EWARS reporting form, and you want to assign a second form to them (e.g. an immediate reporting form).

  ---------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To assign the new form "Y", follow the steps below.

-   Select **Menu** \> **Users** \> **Bulk Assignment** \> **Replicate Assignments**, and the screen below appears:

![](media/image247.png){width="5.931479658792651in" height="2.774263998250219in"}

-   Select the form that was previously assigned to the users from the **For users that currently have access to form** drop-down menu.

-   Select the new form that is to be assigned to all users of the previous form from the **Give access to form** drop-down menu. By default, **Role** is set as Reporting User.

-   Click on **Assign** \> click on **Confirm**, and the form is assigned.

## 8.6 Changing a user password

In EWARS, as an Account Administrator, you can change the passwords of users created with a system-generated email address, but you can't change passwords of users created with a valid personal email address.

  ---------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![](media/image43.png){width="0.65625in" height="0.3541666666666667in"}   Reporting sites, PHCCs, health posts and similar may have a high turnaround of staff/users, and the process of transferring EWARS login details between old and new users may therefore not be very smooth. This feature enables the Account Administrator to change passwords without any hassle.

  ---------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Follow the below steps to change a password for a user with a system-generated email address.

-   Select **Menu** \> **Administration** \> **Users.** Click on the ![](media/image248.png){width="0.23958333333333334in" height="0.20833333333333334in"} icon, and the **Update Password** screen below appears:

![](media/image249.png){width="5.85in" height="1.3833333333333333in"}

-   Enter the new password. Click on **Save Change(s)**, and the password is changed.

## 8.7 Revoking and reinstating user access

Revoking access means the user will not be able to use their account: their user status will be access revoked and they will not be able to log in into the system. User access can also be reinstated to make the user active again.

  ---------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![](media/image43.png){width="0.65625in" height="0.3541666666666667in"}   Some Geographical Administrators or Reporting Users leave the system when they exit the emergency response. As an Account Administrator, you can revoke or reinstate the access of any user.

  ---------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To revoke user access, follow the steps below:

-   Select **Menu** \> **Users**. Click on the ![](media/image250.png){width="0.2604166666666667in" height="0.20833333333333334in"} icon of the user (e.g. John Smith) \> click on **Confirm**, and access is revoked.

To reinstate user access after it has been revoked, follow the steps below:

-   Select **Menu** \> **Users**. Click on the ![](media/image250.png){width="0.2604166666666667in" height="0.20833333333333334in"} icon of the revoked user (e.g. John Smith) \> click on **Confirm**, and access is reinstated.

The following chapter will help you manage your profile, tasks and notifications.

# Chapter 9. User profiles, tasks and notifications

[This chapter will help you configure user profile details, view and act upon assigned tasks, manage notifications, and view activities based on time and date of occurrence. These essential actions will help you administer the varied responsibilities defined by your role effectively, in line with the aims of]{.mark} the Early Warning, Alert and Response System ([EWARS) in various settings.]{.mark}

## 9.1 Editing a user profile

  ---------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------
  ![](media/image43.png){width="0.65625in" height="0.3541666666666667in"}   An Account Administrator or a Geographical Administrator in EWARS can edit their profiles, tasks and notifications.

  ---------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------

-   Click on the **profile** ![](media/image251.png){width="0.23333333333333334in" height="0.24166666666666667in"} icon at the top right-hand corner, and the screen below appears:

![](media/image252.png){width="5.76666447944007in" height="3.091666666666667in"}

-   Edit the relevant fields (such as name, email, role, organization, phone, occupation and bio) \> click on the **save** ![](media/image253.png){width="0.2833333333333333in" height="0.21666666666666667in"} icon to save the changes or click on the **close** ![](media/image254.png){width="0.28125in" height="0.22916666666666666in"} icon to revert to the original text.

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** Geographical Administrators are able to see the location along with the fields shown above.
  --------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 9.2 Changing your password

If you want to change your password for security reasons, sign into the system and follow the steps below.

You can customize your password as there are no set rules for it.

-   Click on the **profile** ![](media/image251.png){width="0.23333333333333334in" height="0.24166666666666667in"} icon \> click on ![](media/image255.png){width="1.3854166666666667in" height="0.22916666666666666in"} at the top right-hand corner, and the screen below appears:

![](media/image256.png){width="5.675in" height="1.6166666666666667in"}

-   Enter a **New Password** \> re-enter the password in the **Confirm New Password** box \> click on **Submit**. The password is changed.

## 9.3 Changing the EWARS display to your preferred language

[EWARS provides multilanguage support. By default, the application is set as English. You can choose a different language from your profile and view the application]{.mark} according to [your preferences.]{.mark}

  ---------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![](media/image43.png){width="0.65625in" height="0.3541666666666667in"}   [EWARS]{.mark} helps you change the default language to your preferred language; you can thereby interact with the system in your selected language. For example, all notifications and tasks, and the entire interface can be viewed in the preferred language.

  ---------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Follow the steps below to change your preferred language.

-   Click on the **profile** ![](media/image251.png){width="0.23333333333333334in" height="0.24166666666666667in"} icon \> click on **Settings**. By default, this is English, as shown below:

![](media/image257.png){width="6.161185476815398in" height="1.8177088801399826in"}

-   Select **French** from the **Language** drop-down menu, and your EWARS display screen is visible in French, as shown below:

![](media/image258.png){width="6.1875in" height="1.8958333333333333in"}

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** if you do not see the desired language in the **Language** drop-down menu, the language needs to be added to the account. To find out more about adding languages, refer to **Chapter 10. EWARS account settings**, topic **10.6.4 Adding a new language to your** **account**.
  --------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 9.4 Enabling two-factor authentication for login

Two-factor authentication is a two-step security process. Users need to verify first by entering their credentials, and then by entering the security code sent to their email address to log into the account. This provides higher security and access control than a login based on email and password alone.

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** this feature is not available for users whose accounts are created with system-generated email addresses (ending in \@ewars.ws) or for EWARS users working offline.
  --------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To enable two-factor authentication, follow the steps below.

-   Select **Menu** \> **Users \>** click on the **edit** ![](media/image240.png){width="0.2916666666666667in" height="0.275in"}icon of the relevant user. Under **Account Security**, in the **Two-factor authentication** field, select **Active** from the drop-down menu.

## 9.5 Assigned tasks under your role

In EWARS, new user registration, reporting assignments, amendments to reports and deletion of reports happen through a systematic approval process. As an administrative user (Account Administrator or Geographical Administrator), you have to manage these tasks if they fall under your geographical administrative area.

A task is created for the Geographical Administrator/Account Administrator whenever a Reporting User requests any of the following:

-   registration of requests

-   approval of assignment requests

-   approval of amendment requests

-   approval of record deletion requests.

The sections below explain how each task is managed.

### 9.5.1 Viewing assigned tasks

As an administrative user, the tasks listed above are in your account. Follow the steps below to see what tasks are assigned to you, needing your approval. For EWARS to function successfully, an administrative user should check tasks on a daily basis.

-   Click on the ![](media/image259.png){width="0.7in" height="0.25in"} icon at the top left-hand corner \> click on ![](media/image260.png){width="0.5916666666666667in" height="0.24166666666666667in"}, and all tasks are visible as shown below:

![](media/image261.png){width="5.808333333333334in" height="2.8583333333333334in"}

### 9.5.2 Performing user registration requests

-   Click on ![](media/image260.png){width="0.5916666666666667in" height="0.24166666666666667in"} at the left-hand side of the EWARS home screen \> click on **Registration requests** under **ADMIN TASKS** \> click on any of the **Registration requests**, and the screen below appears:

![](media/image262.png){width="4.433333333333334in" height="3.125in"}

EWARS allows access to the system via an approval process. Any user who needs access is required to request approval, unless the user is created by the Account Administrator (refer to **Chapter 8. Users and their assignments** for more information).

Read through the request, and review the role of the user. Approve or reject it, according to your needs.

-   **Either** click on ![](media/image263.png){width="0.7916666666666666in" height="0.23333333333333334in"} to register the user, and a notification email is sent to the user

-   **Or** click on ![](media/image264.png){width="0.7333333333333333in" height="0.20833333333333334in"}, and the **Registration requests** dialogue box opens, as shown below:

![](media/image265.png){width="4.433333333333334in" height="2.425in"}

-   Provide a **reason for rejection** \> click on ![](media/image266.png){width="0.7416666666666667in" height="0.2in"}, and a notification email is sent to the user.

### 9.5.3 Performing assignment requests

This function is used when an assignment is requested by a Reporting User. Assignments for any form require the approval of an Account Administrator.

-   Click on ![](media/image260.png){width="0.5916666666666667in" height="0.24166666666666667in"} at the left-hand side of the EWARS home screen \> click on **Assignment requests** under **ADMIN TASKS** \> click on any of the **Assignment requests**, and the screen below appears:

![](media/image267.png){width="4.5in" height="2.591666666666667in"}

-   **Either** click on ![](media/image263.png){width="0.7916666666666666in" height="0.23333333333333334in"} to approve the request, and a notification email is sent to the user

-   **Or** click on ![](media/image264.png){width="0.7333333333333333in" height="0.20833333333333334in"} \> provide a reason for rejection \> click on ![](media/image266.png){width="0.7416666666666667in" height="0.2in"} , and a notification email is sent to the user.

### 9.5.4 Performing amendment requests

This function is used when an amendment of a report is requested by a Reporting User. Amendment of any previously submitted report requires the Account Administrator's approval only if the approval requirement for amendments is enabled. To enable it, refer to **Chapter 6. Forms**, topic **6.8.5 Enabling approval requirement for amendments**.

-   Click on ![](media/image260.png){width="0.5916666666666667in" height="0.24166666666666667in"} at the left-hand side of the EWARS home screen \> click on **Amendment requests** under **ADMIN TASKS** \> click on any of the **Amendment requests**, and the screen below appears:

![](media/image268.png){width="4.475in" height="3.2916666666666665in"}

You can view the changes proposed for amendment under the **Proposed Changes** section.

-   **Either** click on ![](media/image263.png){width="0.7916666666666666in" height="0.23333333333333334in"} to approve the amendment, and a notification email is sent to the user

-   **Or** click on ![](media/image264.png){width="0.7333333333333333in" height="0.20833333333333334in"} \> provide a reason for rejection \> click on ![](media/image266.png){width="0.7416666666666667in" height="0.2in"}, and a notification email is sent to the user.

### 9.5.5 Performing record deletion requests

This function can be requested by the Reporting User when he/she has submitted a report that is entirely invalid or incorrect.

-   Click on ![](media/image260.png){width="0.5916666666666667in" height="0.24166666666666667in"} at the left-hand side of the EWARS home screen \> click on **Record deletion requests** under **ADMIN TASKS** \> click on any of the **Record deletion requests**, and the screen below appears:

![](media/image269.png){width="5.666666666666667in" height="2.625in"}

To view the submitted report, follow the steps below.

-   Click on ![](media/image270.png){width="0.8833333333333333in" height="0.20833333333333334in"}, and the report opens in the **Report manager** menu, as shown below:

![](media/image271.png){width="5.675in" height="3.175in"}

-   **Either** click on ![](media/image263.png){width="0.7916666666666666in" height="0.23333333333333334in"} to approve the request, and a notification email is sent to the user

```{=html}
<!-- -->
```
-   **Or** click on ![](media/image264.png){width="0.7333333333333333in" height="0.20833333333333334in"} \> provide a reason for rejection \> click on ![](media/image266.png){width="0.7416666666666667in" height="0.2in"}, and a notification email is sent to the user.

## 9.6 Notifications

EWARS can send notifications of alerts and other tasks to administrative users. You can receive notifications when an alert is triggered, an alert is reopened, someone comments on an alert, and an alert is automatically closed due to expiration.

### 9.6.1 Subscribing to notifications

You can subscribe to receive notifications based on set preferences. Follow the steps below to set the preferences for subscribing to notifications.

-   Click on the **profile** ![](media/image251.png){width="0.23333333333333334in" height="0.24166666666666667in"} icon \> click on the **Notification Settings** tab, and the screen below appears:

![](media/image272.png){width="5.4375in" height="4.927083333333333in"}

-   To subscribe to notifications as emails, select **Email** from the drop-down menu.

-   To view the notifications in your account, select **Notify** from the drop-down menu.

-   To ignore notifications, select **Ignore** from the drop-down menu.

For demonstration purposes, this guide uses the following two examples.

**Example 1.** Notify via email whenever any alert is triggered.

-   Click on the **profile** ![](media/image251.png){width="0.23333333333333334in" height="0.24166666666666667in"} icon \> click on the **Notification Settings** tab \> select **Email** as shown below:

![](media/image273.png){width="3.7083333333333335in" height="0.38333333333333336in"}

-   Whenever an alert is triggered, you will receive an email notification, as shown below:

![](media/image274.png){width="4.366666666666666in" height="2.8583333333333334in"}

**Example 2.** View the notification in your account whenever an alert is reopened.

-   Click on the **profile** ![](media/image251.png){width="0.23333333333333334in" height="0.24166666666666667in"} icon \> click on the **Notification Settings** tab \> select **Notify** as shown below:

![](media/image275.png){width="3.75in" height="0.38333333333333336in"}

Whenever an alert is reopened, you will receive a system notification in your account. Refer to the following topic for more information.

### 9.6.2 Viewing and managing system notifications

You can view notifications in EWARS and manage them accordingly. As an administrative user, it is recommended that you check notifications frequently.

To view notifications, follow the steps below.

-   Click on the ![](media/image276.png){width="0.6166666666666667in" height="0.25in"} icon at the top left-hand corner \> click on ![](media/image277.png){width="0.59375in" height="0.22916666666666666in"} , and the screen below appears:

![](media/image278.png){width="5.675in" height="2.15in"}

-   Click on a notification (e.g. **Alert re-opened**), and a screen opens with the notification details, as shown below:

![](media/image279.png){width="5.675in" height="2.308333333333333in"}

You can also open the alert by clicking on the **here** link as highlighted in the screenshot above.

To manage notifications, follow the steps below.

-   To clear a notification, click on the **delete** ![Inserting image\...](media/image280.png){width="0.21875in" height="0.20833333333333334in"} icon at the right-hand side of the notification, and the notification is deleted.

-   To clear all notifications, click on ![](media/image281.png){width="0.9270833333333334in" height="0.21875in"} at the top right-hand corner, and all notifications are deleted.

### 9.6.3 Receiving email notifications in plain text format

By default, you will receive email notifications in HyperText Markup Language (HTML) format, as shown below:

![](media/image282.png){width="5.0in" height="3.6145833333333335in"}

To change the **Email Format** to plain text, follow the steps below.

-   Click on the **profile** ![](media/image251.png){width="0.23333333333333334in" height="0.24166666666666667in"} icon \> click on the **Notification Settings** tab. Look for the **Email Format** field, and the screen below appears:

![](media/image283.png){width="5.65in" height="1.5083333333333333in"}

-   Select **Send plain text email** from the drop-down menu. You will see email notifications in a plain text format, as shown below:

![](media/image284.png){width="5.725in" height="1.6833333333333333in"}

### 9.6.4 Disabling email notifications

By default, email notifications is enabled. If you disable the function, you will not receive any notification via email, even if you have subscribed to them. However, you will continue to receive administrative emails, such as password reset emails and other task-oriented emails.

  ---------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![](media/image43.png){width="0.65625in" height="0.3541666666666667in"}   Email notifications should be kept enabled for alerts and administrative tasks so that you are made aware rapidly of disease threats requiring a response.

  ---------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------

To disable email notifications, follow the steps below:

-   Click on the **profile** ![](media/image251.png){width="0.23333333333333334in" height="0.24166666666666667in"} icon \> click on the **Notification Settings** tab \> look for the **Email Notifications** field. By default, **Email Notifications** is enabled, as shown below:

![](media/image285.png){width="5.783333333333333in" height="1.4in"}

-   To disable it, select **Disable Email Notifications** from the drop-down menu.

## 9.7 Viewing activities

EWARS keeps track of two types of activities:

-   new report submissions

-   new user registrations

You can view these activities along with their date and time of occurrence as follows.

-   Click on the ![](media/image276.png){width="0.7in" height="0.26666666666666666in"} icon \> click on ![](media/image286.png){width="0.6979166666666666in" height="0.22916666666666666in"} at the left-hand side, and the screen below appears:

![](media/image287.png){width="5.766666666666667in" height="2.933333333333333in"}

To view submitted reports via the activity feature, follow the steps below.

-   Look for a new report submission activity \> click on it, and the report opens in the **Report manager** menu, as shown below:

![](media/image288.png){width="5.691666666666666in" height="3.1416666666666666in"}

You can view the name of the user and the date of submission.

To view details of a newly joined user in the activity list, follow the steps below.

-   Look for new user registration activity \> click on it, and the screen below appears:

![](media/image289.png){width="5.675in" height="2.691666666666667in"}

You can view the name of the user, his/her organization, role, date and time of joining, activities and assignments.

The following chapter explains how the Account Administrator helps to manage the EWARS account settings for users.

# Chapter 10. EWARS account settings

The Super Administrator creates an account for each Early Warning, Alert and Response System (EWARS) system that is functional centrally. Following account creation, the Account Administrator configures details for the account. This chapter will help you perform key actions including configuring details such as account name, domain name, setting synchronization expiry time, screen lock time and more (Fig. 10.1).

![](media/image290.png){width="5.833333333333333in" height="5.833333333333333in"}Fig. 10.1. Account configuration actions

Account details are configured under **Settings** in their respective sections, as shown below:

![](media/image291.png){width="5.875in" height="2.9166666666666665in"}

The following sections illustrate how to edit the account details under general settings.

## 10.1 Editing the EWARS account name

-   Click on the [**settings**]{.mark} ![](media/image292.png){width="0.275in" height="0.26666666666666666in"} [icon at the top right-hand corner of the dashboard]{.mark} \> []{.mark}click on []{.mark}![](media/image293.png){width="0.7916666666666666in" height="0.3333333333333333in"}[, and the screen below appears:]{.mark}

![](media/image294.png){width="7.114365704286964in" height="2.4013024934383203in"}

-   Make changes to the **Account name** (e.g. "Country X"). Click on **Save Change(s)**, and the name is edited.

## 10.2 Editing the EWARS account domain

-   Click on the **[settings]{.mark}** ![](media/image292.png){width="0.275in" height="0.26666666666666666in"} [icon]{.mark} \> [click on]{.mark} ![](media/image295.png){width="0.7916666666666666in" height="0.3333333333333333in"}[, and the screen below appears:]{.mark}

![](media/image296.png){width="7.124867672790901in" height="2.345269028871391in"}

-   Make changes to the **Domain name** (noting that the domain name must end ".ewars.ws" -- e.g. **"**countryx.ewars.ws"). Click on **Save Change(s)**, and the name is edited.

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** the Super Administrator may have set the domain name already; if so, you should not change it.
  --------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 10.3 Setting screen lock time

Screen lock time refers to the time interval (in minutes) after which the EWARS Web screen will lock automatically. You need to log in again if the screen becomes locked.

-   Click on the **[settings]{.mark}** ![](media/image292.png){width="0.275in" height="0.26666666666666666in"} [icon]{.mark} \> [click on]{.mark} ![](media/image295.png){width="0.7916666666666666in" height="0.3333333333333333in"}[, and the screen below appears:]{.mark}

![](media/image297.png){width="5.808333333333334in" height="2.4in"}

-   Enter the **Screen Lock Time(Minutes)** in minutes (e.g. "30"). Click on **Save Change(s)**.

## 10.4 Setting the offline sync expiry time in days

[Once you synchronize (sync) your account, the system allows you to work in offline mode for a fixed interval before the expiry time is reached. If you do not sync your account before the expiry time is reached, the account is locked. An Account Administrator can set the offline sync expiry time. You can set this time interval (in days) for the EWARS Stand-alone application.]{.mark}

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** Syncing is only done by EWARS Mobile users and Stand-alone users.
  --------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-   Click on the **settings** ![](media/image292.png){width="0.28125in" height="0.2708333333333333in"} icon at the top right-hand corner of the dashboard \> click on ![](media/image298.png){width="0.7291666666666666in" height="0.2708333333333333in"}, and the screen below appears:

![](media/image299.png){width="6.327963692038495in" height="2.5575524934383203in"}

-   Enter the **Offline Sync Expiry Time (Days)** time interval in days (e.g. "7"). Click on **Save Change(s)**.

## 10.5 Setting the epi week

An epidemiological week (epi week) is a [standardized method to define a week as a period to group epidemiological events. Normally,]{.mark} an epi week starts on Sunday or Monday.

[In EWARS, the default e]{.mark}pi week [starts on Monday, and the e]{.mark}pi week [is thus Monday to Sunday. If you change the e]{.mark}pi week [start to Sunday, the format for the e]{.mark}pi week [is Sunday to Saturday.]{.mark}

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** [it is recommended that the e]{.mark}pi week [start should be set at the beginning, while setting up the account, and that it should not be changed.]{.mark}
  --------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-   Click on the **[settings]{.mark}** ![](media/image292.png){width="0.275in" height="0.26666666666666666in"} [icon]{.mark} \> [click on]{.mark} ![](media/image295.png){width="0.7916666666666666in" height="0.3333333333333333in"}[, and the screen below appears]{.mark}

![](media/image300.png){width="6.605249343832021in" height="3.1787762467191603in"}

-   Select the **epi week Start** day (e.g. Sunday). Click on **Save Change(s)**.

## 10.6 Setting up languages

[EWARS provides multilingual support.]{.mark} The Super Administrator sets the default language for your account; however, if required, the Account Administrator can change the default language.

The following topics set out details about other available languages and their status.

### 10.6.1 Viewing available languages

-   Click on the **[settings]{.mark}** ![](media/image292.png){width="0.275in" height="0.26666666666666666in"} [icon]{.mark} \> [click on]{.mark} ![](media/image53.png){width="0.8666666666666667in" height="0.2833333333333333in"}[, and a list of languages opens, as shown below:]{.mark}

![](media/image301.png){width="5.68333552055993in" height="2.9833333333333334in"}

The Super Administrator sets the default language as English.

### 10.6.2 Changing the default language

-   Click on the [**settings**]{.mark} ![](media/image292.png){width="0.275in" height="0.26666666666666666in"} [icon]{.mark} \> [click on]{.mark} ![](media/image53.png){width="0.8666666666666667in" height="0.2833333333333333in"} []{.mark}\> [look for the preferred language (e.g. French).]{.mark} Click on the **set as default** ![Inserting image\...](media/image302.png){width="0.27248687664041993in" height="0.25833333333333336in"} icon \> click on **Yes**, and the default language changes from English to French.

### 10.6.3 Activating and deactivating languages

-   Click on the **[settings]{.mark}** ![](media/image292.png){width="0.275in" height="0.26666666666666666in"} [icon]{.mark} \> [click on]{.mark} ![](media/image53.png){width="0.8666666666666667in" height="0.2833333333333333in"} []{.mark}\> []{.mark}click on the **change status** ![Inserting image\...](media/image303.png){width="0.27248687664041993in" height="0.25833333333333336in"} icon \> click on **Yes**, and the language status is changed from Active to Inactive, or from Inactive to Active.

  ---------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------
  ![](media/image43.png){width="0.65625in" height="0.3541666666666667in"}   Once a language is set as the default language in EWARS, all instructions, forms, logs, dashboards, bulletins and similar appear in that language.

  ---------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------

You can also make the other languages in your account active to facilitate creation of forms in other languages. For example, if you want to create the reporting form in French, set the status of French as active.

### 10.6.4 Adding a new language to your account

[If your system will function in an emergency context whose business language is not English, you can add a new language to your account.]{.mark}

[For example, you can add new language support for Czech by following the steps below.]{.mark}

**Step 1.** Add the Czech language to your account.

-   Click on the **[settings]{.mark}** ![](media/image292.png){width="0.275in" height="0.26666666666666666in"} [icon]{.mark} \> [click on]{.mark} ![](media/image53.png){width="0.8666666666666667in" height="0.2833333333333333in"} [\>]{.mark} click on ![](media/image304.png){width="0.9916666666666667in" height="0.31666666666666665in"}, and the screen below appears:

![](media/image305.png){width="5.833333333333333in" height="1.525in"}

-   Enter the **Name** of the language (e.g. "Czech") \> select Czech from the **Language** drop-down menu. Click on **Save Change(s)**, and the language is added to the list, as shown below:

![](media/image306.png){width="5.80833552055993in" height="2.7333333333333334in"}

**Step 2.** Add translations.

-   Click on the **edit** ![](media/image307.png){width="0.35833333333333334in" height="0.3416666666666667in"} icon of Czech, and the screen below appears:

![](media/image308.png){width="5.85416447944007in" height="2.9166666666666665in"}

-   Click on ![](media/image309.png){width="1.125in" height="0.25in"} \> click on **Yes**. The labels are translated, and the screen below appears:

![](media/image310.png){width="5.85in" height="2.8833333333333333in"}

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** currently, EWARS uses IBM language services for translation.
  --------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-   Click on **Save Change(s)**.

**Step 3.** Edit auto-translated labels.

The auto-translated options may need some modifications, especially for technical terms.

-   Click on the **edit** ![](media/image307.png){width="0.35833333333333334in" height="0.3416666666666667in"} icon next to the key label (e.g. ADD_VARIABLE), and the screen below appears:

![](media/image311.png){width="5.85in" height="1.65in"}

-   Edit or enter a new translation in the **Value** field. Click on **Save Change(s)**.

## 10.7 Menu access

Menu access refers to the permissions or rights of each user in the system. EWARS can grant or revoke access to the menu for any individual user, based on their role.

  ---------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![](media/image43.png){width="0.65625in" height="0.3541666666666667in"}   You can modify the permissions of different users, so that they may or may not be able to perform certain tasks and actions in the system. This flexibility is needed especially when you have a large geographical area and a diverse user group with varying needs.

  ---------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### 10.7.1 Granting menu access

Reporting Users, Geographical Administrators and Account Administrators have access to different features in the EWARS Web version, but this access can be configured, based on the role and for individual users.

-   Click on the **[settings]{.mark}** ![](media/image292.png){width="0.275in" height="0.26666666666666666in"} [icon]{.mark} \> [click on]{.mark} ![](media/image312.png){width="0.71875in" height="0.28125in"}, which is embedded in the settings and the screen below appears:

![](media/image313.png){width="6.11666447944007in" height="3.408333333333333in"}

You can select features from the left-hand column to assign to a user or role.

When you assign features to a role, everybody with that role will have access to the function. Alternatively, you can provide access to features for an individual user, regardless of their role.

**Example 1.** Grant access based on role.

-   Click on the **[settings]{.mark}** ![](media/image292.png){width="0.275in" height="0.26666666666666666in"} [icon]{.mark} \> [click on]{.mark} ![](media/image312.png){width="0.71875in" height="0.28125in"} [\>]{.mark} click on a **feature (**e.g. Alarms). Select a role from the **Role** drop-down menu (e.g. Reporting User) \> click on ![Inserting image\...](media/image314.png){width="0.4479166666666667in" height="0.3333333333333333in"}, and access is granted and the role added to the list, as shown below:

![](media/image315.png){width="5.891666666666667in" height="2.575in"}

**Example 2.** Grant access to a user.

-   Click on the **[settings]{.mark}** ![](media/image292.png){width="0.275in" height="0.26666666666666666in"} [icon]{.mark} \> [click on]{.mark} ![](media/image316.png){width="0.7166666666666667in" height="0.2833333333333333in"} [\>]{.mark} click on the **feature** (e.g. Alarms) \> select the user from the **User** drop-down menu (e.g. John Smith). Click on ![](media/image317.png){width="0.45in" height="0.3333333333333333in"}, and the user is added to the list and access is granted, as shown below:

![](media/image318.png){width="5.96875in" height="2.375in"}

### 10.7.2 Revoking menu access

Sometimes you may not want certain roles or users making changes to the settings and other features on an ongoing basis. You can therefore revoke access.

-   Click on the **[settings]{.mark}** ![](media/image292.png){width="0.275in" height="0.26666666666666666in"} [icon]{.mark} \> [click on]{.mark} ![](media/image316.png){width="0.7166666666666667in" height="0.2833333333333333in"} []{.mark}\> []{.mark}click on the relevant menu in the list at the left-hand side (e.g. Alarms). [In the relevant user or row field, click on the **delete**]{.mark} ![](media/image319.png){width="0.3541666666666667in" height="0.34375in"} [icon under **Action**]{.mark} \> [click on **Yes**,]{.mark} and access is revoked[.]{.mark}

## 10.8 Categorizing alert events reported to EWARS

This feature is used under the alert management module when alerts are based on events.

Event-based surveillance alerts are usually reported from the community and may not be reported as a particular disease or condition. However, the WHO or ministry of health surveillance officer may allocate the alert to disease categories (e.g. acute flaccid paralysis (AFP) or haemorrhagic fever) for further investigation during management of the alert.

In some instances, you can allow alerts from event-based surveillance forms to indicate what the alert or the rumour is likely to be. For example, clusters of cases and deaths following vomiting, diarrhoea and fever are likely to be caused by cholera. This indication of the "likely disease" will help alert management in detecting the outbreak rapidly.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** you can add a list of likely diseases that should be considered in the alert management module for alerts sent via event-based surveillance forms.
  --------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

For more information, refer to **Chapter 13. Alert log**, topic **13.3 Assessing the risk of an alert**.

Follow the steps below to add the list of diseases you want to be considered "likely" under alerts from the event-based surveillance forms.

**Step 1.** Categorize the event.

-   Click on the **[settings]{.mark}** ![](media/image35.png){width="0.24166666666666667in" height="0.25833333333333336in"} [icon]{.mark} \> [click on **Alerts**. Click on **Yes** in **Show Likely Event in Risk Assessment**, and the system displays the field **Likely** **Events(Diseases)**, as shown below:]{.mark}

![](media/image320.png){width="4.95in" height="4.366666666666666in"}

**Step 2.** Add the disease.

-   [Click on the **add**]{.mark} ![](media/image321.png){width="0.25833333333333336in" height="0.26666666666666666in"} [icon to add a new disease to the list]{.mark} \> []{.mark}enter "Cholera" in **Display Name** (visible to the user) and "CH" in **Value** (stored in the system). Click on **Save Change(s)**.

-   [To **edit** the disease, click on the **edit**]{.mark} ![](media/image307.png){width="0.35833333333333334in" height="0.3416666666666667in"} [icon]{.mark} \> [change the display name. Click on **Save **]{.mark}**Change(s)**[.]{.mark}

-   [To **delete** the disease, click on the **delete**]{.mark} ![](media/image319.png){width="0.3541666666666667in" height="0.34375in"} [icon. Click on **Save **]{.mark}**Change(s)**[.]{.mark}

[The following chapter explains how to submit reports, check for duplicate records, and amend or download them according to user requirements.]{.mark}

#  

# PART III. Data Collection and Monitoring

Part II addressed how to set up the structure for reporting in the Early Warning, Alert and Response System (EWARS). The following chapters focus on the Data Collection feature. They illustrate how to view and validate data and verify alerts triggered by the collected data, and how to set up EWARS key performance indicators. In addition, they set out how to use the Data Import feature to import data collected from other systems into EWARS in a seamless manner (Fig. III.1).

Fig. III.1. Data Collection and Monitoring features

![](media/image322.png){width="5.0in" height="4.385416666666667in"}

# Chapter 11. Report manager

This chapter provides an overview of Report manager, a powerful feature in the Early Warning, Alert and Response System (EWARS) that allows you to view, validate, search, amend and analyse reports with ease. "Reports" are the raw data collected and entered into the system by Reporting Users. Thus, the Report manager feature serves as a repository of all data related to each reporting form in the system, underscoring its importance. It allows reports in the system to be utilized for in-depth analysis and subsequent action.

## 11.1 Viewing reports

Using Report manager, you can view all reporting forms in the left-hand column, and related data appear at the right-hand side.

**Example 1.** View weekly EWARS reporting form reports.

-   Select **Menu** \> **Report manager**, and the screen below appears:

![](media/image323.png){width="5.74166447944007in" height="2.8833333333333333in"}

-   Click on **Weekly EWARS Reporting Form**, and it opens, as shown below:

![](media/image324.png){width="5.95in" height="2.941666666666667in"}

This shows the complete dataset of the data reported for the relevant form.

Each row represents a submitted report. Within each row, you can perform five functions, as depicted below:

![](media/image325.png){width="2.276042213473316in" height="0.4791666666666667in"}

![](media/image326.png){width="0.2916666666666667in" height="0.2833333333333333in"} edit/view the report

![](media/image327.png){width="0.25in" height="0.2833333333333333in"} download the report

![](media/image328.png){width="0.3in" height="0.2833333333333333in"} re-evaluate an alert

![](media/image329.png){width="0.2833333333333333in" height="0.275in"} complete a sub form (if available) for the report

![](media/image330.png){width="0.3333333333333333in" height="0.325in"} view sub form records (if any).

-   Click on the **edit/view** ![](media/image326.png){width="0.2916666666666667in" height="0.2833333333333333in"} icon of the submitted report, and the screen below appears:

![](media/image331.png){width="6.5in" height="3.0770833333333334in"}

The edit/view function will enable you to view individual reports. It will also help you to make further edits as explained in topic **11.8 Amending a report and viewing amendment history** below.

## 11.2 Searching a report

Report manager makes it easy to search specific reports. A keyword entered in the search box is matched against the data in the report. This facilitates early retrieval of the report the user wants.

-   Select **Menu** \> **Report manager**. Click on the name of the form (e.g. Weekly EWARS Reporting Form) \> enter text into the search box (e.g. "100"). Click on the **search** ![](media/image332.png){width="0.25in" height="0.25833333333333336in"} icon, and reports that contain the search text are listed, as shown below:

![](media/image333.png){width="5.96666447944007in" height="2.5083333333333333in"}

-   Click on ![](media/image334.png){width="0.25in" height="0.25in"} to clear the search.

## 11.3 Finding duplicate reports

Duplicate entries of a single report may exist in the system. EWARS helps to identify these so that they can be deleted to remove redundant data.

  ---------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![](media/image43.png){width="0.65625in" height="0.3541666666666667in"}   Finding duplicate data entries is especially important in line listing or case-based data. This is one of the strategies EWARS uses to improve data quality. For example, in line lists, you may want to search for duplicates using three variables: name + age + primary health-care centre (PHCC).

  ---------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can check for duplicate records that match the selected column values in two ways:

-   by selecting a single field

-   by selecting multiple fields.

For demonstration purposes, this guide uses the following example.

**Example 1.** Find duplicates in cholera line list with three variables: name of case, age and sex.

-   Select **Menu** \> **Report manager**. Click on the **folder** ![](media/image335.png){width="0.3in" height="0.2833333333333333in"} icon of the Cholera Line List \> click on ![](media/image336.png){width="0.8333333333333334in" height="0.25in"}. Select the form fields Name of case, Age and Sex to filter \> click on **Apply**, and the screen below appears:

![](media/image337.png){width="4.941666666666666in" height="2.775in"}

All matching rows are grouped together, and the groups are coloured alternately as shown in the screenshot above. Once you identify the duplicates, you can decide which to delete to leave only one correct report in the system.

-   Click on the **edit** ![](media/image326.png){width="0.2916666666666667in" height="0.2833333333333333in"} icon of the duplicate report, and the report opens. Click on **Delete Report** \> provide a reason for deletion ("duplication") \> click on **Submit**, and the duplicate report is deleted. Repeat these steps for other duplicates.

-   Click on ![](media/image338.png){width="0.6083333333333333in" height="0.25in"} to remove the filter.

## 11.4 Adding comments to reports

The feature allows you to add comments to reports; these are useful in report authentication. Users who view the reports can also view the complete thread of comments -- a discussion associated with the report.

To add comments and view them, follow the steps below.

-   Select **Menu** \> **Report manager** \> click on the **folder** ![](media/image335.png){width="0.3in" height="0.2833333333333333in"} icon of the relevant form. Click on the **edit** ![](media/image326.png){width="0.2916666666666667in" height="0.2833333333333333in"} icon \> click on the **comment** ![](media/image339.png){width="0.3in" height="0.2916666666666667in"} icon at the right-hand side, and the discussion screen below appears:

![](media/image340.png){width="4.4in" height="1.7166666666666666in"}

-   Enter a comment (e.g. "The total cases reported for Cholera are 127. Verify it."). Click **Enter**, and the comment is added. Comments are listed in chronological order and can only be seen under Report manager.

![](media/image341.png){width="5.95833552055993in" height="2.425in"}

## 11.5 Viewing alerts triggered by reports and re-evaluating them

You can view the alerts triggered by reports and re-evaluate them, if they are found to be incorrect. Triggered alerts are recorded in the alert log. For more information, refer to **Chapter 13. Alert log**.

To view triggered alerts, follow the steps below.

-   Select **Menu** \> **Report manager** \> click on the **folder** ![](media/image335.png){width="0.3in" height="0.2833333333333333in"} icon of the relevant form. Click on the **edit** ![](media/image326.png){width="0.2916666666666667in" height="0.2833333333333333in"} icon\> click on the **alarm** ![](media/image328.png){width="0.3in" height="0.2833333333333333in"} icon, and the screen below appears:

![](media/image342.png){width="6.00833552055993in" height="0.825in"}

To re-evaluate associated alarms against the report, follow the steps below.

If a record is associated with an alarm, on submission of the report, the system automatically triggers an alert. This feature makes it easy to re-evaluate the alert, which means that you can revisit the alert management process.

-   Select **Menu** \> **Report manager** \> click on the **folder** ![](media/image335.png){width="0.3in" height="0.2833333333333333in"} icon of the relevant form. Click on the **alarm** ![](media/image343.png){width="0.25in" height="0.25in"} icon at the right-hand side, and the report is sent for re-evaluation.

For more detail, refer to **Chapter 7. Alarms**.

## 11.6 Downloading reports as PDF or Word files

[The system allows you to download individual reports in two formats: PDF and Microsoft Word. These are easily printable formats, which is helpful in places where paper evidence is valued.]{.mark}

-   Select **Menu** \> **Report manager** \> click on the **folder** ![](media/image335.png){width="0.3in" height="0.2833333333333333in"} icon of the relevant form. Click on the **export** ![](media/image327.png){width="0.25in" height="0.2833333333333333in"} icon, and the screen below appears:

![](media/image344.png){width="5.958333333333333in" height="1.3902777777777777in"}

-   Click on **Export as PDF**, and the file is downloaded. Open it, and it appears as below:

![](media/image345.png){width="5.95833552055993in" height="2.525in"}

-   Click on **Export as Microsoft Word**, and the file is downloaded. Open it, and it appears as below:

![](media/image346.png){width="5.96666447944007in" height="2.7416666666666667in"}

## 11.7 Downloading a blank report as a PDF or Word file

[The system allows you to download blank reports in two formats: PDF and Microsoft Word. These are printable: you can print and use the paper formats for reporting, which is helpful in places where paper reporting is valued.]{.mark}

-   Select **Menu** \> **Report manager**. Click on the **folder** ![](media/image335.png){width="0.3in" height="0.2833333333333333in"} icon of the relevant form. Click on the **export** ![](media/image327.png){width="0.25in" height="0.2833333333333333in"} icon, and the screen below appears:

![](media/image347.png){width="6.195807086614173in" height="2.0394531933508313in"}

-   Click on **Export as PDF**, and the file is downloaded. Open it, and it appears as below:

![](media/image348.png){width="5.99166447944007in" height="2.175in"}

-   Click on **Export as Microsoft Word**, and the file is downloaded. Open it, and it appears as below:

![](media/image349.png){width="5.99166447944007in" height="2.158333333333333in"}

## 11.8 Amending a report and viewing amendment history

[If you find any inaccurate entries, Report manager enables you to amend reports. You can also view the amendment history.]{.mark} Amendment of any submitted report requires the Account Administrator's approval. You also need to enable the amendment, as described in **Chapter 6. Forms**, topic **6.8.5 Enabling approval requirement for amendments**.

[For example, if a]{.mark} Reporting User [accidentally enters 10 cases of]{.mark} acute flaccid paralysis ([AFP) (instead of 0 cases) for epidemiological week (]{.mark}epi week[) 15, the report needs to be amended to reflect the correct number.]{.mark}

To amend a report, follow the steps below.

-   Select **Menu** \> **Report manager** \> click on the **folder** ![](media/image335.png){width="0.3in" height="0.2833333333333333in"} icon of the relevant form. Click on the **edit** ![](media/image350.png){width="0.25833333333333336in" height="0.25in"} icon \> click on ![](media/image351.png){width="1.1666666666666667in" height="0.25in"}, and the report opens in amendment mode, as shown below:

![](media/image352.png){width="5.58333552055993in" height="3.175in"}

-   Make the desired changes \> provide a reason for the amendment \> click on **Submit Amendment**.

You can view two different types of report amendment history.

To view the form submission history, which lists the submission date and time of any amendments, follow the steps below.

-   Select **Menu** \> **Report manager**. Click on the **folder** ![](media/image353.png){width="0.3in" height="0.2833333333333333in"} icon of the relevant form. Click on the **edit** ![](media/image350.png){width="0.25833333333333336in" height="0.25in"} icon \> click on the **report history** ![](media/image354.png){width="0.3333333333333333in" height="0.3in"} icon at the right-hand side.

![](media/image355.png){width="6.11666447944007in" height="1.425in"}

To view the original and revised values of the modified fields for each amendment, follow the steps below.

-   Select **Menu** \> **Report manager** \> click on the **folder** ![](media/image335.png){width="0.3in" height="0.2833333333333333in"} icon of the relevant form. Click on the **edit** ![](media/image326.png){width="0.2916666666666667in" height="0.2833333333333333in"} icon\> click on the **amendments** ![](media/image356.png){width="0.3333333333333333in" height="0.2916666666666667in"} icon at the right-hand side, and a list of amendments appears, as shown below:

![](media/image357.png){width="6.03333552055993in" height="1.1166666666666667in"}

-   Click on the **expand** ![](media/image358.png){width="0.35833333333333334in" height="0.31666666666666665in"} icon to view the amendment details, as shown below:

![](media/image359.png){width="6.04166447944007in" height="1.55in"}

## 11.9 Deleting a report

The Account Administrator can delete any report that is entirely invalid or incorrect.

  ---------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------
  ![](media/image43.png){width="0.65625in" height="0.3541666666666667in"}   Deleting records that are already submitted is not recommended. Each report should be submitted after careful consideration and data entry checks.

  ---------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------

-   Select **Menu** \> **Report manager**. Click on the **folder** ![](media/image335.png){width="0.3in" height="0.2833333333333333in"} icon of the relevant form. Click on the **edit** ![](media/image350.png){width="0.25833333333333336in" height="0.25in"} icon \> click on ![](media/image360.png){width="1.0916666666666666in" height="0.25833333333333336in"} and provide a reason for deletion. Click on **Submit**, and a notification appears that the report is deleted permanently.

## 11.10 Submitting a new report

In EWARS, most reports are submitted by Reporting Users, using EWARS Mobile. Web users like Account Administrators or Geographical Administrators using the web version of the system are not expected to submit reports. However, even these roles can submit reports during an emergency.

-   Select **Menu** \> **Report manager**. Click on the **add** ![](media/image329.png){width="0.2833333333333333in" height="0.275in"} icon on the right-hand side of the form name, and the screen below appears:

![](media/image361.png){width="5.66666447944007in" height="2.841666666666667in"}

-   Populate the **Location**, **Report date** and remaining report fields.

-   Click on ![](media/image362.png){width="0.7583333333333333in" height="0.23333333333333334in"}.

All mandatory fields need to be completed for any report to be submitted. If any mandatory field is not filled in, the system will flag this, and submission will fail. Once all the necessary fields are fille din, submission can be completed.

## 11.11 Saving a report as a draft

-   Select **Menu** \> **Report manager**. Click on the **add** ![](media/image329.png){width="0.2833333333333333in" height="0.275in"} icon at the right-hand side of the form name and the screen below appears:

![](media/image361.png){width="5.66666447944007in" height="2.841666666666667in"}

-   Populate the **Location**, **Report date** and remaining report fields.

-   Click on ![](media/image363.png){width="0.7833333333333333in" height="0.25in"}, and the report is saved as a draft.

## 11.12 Editing and submitting a draft report

-   Select **Menu** \> **Data Collection** \> **Report manager** \> ![](media/image364.png){width="0.7333333333333333in" height="0.25833333333333336in"}. Click on the **edit** ![](media/image365.png){width="0.2833333333333333in" height="0.275in"} icon \> edit the desired field values \> click on ![](media/image362.png){width="0.7583333333333333in" height="0.23333333333333334in"}.

![](media/image366.png){width="5.89166447944007in" height="2.7083333333333335in"}

## 11.13 Deleting a draft report

-   Select **Menu** \> **Data Collection** \> **Report manager** \> ![](media/image364.png){width="0.7333333333333333in" height="0.25833333333333336in"}. Click on the **delete** ![](media/image367.png){width="0.25833333333333336in" height="0.2916666666666667in"} icon \> click on **Confirm**, and the draft is deleted permanently.

## 11.14 Submitting a new sub form report

Sub forms enable you to add associated additional information to existing reports. For example, during an outbreak, cases can be captured through a line list, which is the main form, and a laboratory (lab) report form can act as a sub form for each record in the line list.

The sub form and the main form are linked via a unique identifier (ID), such as a government-issued unique card number, health card number, tax registration number, mobile phone number or any other unique generated code.

Most sub forms are submitted by Reporting Users. Web users are usually not tasked with submission of forms. However, if the Reporting User is a lab, there may be web users who submit sub forms via a web interface.

You can submit a sub form report by clicking directly on the sub form or navigating to the main report and selecting the sub form from it. Once the sub form is updated, the main form section is updated automatically.

Treat the sub form like any other form you submit. Unlike other forms, however, the sub form will have a field for a unique ID. This field, once filled, will connect the sub form to the main form. Having a unique ID will also enable automatic population of some fields that enhance case identification.

To submit a sub form report by clicking on the sub form directly (e.g. Cholera Lab test), follow the steps below.

-   Select **Menu** \> **Report manager**. Click on the **add** ![](media/image329.png){width="0.2833333333333333in" height="0.275in"} icon of the form (e.g. Cholera Lab test), and Cholera cases are listed with an **add** ![](media/image329.png){width="0.2833333333333333in" height="0.275in"} icon as shown below:

![](media/image368.png){width="5.60833552055993in" height="2.316666666666667in"}

-   Search by a unique case ID \> look for the case \> click on the **add** ![](media/image329.png){width="0.2833333333333333in" height="0.275in"} icon, and the **Sub Form** opens with automatically populated case details, as shown below:

![](media/image369.png){width="5.675in" height="2.816666666666667in"}

-   Fill in the lab test details \> click on **Submit**, and the report is submitted.

To submit a sub form report using the sub form option of the main report, follow the steps below.

-   Select **Menu** \> **Report manager** \> click on the Cholera line list, and cholera cases are listed, as shown below:

![](media/image370.png){width="6.9049737532808395in" height="2.819530839895013in"}

-   Search for the unique ID of the relevant cholera case \> look for the case \> click on the **add** ![](media/image329.png){width="0.2833333333333333in" height="0.275in"} icon of the case. Click on the Cholera lab test **Sub Form**, and it opens, as shown below:

![](media/image371.png){width="6.09375in" height="3.0214840332458444in"}

-   Fill in the lab test details \> click on **Submit**, and the report is submitted.

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** you can save the sub form report as a draft for future changes and submit it later.
  --------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The following chapter explores Monitoring and Evaluation (M&E) Auditor -- an important feature that aids in the supervision of reporting.

# Chapter 12. M&E Auditor

This chapter will provide an overview of the monitoring and evaluation (M&E) Auditor -- a key feature of the Early Warning, Alert and Response System (EWARS). The M&E Auditor feature helps you oversee the performance (timeliness and completeness) of interval-based reporting from different locations. The chapter will help you evaluate the quality of reporting, export performance data, and analyse it.

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** the M&E Auditor is pre-configured, and users are not required to configure anything.
  --------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 12.1 Key performance indicators of reporting

EWARS uses two key performance indicators to measure its performance of early warning, alert and response.

-   **Completeness of reporting** refers to submission of reports within a defined period of time.

Formula: (Number of reports submitted/number of reports expected) × 100%

-   **Timeliness of reporting** refers to submission of reports on time. It includes an overdue threshold -- for example, if the epidemiological week (**epi week**) starts on Monday and you can consider all reports on the previous week submitted by Wednesday as "on time", you need to set an overdue threshold of +3 days in the form.

Formula: (Number of reports submitted on time/number of reports expected) × 100%

Completeness and timeliness performance are graded as shown below:

![](media/image372.png){width="4.441666666666666in" height="1.5in"}

Reporting performance for any active form whose reporting is deemed interval-based can be reviewed using the M&E Auditor. Refer to topic **6.8.1 Enabling interval-based reporting** for more information.

The performance can be measured at all levels of reporting hierarchy, including the national, provincial, district and primary health-care levels.

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** locations need to be configured correctly to show the number of expected reports.
  --------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 12.2 Viewing completeness or timeliness of reporting

To review the performance of a specific form, follow the steps below.

-   Select **Menu** \> **M&E Auditor**, and the screen below appears:

![](media/image373.png){width="5.895833333333333in" height="0.994922353455818in"}

Select **Indicator** \> select the relevant **Form** \> select the **Start date** and **End date**.

For example, to view the completeness of weekly EWARS reporting form reporting for the period 1 July 2020 to 23 April 2021, follow the steps below:

-   Select **Reporting Completeness** from the **Indicator** drop-down menu.

-   Select **Weekly EWARS Reporting form** from the **Form** drop-down menu.

-   Select the **Start date** 01-07-2020 in the calendar.

-   Select the **End date** 23-04-2021 in the calendar.

Completeness performance for the selected report for the specified period appears, as shown below:

> ![](media/image374.png){width="6.04166447944007in" height="0.8in"}

-   To review the performance at a lower geographical level, click on the **expand** ![](media/image375.png){width="0.25in" height="0.275in"} icon next to the **Location Name**. Continue expanding to the lowest level in the hierarchy to review performance, as shown below:

> ![](media/image376.png){width="5.95833552055993in" height="1.45in"}
>
> The above result table displays the location name column with several other columns showing weekly performance for the location.
>
> To view timeliness data, follow the same steps but select "Reporting Timeliness" from the drop-down menu.

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** locations need to be configured correctly to show the number of expected reports.
  --------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 12.3 Exporting performance data

-   Click on ![](media/image377.png){width="0.9666666666666667in" height="0.36666666666666664in"}, and the **export_audit.csv** file is downloaded, with details of the expanded locations, as shown below:

![](media/image378.png){width="5.66666447944007in" height="1.7833333333333334in"}

## 12.4 Plotting completeness and timeliness indicator

To analyse the completeness and timeliness of reporting, you can use the form submissions indicator under system indicators. To learn more about this, refer to **Chapter 5. Indicators**, topic **5.8 System indicators**.

The completeness and timeliness of reporting can be analysed in various features, including Plot, Mapping, Document Templates, Website Builder and Notebooks. For demonstration purposes, this guide uses the following two examples.

**Example 1.** Use the Plot feature to draw a plot of the completeness of the weekly EWARS reporting form.

-   Select **Menu** \> **Plot**. Select **Time Series** from the **Chart** **Type** drop-down menu.

```{=html}
<!-- -->
```
-   Configure the other settings in the **General** **Settings** tab (for more information, refer to **Chapter 15. Plot**, topic **15.2 Plotting data on a time series chart**). Enter "Completeness of the weekly EWARS reporting form" as the **Chart Title** \> enter "epi week" as the **X Axis title** \> enter "Completeness" as the **Y Axis title** \> set **Show legend** as **Yes**, set **Show slices with no data** as **Yes** if you want to show weeks with 0 reporting, or select **No** if you want to omit weeks with 0 reporting \> select the correct **Location** \> set **Group By** as **Time Interval and** select a suitable interval \> set **Compare Years** as **Yes** if you want to compare completeness of two or more years, and select years accordingly \> select the **Start date** 2021-01-01 in the calendar \> select the **End date** 2020-12-31 in the calendar.

```{=html}
<!-- -->
```
-   Switch to the **Data** tab \> click on the **add** ![](media/image379.png){width="0.24166666666666667in" height="0.21666666666666667in"} icon \> select **Indicator** \> **System** \> **Form Submissions** \> select **Weekly EWARS Reporting Form** \> select dimension as **Completeness**. The chart is generated as shown below:

![](media/image380.png){width="6.302083333333333in" height="3.0460061242344705in"}

**Example 2.** Use the Notebooks feature to render completeness of the weekly EWARS reporting form for each province on a map.

-   Select **Menu** \> **Notebooks** \> **Create Notebook**.

-   Drag the **Map** widget from the left-hand column into the notebook \> click on the **settings** ![](media/image381.png){width="0.325in" height="0.2916666666666667in"} icon.

-   Enter a **Title** and configure the **Location source**: set **Location(s)** as **Of Type** \> select **Location** \> select **Location type**.

-   Configure the **Data Source**: set **Query Type** to **Indicator** \> select **Indicator** \> **System** \> **Form Submissions** from the drop-down menu. Select the **Form** Weekly EWARS Reporting Form \> select **Dimension** as **Completeness (%)** \> select the **Source** of reporting (if you want to consider both EWARS Mobile and EWARS Web reporting, select **No selection**). Select how you want the data to be aggregated: **Sum** or **Average**. Select the start date and end date under **Period**. Configure other options in accordance with **Chapter 18. Notebooks**.

-   Click on **Save Change(s)** \> click on **View**, and the screen below appears:

![](media/image382.png){width="6.05in" height="2.9166666666666665in"}

[The following chapter is about alert management in EWARS.]{.mark}

# Chapter 13. Alert log

This chapter provides an overview of alert management -- a collective, dynamic process that takes place with clinicians, reporting officers, labs and the community. Alert management is one of the major features of the Early Warning, Alert and Response System (EWARS).

Alerts triggered are recorded in the Alert log. You have to follow a standardized four-stage workflow to manage them effectively (Fig. 13.1):

-   verification

-   risk assessment

-   risk characterization

-   outcome.

Fig. 13.1. Alert workflow process

![](media/image383.png){width="6.5636734470691165in" height="2.912630139982502in"}

Alerts are triggered based on the criteria set under each disease or event, according to the prevailing conditions. Alert criteria are set under alarms. It is recommended that you read the alarms chapter before managing the alert log. for more information on alarms, refer to **Chapter 7. Alarms**.

## 13.1 Viewing triggered alerts

The alerts below are triggered based on alarms that you have set up under the Alarms feature.

-   Select **Menu** \> **Alert Logs** \> **Open alerts**, and open alerts are listed, as shown below:

![](media/image384.png){width="5.74166447944007in" height="2.2416666666666667in"}

-   Click on the **view** ![](media/image330.png){width="0.3333333333333333in" height="0.325in"} icon of an alert (e.g. Cholera), and the alert overview screen opens, as shown below:

![](media/image385.png){width="5.74166447944007in" height="2.566666666666667in"}

You can see above that the cholera alert is triggered, and its verification is pending.

### 13.1.1 Viewing the report that triggered the alert

-   Select **Menu** \> **Alert Logs** \> **Open Alerts**. Click on the **view** ![](media/image330.png){width="0.3333333333333333in" height="0.325in"} icon of an alert \> click on the ![](media/image386.png){width="0.7833333333333333in" height="0.4083333333333333in"} tab \> click on the report visible at the left-hand side to view the information, as shown below:

![](media/image387.png){width="5.825in" height="2.0166666666666666in"}

You can see the name of the user who submitted the report and the date of submission. You can also see the relevant forms/sub forms that triggered the alert at the left-hand side.

### 13.1.2 Commenting while managing alerts and checking user activity

Alert management is a dynamic and collaborative process. The activity section is used to facilitate easy communication between users handling a particular alert. Under this, you can view entries and comments made by users.

To view and add a comment, follow the steps below.

-   Select **Menu** \> **Alert Logs** \> **Open Alerts**. Click on the **view** ![](media/image330.png){width="0.3333333333333333in" height="0.325in"}icon of an alert \> click on the ![](media/image388.png){width="0.8916666666666667in" height="0.425in"} tab. Type your comment in the rectangular box at the bottom of the screen \> click on ![](media/image389.png){width="1.1458333333333333in" height="0.2708333333333333in"}and the comment is added.

![](media/image390.png){width="6.39583552055993in" height="3.4244356955380577in"}

### 13.1.3 Analysing and viewing the disease trend that triggered the alert

-   Select **Menu** \> **Alert Logs** \> **Open Alerts**. Click on the **view** ![](media/image330.png){width="0.3333333333333333in" height="0.325in"} icon of an alert (e.g. Cholera). Click on ![](media/image391.png){width="0.875in" height="0.4166666666666667in"} to **analyse** the record, and the alert trend below appears:

![](media/image392.png){width="5.64166447944007in" height="2.55in"}

The graph shows the number of cholera cases reported from Nambutu over a period of time.

### 13.1.4 Viewing users for the alert

-   Select **Menu** \> **Alert Logs** \> **Open Alerts**. Click on the **view** ![](media/image330.png){width="0.3333333333333333in" height="0.325in"} icon of an alert \> click on ![](media/image393.png){width="0.8020833333333334in" height="0.37916666666666665in"}, and the list of users who have participated in the alert appears:

![](media/image394.png){width="4.233333333333333in" height="3.1666666666666665in"}

## 13.2 Verifying an alert

Once an alert is triggered, the first step is to verify it. Verification of the alert determines whether an alert is valid (true) or not.

Not all alerts are true or valid. For instance, calculation errors in the weekly tally, errors in data input, false rumours and similar may produce false alerts. Therefore, the first step in alert management is confirmation of triggered alerts as true and of public health importance.

Alert verification should be done in communication with the clinician, community health worker/volunteer or surveillance officer of the relevant alert.

To verify an alert, follow the steps below.

-   Select **Menu** \> **Alert Logs** \> **Open Alerts**, and open alerts are listed. Click on the **view** ![](media/image330.png){width="0.3333333333333333in" height="0.325in"}icon of an alert to be verified, and the **Alert Workflow** screen below appears:

![](media/image395.png){width="5.75in" height="2.533333333333333in"}

-   Click on **Start verification**, and the verification screen opens. Turn on guidance \> go through the guidance notes. Guidance notes aid the verification process.

-   Enter **Verification notes** \[Mandatory\] (e.g. "The clinical presentation of all cases fits the case definition -- the alert is a true alert" for a true alert, or "There is an error in reporting" for a false alert).

To set the verification **Outcome**, follow one of the options below.

-   Select **Discard** when the alert is verified as a false alert or refers to a disease or hazard that is not applicable to immediate public health action. Once discarded, the alert is closed, and no further steps are required. You can review the verification by clicking on ![](media/image396.png){width="1.1583333333333334in" height="0.3in"}. In the future, if the alert turns out to be critical or valid, you can re-open it and reassess the verification stage.

-   Select **Monitor** when you don't have enough information for the alert to be verified. This indicates that the definitive outcome of an alert verification is still pending. When you have enough information, click on ![](media/image397.png){width="1.2083333333333333in" height="0.26666666666666666in"}to update the alert.

-   Select **Start Risk Assessment** when the alert is verified as genuine. The alert is escalated to the risk assessment stage, and it must be assessed to understand the potential impact it may have on public health.

```{=html}
<!-- -->
```
-   Click on **Submit**.

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** rapidness of alert verification is a key performance measure of a good surveillance system. All triggered alerts should be verified within 48 hours.
  --------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 13.3 Assessing the risk of an alert

All verified alerts should be risk assessed to characterize the public health impact. The risk is assessed in the light of **Hazard**, **Exposure** and **Context**. Risk assessment should be conducted in communication with clinicians, surveillance officers and the laboratory network of the location.

To assess the risk, follow the steps below.

-   Select **Menu** \> **Alert Logs** \> **Open Alerts**, and open alerts are listed. Click on the **view** ![](media/image330.png){width="0.3333333333333333in" height="0.325in"}icon of an alert that is to be assessed, and the alert opens for risk assessment, as shown below:

![](media/image398.png){width="5.791666666666667in" height="2.307292213473316in"}

-   Click on **Start risk assessment**, and the risk assessment screen opens.

-   Enter **Hazard Assessment** information \[Mandatory\]. If confirmatory laboratory tests, rapid diagnostic tests or other supplementary tests have been conducted, enter the information here. Enter clinical or other epidemiological features (e.g. "Cholera Rapid Diagnostic test is positive, stool sample is sent for culture confirmation test. The patient showed clinical signs compatible with Cholera, rice-water stools and severe dehydration").

-   Enter **Exposure Assessment** information \[Mandatory\]. Enter exposure information, such as how many individuals and populations are probably exposed to this hazard (e.g. "The patient is a food handler in the communal kitchen of the internally displaced person (IDP) camp. Three family members are already showing similar symptoms: diarrhoea and signs of dehydration. The camp population has not been vaccinated for cholera in the recent past").

-   Enter **Context Assessment** information \[Mandatory\]. Describe the context that may affect either the transmission potential or the overall impact of the event (e.g. "The camp is overcrowded, with very poor water and sanitation facilities. No hygiene kits are available for distribution. Households do not have safe water for drinking").

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** if you are waiting for lab results, click on **Save Draft** to save the risk assessment at the draft stage and come back when more information is available.
  --------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-   Click on **Submit** to move to the next stage.

Fig. 13.2. The risk assessment process

![](media/image399.png){width="2.9427088801399823in" height="2.8847244094488187in"}

The risk assessment process involves assessment of the hazard or the suspected pathogen, possible exposure to the hazard and the context in which this takes place. Risk assessment is not always a linear, sequential process but an overlap of all three assessments. The outcome of the three individual assessments should be used to characterize the overall level of the verified alert in the next step.

## 13.4 Characterizing the risk of a verified alert

After the risk assessment has been completed, the next step is to assign an overall level of risk to the alert.

-   Select **Menu** \> **Alert Logs** \> **Open Alerts**, and open alerts are listed. Click on the **view** ![](media/image330.png){width="0.3333333333333333in" height="0.325in"}icon of an alert, and the alert opens for risk characterization, as shown below:

![](media/image400.png){width="5.614583333333333in" height="2.366345144356955in"}

-   Click on **Start risk characterization**, and the **Risk Matrix** is visible, as shown below:

![](media/image401.png){width="5.64166447944007in" height="3.4166666666666665in"}

-   Click on a matrix cell. Risks are defined by the likelihood of the event and the potential severity of the consequences.

-   Go through the description of the selected risk -- i.e. the likelihood, consequences and action comments.

Fig. 13.3 will help you to decide the level of risk. The risk assigned determines the urgency and scale of the response. When you have multiple risks, it also helps you to prioritize resources, based on risk levels.

Fig. 13.3. Level of estimated overall risk and potential response

![](media/image402.png){width="5.5756222659667545in" height="3.577691382327209in"}

-   Once you finalize the risk selection, click on **Submit**.

## 13.5 Determining the outcome

After a risk has been characterized, you can assign a risk outcome, as shown below.

-   Select **Menu** \> **Alert Log** \> **Open Alerts**, and open alerts are listed. Click on the **view** ![](media/image330.png){width="0.3333333333333333in" height="0.325in"}icon of an alert \> view the **Alert Workflow** at the outcome stage.

![](media/image403.png){width="5.80833552055993in" height="2.8916666666666666in"}

-   Click on **Start outcome**, and the outcome screen opens.

To set the **Outcome**, follow one of the options below.

-   Select **Respond** when the risk assessment determines that the alert requires immediate public health action (e.g. if cholera is confirmed). A cholera contingency plan is implemented immediately as a result.

```{=html}
<!-- -->
```
-   Select **Discard** when the risk assessment determines that the alert is not applicable to immediate public health action -- for example, if all lab test results are negative for the specified pathogens, and clinical signs are attributed to accidental poisoning. When discarded, the alert is closed, and no further steps are required.

![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}**Note:** if the alert turns out to be critical or valid in the future, you can re-open it and reassess the verification stage.

-   Select **Monitor** when the risk assessment is not yet determined (e.g. a culture confirmation of cholera is still awaited).

-   Enter relevant **Comments** for the option chosen.

-   Click on **Submit**, the alert is closed, and the screen below appears:

![](media/image404.png){width="5.90833552055993in" height="3.033333333333333in"}

-   To review, click on **Review outcome**, and outcome-related information is visible on the screen.

-   Once you complete the process, unless you chose the **Monitor** option above, all alerts are switched from the **Open Alerts** list to the **Closed Alerts** list.

  ---------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![](media/image43.png){width="0.65625in" height="0.3541666666666667in"}   It is of paramount importance that EWARS administrative users (Account Administrators and Geographical Administrators) follow up each alert through verification, risk assessment, characterization and outcome. Alert management should not be neglected or stopped part-way through the process.

  ---------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 13.6 Re-opening closed alerts

Whenever the risk level changes or new information becomes available, you can re-open closed alerts. Closed alerts are alerts that are discarded, responded to or auto-discarded. For more information about auto-discarding alerts, refer to **Chapter 7. Alarms**, topic **7.4 Enabling auto-discard of an alert**.

The steps to re-open an alert are as follows.

-   Select **Menu** \> **Alert Log** \> **Closed Alerts**, and closed alerts are listed. Click on the **view** ![](media/image330.png){width="0.3333333333333333in" height="0.325in"} icon of an alert.

-   Click on **Re-Open Alert**, and the Re-Open dialogue box below opens:

![](media/image405.png){width="5.0in" height="1.84375in"}

-   Enter the reason for re-opening \> click on **Re-Open Alert**, and the alert is re-opened.

## 13.7 Configuring alert maps

Alert maps allow you to visualize open and closed alerts on a map. You can configure location type in alert maps to visualize various alerts triggered from different administrative level locations, such as province, state and so on.

### 13.7.1 Configuring a location type for the alerts map

-   Click on the **settings** ![](media/image406.png){width="0.24166666666666667in" height="0.25833333333333336in"} icon at the top right-hand corner \> click on ![](media/image407.png){width="0.6583333333333333in" height="0.20833333333333334in"}, and the screen below appears:

![](media/image408.png){width="5.6in" height="1.8416666666666666in"}

-   Select the location type (e.g. **Province**) to configure the alert map based on provinces. Click on **Save Change(s)**.

The following topic describes how to configure the alerts map based on provinces.

### 13.7.2 Viewing open alerts on a map

-   Select **Menu** \> **Alert log** \> **Alerts Map** \> click on **Open**, and the map is visible with province names and alert counts. Click on any province (e.g. Aimal), and alerts are visible, as shown below:

![](media/image409.png){width="5.86666447944007in" height="3.283333333333333in"}

### 13.7.3 Viewing closed alerts on a map

-   Select **Menu** \> **Alert log** \> **Alerts Map** \> click on **Closed**, and the map is visible with province names and alert counts. Click on any province (e.g. Aimal), and alerts are visible, as shown below:

> ![](media/image410.png){width="5.90833552055993in" height="3.316666666666667in"}

## 13.8 Exporting alert data

You can also export alert data to share it with other users. For more information on how to use the Export feature effectively, refer to **Chapter 23. Exports**, topic **23.3 Exporting alerts data**.

The following chapter explores the Data Import feature, which facilitates easy and smooth importing of data from other systems to EWARS.

# Chapter 14. Data Import

This chapter provides an overview of Data Import, a significant feature that can be utilized to import data collected in other systems into the Early Warning, Alert and Response System (EWARS) seamlessly. Using the Data Import feature, you can import different types of data -- related to historical diseases, outbreaks or information from laboratories. You can harness data to enhance your operational use of EWARS in line with situational objectives through this feature.

## 14.1 Data Import scenarios

Using the Data Import feature, you can import data to your account in comma-separated values (CSV) file format. The feature is useful in several scenarios, including the following:

-   when preloading your account with previously collected/historical data for the same context;

-   when data collected elsewhere (such as laboratory data or data from district health information software (DHIS)) are required to generate bulletins in EWARS;

-   when data reported via email or via storage media (such as CSV or Excel files) are required in the system.

## 14.2 Data Import prerequisites

To import data, you must have a matching EWARS form into which the data can be imported. If not, you should create one via the Forms feature. Refer to **Chapter 6. Forms**, topic **6.4 Creating a new form** for more information on creating a form.

You need to map the columns of the CSV file with the relevant fields of the form. To facilitate smooth import, you should create a form with appropriate response field options. For example, if a variable in the CSV file is binary, with two options (yes/no), you should create a select field (yes/no). For more information, refer to **Chapter 6. Forms**, topic **6.5.7 Configuring the select field**.

It is recommended that you have a clean and a well structured dataset before attempting to import data to the EWARS system.

  ---------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![](media/image43.png){width="0.65625in" height="0.3541666666666667in"}   Review the dataset you want to import carefully. Also, review all variables and the clean data, if required. Then create a form in EWARS that matches the variables of the dataset you want to import.

  ---------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The following topic explains the import process in more detail.

## 14.3 Importing data using a CSV file

To import data, follow the steps outlined in Fig. 14.1. Importing data is a four-step process.

1.  Create an import project by uploading a CSV/Excel file, and then edit it.

2.  Map \[Mandatory\] columns such as reporting location, reporting date and submitted date.

3.  Map the data columns of the CSV file with the form fields, matching the importing dataset with the existing data for harmonization.

4.  Validate, then validate and run the import.

![](media/image411.png){width="3.3816404199475065in" height="6.936699475065617in"}Fig. 14.1. Workflow to import data

**Step 1.** Create an import project by uploading a CSV file, and then edit it.

-   Select **Menu** \> **Data Import** \> click on the form name at the left-hand side (e.g. Event-Based Surveillance Form) \> click on **Upload CSV/Excel Sheet for new project**. Select a CSV file and double-click on it to upload it. A **New** **Import** **Project** is added, as shown below:

![](media/image412.png){width="6.427083333333333in" height="1.98124343832021in"}

-   Click on the **edit** ![](media/image413.png){width="0.31666666666666665in" height="0.3in"} icon of **New Import Project**, and the screen below appears:

![](media/image414.png){width="6.46875in" height="3.09375in"}

-   Enter a **Project name** (e.g. "EBS data for Nambutu") \> enter a **Description** (e.g. "Data for the year 2020"). Click on **Save Change(s)**.

**Step 2.** Map \[Mandatory\] columns such as reporting location, reporting date and submitted date.

To map the reporting location column, follow the steps below.

For the data import to be successful, the **reporting locations** must be present in the system before the import is performed. If you are trying to import data for an area or a location type that does not exist in the system, ensure to add locations, locations type prior to import (refer to **Chapter 3. Locations**, topic **3.2.3 Importing child locations in bulk via a** **CSV file** on adding reporting locations to the system).

EWARS needs to match the importing data with existing locations. It does this by matching one of the three options listed below:

-   the universally unique identifier (UUID)

-   the place code (PCODE)

-   the location name.

For example, if you select the UUID as the location match type, all data under a particular UUID will be saved under the same UUID in the system. The same applies for PCODE and location name.

-   Select a CSV file column with a reporting location identifier from the **Location Column** drop-down menu \> select an appropriate location matching the type from the **Location Match Type** drop-down menu.

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** if you are using location name as an identifier, there may be chances of name conflicts. These may arise, for instance, if there are any errors in the location name in the CSV file, or if this differs from the system's location name. In such cases, data will not be correctly matched to the system location, so it is recommended that you check location names or add a PCODE in the CSV file before importing it to the system.
  --------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-   Set **Override location type match** as **Yes** \> select type of location from the **Location type match** drop-down menu.

To map the reporting date column, follow the steps below.

-   Select a CSV file column with a reporting date from the **Report Date Column** drop-down menu.

-   Select the matching date format according to the reporting date column of the CSV file from the **Report Date Format** drop-down menu.

To map the report submission date column, follow the steps below.

-   Select a CSV file column with a **submitted date** from the **Submitted Date** **Column** drop-down menu.

-   Select the matching **date format** according to the submitted date column of the CSV file from the **Submitted Date** **Format** drop-down menu.

**Step 3.** Map the data columns of the CSV file with the form fields.

-   Select **Menu** \> **Administration** \> **Data Import**. Click on the form name, and a list of projects appears. Click on the **edit** ![](media/image307.png){width="0.35833333333333334in" height="0.3416666666666667in"} icon of your project, and the system lists all columns of the CSV file, as shown in the highlighted part below:

![](media/image415.png){width="6.322916666666667in" height="3.0613068678915134in"}

-   Click on the **expand** ![](media/image416.png){width="0.2833333333333333in" height="0.25in"} icon to expand the columns one by one, and the screen below appears:

![](media/image417.png){width="4.983333333333333in" height="1.225in"}

-   The **Target form field** contains all form fields and an **Ignore** option:

```{=html}
<!-- -->
```
-   **Either** select a matching form field from the **Target form field** drop-down menu to map an expanded CSV column with a selected form field

-   **Or** select the **Ignore** option from the **Target form field** drop-down menu, and the data for this ignored column will not be imported.

```{=html}
<!-- -->
```
-   Choose the **missing cell value replacement option** from the **Missing data plan** drop-down menu for empty cells in a CSV file.

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** a CSV row is equivalent to a report, and a cell value is equivalent to a field value.
  --------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-   **Set to Ignore Row**: in this option, if any cell of the CSV row is empty, then the entire row will not be imported.

-   **Set Zero (0)**: in this option, empty cells are replaced with **Zero (0)**.

-   **Set NULL**: in this option, empty cells are replaced with **Null** value.

**Step 4.** Validate, then validate and run the import.

-   Click on ![](media/image418.png){width="0.7in" height="0.31666666666666665in"} \> wait till validation is completed. Click on the ![](media/image419.png){width="0.575in" height="0.25in"} tab \> check whether the **Run State** is **Valid** or **Invalid**. Valid rows are ready to be imported.

-   Click on ![](media/image420.png){width="0.8583333333333333in" height="0.25833333333333336in"} \> click on **Confirm**, and **Invalid** record(s) remain in the **Data** tab. Successfully imported records are visible under the **Results** tab.

-   Click on the **Data** tab, and **Invalid** records that are not imported are visible.

The possible reasons for data being deemed **Invalid** are as follows:

-   **Data type mismatch** (e.g. the CSV column has textual data and the form field is numeric)

-   **Reporting location does not exist** in the system and needs to be added to the form

-   **Invalid or incorrect formatted date** in the reporting date and submitted date columns.

```{=html}
<!-- -->
```
-   Reimport the **Invalid** rows, if any \> delete all **Invalid** rows one by one under the **Data** tab. To delete a row, click on the **delete** ![](media/image421.png){width="0.20833333333333334in" height="0.23333333333333334in"} icon \> remove successfully imported rows from the CSV file and keep the invalid rows. Correct the invalid rows in the CSV file \> **Repeat steps 1 to 4** with the corrected CSV file.

To view the successfully imported reports under Report manager, follow the steps below.

-   Select **Menu** \> **Report manager**. Click on the form name \> you can check the form details, as shown below:

![](media/image422.png){width="6.48333552055993in" height="3.2in"}

## 14.4 Deleting an imported project

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image211.png){width="0.41060695538057745in" height="0.3875in"}**WARNING:**   Deleting an imported project will also delete all data imported from the project.
  --------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To view the records imported by the project, follow the steps below.

-   Select **Menu** \> **Data Import**. Click on the form name, and a list of projects appears \> click on the **edit** ![](media/image413.png){width="0.31666666666666665in" height="0.3in"} icon of the project \> click on the ![](media/image423.png){width="0.6166666666666667in" height="0.2833333333333333in"} tab, and the imported records appear.

To delete the project, follow the steps below.

-   Select **Menu** \> **Administration** \> **Data Import** \> click on form name \> list of projects appears \> click on the **delete** ![](media/image424.png){width="0.275in" height="0.2833333333333333in"} icon \> click on **Confirm**. All the data imported by the project and the project are deleted.

## 14.5 Importing a sample CSV file for the event-based surveillance form

The sample CSV file needs to match the event-based surveillance form of the Model account, as shown below:

![](media/image425.png){width="5.98333552055993in" height="2.05in"}

The event-based surveillance form fields are:

-   Submitted date

-   Report date

-   Location PCODE

-   Source of the report

-   Event reported

-   Hazard Type

-   Type of event

-   Human -- Cases

-   Human -- Deaths

-   Animal -- Cases

-   Animal -- Deaths

To import the sample CSV file, follow the steps below.

-   Download the sample CSV file from this link: [[https://ewarscontent.s3.ap-south-1.amazonaws.com/\_0464f6fd1cc8/data%20import/ebs_csv/data%20import.csv]{.underline}](https://ewarscontent.s3.ap-south-1.amazonaws.com/_0464f6fd1cc8/data%20import/ebs_csv/data%20import.csv)

-   Create an import project with the sample CSV file, and then edit it.

-   Select **Menu** \> **Data Import** \> click on **Event-Based Surveillance Form** \> click on **Upload CSV/Excel Sheet** for the new project. Select the CSV file and double-click on it to upload it. A **New Import Project** is added, as shown below:

![](media/image426.png){width="5.94166447944007in" height="1.65in"}

-   Click on the **edit** ![](media/image413.png){width="0.31666666666666665in" height="0.3in"} icon of **New Import Project**, and the screen below appears:

![](media/image414.png){width="6.46875in" height="3.09375in"}

-   Enter a **Project name** (e.g. "EBS data for Nambutu") \> enter a **Description** (e.g. "Data for the year 2020"). Click on **Save Change(s)**.

To map the reporting location column, follow the steps below.

-   Select **Location PCODE** from the **Location Column** drop-down menu \> select **PCODE** from the **Location Match Type** drop-down menu.

To map the reporting date column, follow the steps below.

-   Select **Report date** from the **Report Date Column** drop-down menu.

-   Select ISO8601 2017-12-31 (%Y-%m-%d) from the **Report Date Format** drop-down menu.

To map the report submission date column, follow the steps below.

-   Select **Submitted date** from the **Submitted Date Column** drop-down menu.

-   Select **ISO8601 2017-12-31 (%Y-%m-%d)** from the **Submitted Date Format** drop-down menu.

To map the data columns, follow the steps below.

-   To map **Animal -- Cases** with the form field, look for **Animal -- Cases** at the right-hand side and click on the **expand** ![](media/image427.png){width="0.2833333333333333in" height="0.25833333333333336in"} icon \> select the **Cases and Deaths \\ Animal Deaths \\ Cases \[text\]** field from the **Target form field** drop-down menu, and the screen below appears:

![](media/image417.png){width="4.983333333333333in" height="1.225in"}

-   Set the **Missing data plan** drop-down menu as **Set Zero (0)** -- this will set zero (0) in **Animal -- Cases** if the cell is empty.

-   To map **Animal -- Deaths** with the form field, look for **Animal -- Deaths** at the right-hand side and click on the **expand** ![](media/image427.png){width="0.2833333333333333in" height="0.25833333333333336in"} icon \> select the **Cases and Deaths \\ Animal Deaths \\ Deaths \[text\]** field from the **Target form field** drop-down menu, and the screen below appears:

![](media/image428.png){width="5.0in" height="1.2916666666666667in"}

-   Set the **Missing data plan** drop-down menu as **Set Zero (0)** -- this will set zero (0) in **Animal -- Deaths** if the cell is empty.

-   To map **Event reported** with the form field, look for **Event reported** at the right-hand side and click on the **expand** ![](media/image427.png){width="0.2833333333333333in" height="0.25833333333333336in"} icon \> select the **Describe the event being reported: \[text area\]** field from the **Target form field** drop-down menu, and the screen below appears:

![](media/image429.png){width="4.983333333333333in" height="1.35in"}

-   Set the **Missing data plan** drop-down menu as **Set NULL** -- this will set NULL in **Event reported** if the cell is empty.

-   To map **Hazard Type** with the form field, look for **Hazard Type** at the right-hand side and click on the **expand** ![](media/image427.png){width="0.2833333333333333in" height="0.25833333333333336in"} icon \> select the **What is the likely hazard type? \[select\]** field from the **Target form field** drop-down menu, and the screen below appears:

![](media/image430.png){width="4.958333333333333in" height="1.1583333333333334in"}

-   To map **Human -- Deaths** with the form field, look for **Human -- Deaths** at the right-hand side and click on the **expand** ![Inserting image\...](media/image427.png){width="0.2833333333333333in" height="0.25833333333333336in"} icon \> select the **Cases and Deaths \\ Human \\ Deaths \[text\]** field from the **Target form field** drop-down menu, and the screen below appears:

![](media/image431.png){width="6.197915573053368in" height="1.53125in"}

-   Set the **Missing data plan** drop-down menu as **Set Zero (0)** -- this will set zero (0) in **Human -- Deaths** if the cell is empty.

-   To map **Human -- Cases** with the form field, look for **Human -- Cases** at the right-hand side and click on the **expand** ![](media/image427.png){width="0.2833333333333333in" height="0.25833333333333336in"} icon \> select the **Cases and Deaths \\ Human \\ Cases \[text\]** field from the **Target form field** drop-down menu, and the screen below appears:

![](media/image432.png){width="6.322915573053368in" height="1.4479166666666667in"}

-   Set the **Missing data plan** drop-down menu as **Set Zero(0)** -- this will set zero in **Human -- Cases** if the cell is empty.

-   To map **Location PCODE** with the form field, look for **Location PCODE** at the right-hand side and click on the **expand** ![](media/image427.png){width="0.2833333333333333in" height="0.25833333333333336in"} icon \> select the **Ignore** field from the **Target form field** drop-down menu, and the screen below appears:

![](media/image433.png){width="5.375in" height="1.1666666666666667in"}

To map **Report date** with the form field, look for **Report date** at the right-hand side and click on the **expand** ![](media/image427.png){width="0.2833333333333333in" height="0.25833333333333336in"} icon \> select the **Ignore** field from the **Target form field** drop-down menu, and the screen below appears:

![](media/image434.png){width="5.29166447944007in" height="1.125in"}

-   To map **Source of the report** with the form field, look for **Source of the report** at the right-hand side and click on the **expand** ![](media/image427.png){width="0.2833333333333333in" height="0.25833333333333336in"} icon \> select the **Source of the report? \[select\]** field from the **Target form field** drop-down menu, and the screen below appears:

![](media/image435.png){width="5.0in" height="1.0833333333333333in"}

-   To map **Submitted date** with the form field, look for **Submitted date** at the right-hand side and click on the **expand** ![](media/image427.png){width="0.2833333333333333in" height="0.25833333333333336in"} icon \> select the **Ignore** field from the **Target form field** drop-down menu, and the screen below appears:

![](media/image436.png){width="5.125in" height="1.125in"}

-   To map **Type of the event** with the form field, look for **Type of the event** at the right-hand side and click on the **expand** ![](media/image427.png){width="0.2833333333333333in" height="0.25833333333333336in"} icon \> select the **What is the type of event? \[select\]** field from the **Target form field** drop-down menu, and the screen below appears:

![](media/image437.png){width="4.966666666666667in" height="1.2166666666666666in"}

-   Once all columns are mapped, click on **Save Change(s)**.

To validate and import the CSV file, follow the steps below.

-   Click on ![](media/image418.png){width="0.7in" height="0.31666666666666665in"} \> wait until validation is completed. Click on the ![](media/image419.png){width="0.575in" height="0.25in"} tab, and the screen below appears, with **VALID** in the **Run State** column:

![](media/image438.png){width="6.0in" height="1.9166666666666667in"}

-   Click on ![](media/image420.png){width="0.8583333333333333in" height="0.25833333333333336in"} \> click on **Confirm**, and successfully imported record(s) are visible under the **Results** tab. Click on **Completed**.

To view the import data under Report manager, follow the steps below.

-   Select **Menu** \> **Report manager**. Click on **Event-Based Surveillance Form**, and the record is visible, as shown below:

![](media/image439.png){width="6.225in" height="2.8916666666666666in"}

The screenshot above shows all the successfully imported records.

The following chapters will help you plot data within EWARS effectively for visual analysis, presentations and summaries.

#  

# PART IV. Data analysis, visualization and dissemination

[Part III addressed the Data Collection and Monitoring features. Part IV focuses on analysing data collected in]{.mark} the Early Warning, Alert and Response System ([EWARS) for dissemination with useful features such as Plot, Mapping, Widgets, Notebooks and more (Fig. IV.1). Using these, you can visualize your data and take necessary action. Further, you can disseminate key information visually by downloading or sharing it with users in various formats.]{.mark}

Fig. IV.1. Data analysis, visualization and dissemination elements

![](media/image440.png){width="3.8958333333333335in" height="5.0in"}

**\
**

# Chapter 15. Plot

Plot is a key Early Warning, Alert and Response System (EWARS) feature that facilitates easy analysis and visualization of data within the system via various chart types without any additional software support. Using this feature, administrative users (Account Administrators and Geographical Administrators) can easily provide data for common emergency reports, presentations or summaries in a visual format for research, monitoring, annual comparisons and further analysis needs.

  ---------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------
  ![](media/image43.png){width="0.65625in" height="0.3541666666666667in"}   You [cannot save charts within plot. Once you complete a chart, you need to download it and save it in your own drives for further use.]{.mark}

  ---------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------

It supports the following chart types (Fig. 15.1).

Fig. 15.1. Chart types supported

![](media/image441.png){width="7.072049431321084in" height="7.9872550306211725in"}

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** both the data and the related indicators need to be defined in the system to plot a chart.
  --------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 15.1 Defining settings for various chart types

Follow the instructions below to plot different chart types.

-   Select **Menu** \> **Analysis** \> **Plot**, and the screen below appears:

![](media/image442.png){width="6.725775371828521in" height="3.012587489063867in"}

The three highlighted parts in the above figure are as follows.

**Part 1: Settings** -- this helps you define chart components once you decide the chart type.

**Part 2: Data** -- this lets you use data available in the system based on the indicators.

**Part 3: Chart rendering area** -- this is the area where the plot is developed.

By default, the **Settings** tab (Part 1 in the screenshot) is open. Follow the steps below to plot a chart.

-   Select a **Chart Type** that is to be generated from the drop-down menu (e.g. **Time Series**).

-   Populate the **Chart Title** field to give a title to appear at the top of the chart.

-   Populate the **X Axis title** field to give a title to the horizontal axis of the chart; this is displayed below the X axis.

-   Populate the **Y Axis title** field to give a title to the vertical axis of the chart; this is displayed to the side of the Y axis.

-   Set **Show legend** as **Yes** if you want legends on the chart; these help you to differentiate variables in the chart, as shown below:

> ![](media/image443.png){width="4.65in" height="2.3833333333333333in"}

-   Set **Show slices with no data** as **Yes** if you want to display a graph that includes data with zero value, as shown below:

> ![](media/image444.png){width="2.6416666666666666in" height="2.55in"} ![](media/image445.png){width="2.7916666666666665in" height="2.5166666666666666in"}

-   Select the **Location** for which you want to generate the chart.

-   Select a **Group By** field; this allows you to group data based on **Time Interval**, **Location** or **Indicators**, according to your requirements. (The **Indicators** option in **Group By** is only available for **Pie** and **Pyramid** charts).

```{=html}
<!-- -->
```
-   To group by **Time Interval**, select a suitable interval (e.g. Daily, Weekly, Monthly or Yearly) from the drop-down menu. If the selection is Weekly, for example, the chart is produced with weekly aggregated data. The X axis of the chart will show the week number and the Y axis will show the indicator data count.

-   To group by **Location**, select a suitable location type (e.g. Province or District). If the selection is Province, for example, the chart is rendered against aggregated provincial data. The X axis of the chart will show the provinces and the Y axis will show the indicator data count.

-   To group by **Indicators** (option available for Pie and Pyramid charts only), a slice is shown for each added indicator. If you have added three indicators in the pie chart, for example, three slices of the pie chart are visible.

```{=html}
<!-- -->
```
-   Set **Compare Years** as **Yes** if you want to compare data from multiple years for selected periods. Once you set **Compare Years** as **Yes**, you need to populate the **Select years to compare** field (e.g. 2019, 2020 and 2021), as show below:

> ![](media/image446.png){width="3.9791666666666665in" height="2.875in"}

-   Select the **Start date** and **End date** in the calendar, as shown below:

> ![](media/image447.png){width="3.9270833333333335in" height="1.5in"}

-   Click on the ![](media/image448.png){width="0.7in" height="0.25833333333333336in"} tab (Part 2 in the screenshot) \> click on the **add** ![](media/image449.png){width="0.31666666666666665in" height="0.2833333333333333in"} icon to add an indicator data series, and the screen below appears:

> ![](media/image450.png){width="4.233333333333333in" height="0.9583333333333334in"}

How to use data is addressed under each chart type topic below.

-   Once you input the data above, the chart is created automatically in the Chart rendering area (Part 3 in the screenshot).

## 15.2 Plotting data on a time series chart

The time series chart is a line chart. This guide uses the following two examples to demonstrate how to plot data on a time series for the fictional country Nambutu.

**Example 1.** Plot provincial total acute watery diarrhoea cases for Nambutu for 2020.

-   Select **Menu** \> **Analysis** \> **Plot**. Set **Chart** **Type** as **Time Series** \> enter "Acute Watery Diarrhoea Cases in 2020" as the **Chart Title** \> enter "Province" as the **X Axis title** \> enter "Cases" as the **Y Axis title** \> set **Show legend** as **Yes**, set **Show slices with no data** as **Yes** \> select the location **Nambutu** \> set **Group By** as **Location** \> set **Location type** as **Provinces** \> set **Compare Years** as **No** \> select the **Start date** 2020-01-01 in the calendar \> select the **End date** 2020-12-31 in the calendar.

-   Click on the **Data** tab \> click on the **add** ![](media/image449.png){width="0.31666666666666665in" height="0.2833333333333333in"} icon \> select the **Indicator** (e.g. **Acute Watery Diarrhoea (AWD) Total**).

The chart is generated, as shown below:

![](media/image451.png){width="5.0in" height="2.75in"}

The blue line represents total AWD cases in 2020, and it is plotted against provinces in Nambutu.

**Example 2.** Plot and compare provincial total acute watery diarrhoea cases for Nambutu for the years 2019 and 2020.

-   Select **Menu** \> **Analysis** \> **Plot**. Set **Chart Type** as **Time Series** \> enter "Acute Watery Diarrhoea Cases in in 2019 & 2020" as the **Chart Title** \> enter "Province" as the **X Axis title** \> enter "Cases" as the **Y Axis title** \> set **Show legend** as **Yes** \> set **Show slices with no data** as **Yes** \> select the location **Nambutu** \> set **Group By** as **Location** \> set **Location type** as **Provinces** \> set **Compare Years** as **Yes** \> select the years **2019** and **2020** \> select the **Start date** Jan 01 in the calendar \> select the **End date** Dec 31 in the calendar.

-   Click on the **Data** tab \> click on the **add** ![](media/image449.png){width="0.31666666666666665in" height="0.2833333333333333in"} icon \> select **Acute Watery Diarrhoea (AWD) Total**.

The chart is generated, as shown below:

![](media/image452.png){width="5.0in" height="2.7083333333333335in"}

The blue line represents total AWD cases in 2020 and the black line represents total AWD cases in 2019, plotted against provinces in Nambutu.

## 15.3 Plotting data on a pie chart

A pie chart is a categorical chart type. It displays data in different slices, enabling you to plot suitable scenarios. For demonstration purposes, this guide uses the following example.

**Example 1.** Plot total measles cases by health facility from 1 June 2020 to 13 December 2020.

-   Select **Menu** \> **Analysis** \> **Plot**. Set **Chart Type** as **Pie** \> enter "Total Measles Cases" as the **Chart Title** \> set **Show legend** as **Yes** \> set **Show slices with no data** as **No** \> select the location **Nambutu** \> set **Group By** as **Location** \> set **Location type** as **Health Facility** \> set **Compare Years** as **No** \> select the **Start date** 2020-06-01 in the calendar \> select the **End date** 2020-12-31 in the calendar.

-   Click on the **Data** tab \> click on the **add** ![](media/image449.png){width="0.31666666666666665in" height="0.2833333333333333in"} icon \> select **Health** \> **Morbidity** \> **Measles** \> **Measles Total**.

The chart is generated, as shown below:

![](media/image453.png){width="5.49166447944007in" height="2.783333333333333in"}

## 15.4 Plotting data on a bar chart

A bar chart helps you represent categorical data with rectangular bars, the heights/lengths of which are proportional to the values they represent. This guide uses the following example to demonstrate this.\
**\
Example 1.** Plot provincial total acute watery diarrhoea cases for Nambutu from 1 January 2020 to 31 December 2020.

-   Select **Menu** \> **Analysis** \> **Plot**. Set **Chart Type** as **Bar** \> enter "Acute Watery Diarrhoea cases in 2020" as the **Chart Title** \> enter "Province" as the **X Axis title** \> enter "Cases" as the **Y Axis title** \> set **Show legend** as **Yes** \> set **Show slices with no data** as **Yes** \> select the location **Nambutu** \> set **Group By** as **Location** \> set **Location type** as **Provinces** \> set **Compare Years** as **No** \> select the **Start date** 2020-01-01 in the calendar \> select the **End date** 2020-12-31 in the calendar.

-   Click on the **Data** tab \> click on the **add** ![](media/image449.png){width="0.31666666666666665in" height="0.2833333333333333in"} icon and select the **Indicator** you want to plot (e.g. **Acute Watery Diarrhoea (AWD) Total**).

The chart is generated, as shown below:

![](media/image454.png){width="4.975in" height="2.675in"}

## 15.5 Plotting data on a stacked bar chart

A stacked bar chart is a chart type with rectangular bars used to break down and compare parts of a whole. Each rectangular bar stands for the whole, while segments within the bar denote different parts of the whole. For demonstration purposes, this guide uses the following example.

**\
Example 1.** Plot and compare total cholera cases for Nambutu by province for 2019 and 2020.

-   Select **Menu** \> **Analysis** \> **Plot**. Set **Chart Type** as **Stacked Bar** \> enter "Cholera Cases" as the **Chart Title** \> enter "Province" as the **X Axis title** \> enter "Cases" as the **Y Axis title** \> set **Show legend** as **Yes** \> set **Show slices with no data** as **Yes** \> select the location **Nambutu** \> set **Group By** as **Location** \> set **Location type** as **Provinces** \> set **Compare Years** as **Yes** \> select years **2019** and **2020** \> select the **Start date** Jan 01 in the calendar \> set the **End date** Dec 31 in the calendar.

-   Click on the **Data** tab \> click on the **add** ![](media/image449.png){width="0.31666666666666665in" height="0.2833333333333333in"} icon \> select **Health** \> **Morbidity** \> **Cholera** \> **Cholera Total**.

The chart is generated, as shown below:

![](media/image455.png){width="5.49166447944007in" height="2.716666666666667in"}

## 15.6 Plotting data on a pyramid chart

A pyramid chart represents data in the shape of a triangle or pyramid. These are best used when the data need to be organized hierarchically. For demonstration purposes, this guide uses the following example.**\
\
Example 1.** Plot total measles cases data, total cholera cases data, total acute watery diarrhoea cases data and total acute bloody diarrhoea cases data for Nambutu for 2019 and 2020.

-   Select **Menu** \> **Analysis** \> **Plot**. Set **Chart Type** as **Pyramid** \> enter "Overall cases for 2019 & 2020" as the **Chart Title** \> set **Show legend** as **Yes** \> set **Show slices with no data** as **Yes** \> select the location **Nambutu** \> set **Group By** as **Indicators** \> set **Compare Years** as **Yes** \> select years **2019** and **2020** \> select the **Start date** Jan 01 in the calendar \> select the **End date** Dec 31 in the calendar.

-   Click on the **Data** tab \> click on the **add** ![](media/image449.png){width="0.31666666666666665in" height="0.2833333333333333in"} icon \> select **Health** \> **Morbidity** \> **Measles** \> **Measles Total** \> click on the **add** ![](media/image449.png){width="0.31666666666666665in" height="0.2833333333333333in"} icon \> select **Cholera Total cases** \> click on the **add** ![](media/image449.png){width="0.31666666666666665in" height="0.2833333333333333in"} icon \> select **Health** \> **Morbidity** \> **Acute Bloody Diarrhoea** \> **Acute Bloody Diarrhoea Total cases** \> click on the **add** ![](media/image449.png){width="0.31666666666666665in" height="0.2833333333333333in"} icon \> select **Health** \> **Morbidity** \> **Acute Watery Diarrhoea** \> **Acute Watery Diarrhoea Total cases**.

The chart is generated, as shown below:

![](media/image456.png){width="4.883333333333334in" height="4.958333333333333in"}

## 15.7 Plotting data on a tabular report chart

A tabular report is used to represent data in a table format. This format is useful because the data can be divided into different categories for easy analysis. For demonstration purposes, this guide uses the following example.**\
\
Example 1.** Plot provincial total cholera cases data for Nambutu for 2020.

-   Select **Menu** \> **Analysis** \> **Plot**. Set **Chart Type** as **Tabular Report** \> enter "Cholera Cases" as the **Chart Title** \> select the location **Nambutu** \> set **Group By** as **Location** \> set **Location type** as **Provinces** \> set **Compare Years** as **No** \> select the **Start date** 2020-01-01 in the calendar \> select the **End date** 2020-12-31 in the calendar.

-   Click on the **Data** tab \> click on the **add** ![](media/image449.png){width="0.31666666666666665in" height="0.2833333333333333in"} icon and select the desired indicator from the drop-down menu (e.g. **Total cholera cases**).

The chart is generated, as shown below:

![](media/image457.png){width="5.46666447944007in" height="1.925in"}

## 15.8 Downloading a chart as a PDF file

You can download any chart as a PDF file by clicking on the **download** ![](media/image458.png){width="0.35833333333333334in" height="0.2916666666666667in"} icon at the top of the generated chart.

The following chapter explores the Mapping feature, using which you can represent EWARS data on a map.

**\
**

# Chapter 16. Mapping

The Mapping feature facilitates representation of Early Warning, Alert and Response System (EWARS) data on a map. You can download EWARS maps easily and use them for data presentations, reports or sharing via links.

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** the Mapping feature and the map widget are two different mapping facilities provided in EWARS. The Mapping feature allows you to represent the data for different locations in the form of multiple layers on a map. This cannot be incorporated into dashboards, bulletins, notebooks or websites. The map widget, on the other hand, cannot represent data in the form of multiple layers but can be used in dashboards, bulletins, notebooks and websites.
  --------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

For more information on the map widget, refer to **Chapter 17. Widgets and their configuration**, topic **17.16 Map widget**.

Fig. 16.1 shows the different types of maps that can be produced with the Mapping feature in EWARS.

Fig. 16.1. Types of maps EWARS can produce

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 1.  **Single location**                                                                                                                                                                                                                                     | 2.  **Point map**                                                                                                                                                                                                                                | 3.  **Same types of locations**                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                              |
| ![https://lh4.googleusercontent.com/X0ZVLZnmbCoX5Qij-BKSnquL5EsaK_Im1amOJQQbGTD2ZSIyoUtpHjy3IJ3EAbS7fuAcCmCW1YDANC5Q_fNYaO2cuz3cLKYwU1y0NTe-2WVuJrAHUPGzGtWI0YNb8b23ElCvsOUo](media/image459.png){width="2.0in" height="1.7916666666666667in"}     | ![https://lh5.googleusercontent.com/f_oRX3jU_0eie8bFBJ4hohfwpYy4YbJSbcK42TL_j9S2QBSrlBaFDtS4IdVis-ms5PbR6736JsMTfXOxUtnITgr6K-r3Qiv6MvvAfWGsAjFZXPgrpeqkH2xErb12bAdoB185TpvB](media/image460.png){width="2.0in" height="1.78125in"}     | ![https://lh6.googleusercontent.com/vVlqTyi60Dq3SWFhJM6XzjXFKZyA0xciL6OWxLULQA9C_VrQgsIplPmSXaupSh_Wx3a44_gUUfILzxKDlBmrpf7nwmX8Sj3F4jGMtfQVS6k1bk9VX3QKT-slGftwPZ_dPCDkyh6c](media/image461.png){width="2.0in" height="1.78125in"} |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 4.  **Group of locations**                                                                                                                                                                                                                                  | 5.  **Multilayer map**                                                                                                                                                                                                                           | 6.  **Alerts map**                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                              |
| ![https://lh3.googleusercontent.com/JcHYHRewhjfNnY4bVWBKY63yZfmJULgkZdtSeyDIBB1MKFMsaXLsJGAzUcsTJyYdNEKJfAqRXOTM8Uee1zsyB_oKC-z-qroMeZMOxFH1YynxUEjtzgjmuBsmx8mQsV8X9Vs1itiV](media/image462.png){width="2.03125in" height="1.7916666666666667in"} | ![https://lh6.googleusercontent.com/rncI_E4_zwqk-hY39XQycFEW6ABlOtNSwFzUfyfpck7_LFBeZcSgD5ZjYxYlXIEfkWi2lOTtbuqjGlM8WghShleaiFGbcUrVBx8-slbhF0ODCedV8E58UwPraPNliDft_I9Q1i1r](media/image463.png){width="1.90625in" height="1.78125in"} | ![https://lh6.googleusercontent.com/y-ZZnXFtRQW8vDESbn6OMC9n7KU0bpDETgFYsUFI3ItHQHeKfLNS3I3c5d2zA4Odopt2sThESDjeVUJiDXwpLC1kU2Sk9HVrAC2HmjiUmV9lr7nz0s8dEfzp7wvSZrlSVvHn74dN](media/image464.png){width="2.0in" height="1.75in"}    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

## 16.1 Creating a new map

  ---------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![](media/image43.png){width="0.65625in" height="0.3541666666666667in"}   EWARS provides you with a base map on which you can overlay data from the system. You need to have country GeoJson data in the system before configuring the map.

  ---------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------

Follow the instructions below to create a new map.

-   Select **Menu** \> **Mapping** \> **Create New**, and the screen below appears:

> ![](media/image465.png){width="7.0in" height="2.3in"}

Part 1 of the screenshot above shows the configuration options for maps. As you configure the fields in this section, the map is displayed on the base map shown as Part 2.

Configuration of a map (in Part 1) has three steps:

-   **Settings** -- configuring general settings

-   **Layers** -- adding layers to the map

-   **Default** -- setting the default map position.

**Step 1.** Configure general settings.

-   **Title:** enter the map title (e.g. "Geographical distribution of Cholera alerts in 2021").

-   **Shared:** by default, no map is shared with others; it is not visible to other users as well. Once the option is set to **Shared**, it is shared with other users and visible under **Shared maps**. Select your preferred option.

-   **Access:** by default, the access type is **Private**; you cannot access the map outside the system. Once the option is set as **Public**, if required, you can access the map externally with the help of a link. Select your preferred access type.

**Step 2.** Add layers to the map.

Mapping allows you to add multiple layers to a single map. Each map layer displays a specific geographical dataset. Follow the steps below to add a layer.

-   Click on **Layers** \> click on the **add** ![](media/image466.png){width="0.36666666666666664in" height="0.25833333333333336in"} icon to add a new layer, and the **Layers** screen below appears:

![](media/image467.png){width="6.322915573053368in" height="3.4791666666666665in"}

The layers screen consists of five sections: visualization, data source, thresholds, style and labels.

**1. Visualization**

-   **Layer title**: enter a **Layer title**, which is displayed as the legend name on the map (e.g. "No. of cholera alerts in Country X").

-   **Visualization:** set the **Visualization** according to your needs from the options below:

```{=html}
<!-- -->
```
-   **Single Location:** this lets you select a single **location** from the location drop-down menu, which is rendered on the map.

-   **Locations of Group:** this lets you select a **location group**, and all the locations of the selected group are rendered on the map.

-   **Locations of type:** this lets you select a **Location** and a **Location type** (for example, if the **Location** is set as Province X and the **Location type** is set as Health Facility, all health facilities in Province X are rendered on the map).

For more information regarding configuration of locations and location types, refer to **Chapter 3. Locations**.

-   **Collected Lat/Long:** this lets you select a form with a field for global positioning system (GPS) coordinates. Select the **Form** and then the **Lat/long field** \> select the **From** and **To** dates. The data from the reported fields will make the map layer, in this case as a point locations.

-   **Alerts Map**: this lets you select an **Alarm**, select a **Dimension/alarm status** and select **From** and **To** dates. Alerts triggered by the selected alarm between the dates are rendered on the map.

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** you don't need to configure the data source and thresholds sections for the visualization types collected lat/long and alerts map.
  --------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**2**. **Data source**

-   **Data source:** set the **Data source** according to your needs from the options below:

```{=html}
<!-- -->
```
-   **Indicator:** set **Data Source** as **Indicator** \> select the indicator \> select **From** and **To** dates in the calendar.

-   **Formula**: input the formula you want to use (e.g. Diarrhoea = total AWD + total cholera). Once you have stated the formula name, select each variable (e.g. total AWD or total cholera) and select the appropriate indicator under each variable \> click on **Add Variable** \> click on the **edit** ![](media/image468.png){width="0.2916666666666667in" height="0.25in"} icon \> enter a **Variable Name** () \> select the **Indicator** \> click on **Add Variable** again \> click on the **edit** ![](media/image468.png){width="0.2916666666666667in" height="0.25in"} icon \> enter another **Variable Name** \> select the correct indicator \> select the **From** and **To** dates in the calendar.

**3. Threshold**

-   Click on the **add** ![](media/image466.png){width="0.36666666666666664in" height="0.25833333333333336in"} icon to add a threshold value \> enter a range (e.g. "0" to "50").

-   Select a colour for the threshold from the drop-down menu.

-   Repeat the steps above to add more thresholds

-   **Show Legends**: by default, legends are hidden. Once you select **Yes**, legend information is visible.

-   **Legend Position**: by default, the legend information is displayed at the bottom right-hand position of the map. Select your preferred legend position from the available options.

    The screenshot below shows how different thresholds are displayed in the legend:

![](media/image469.jpg){width="5.0in" height="2.96875in"}

**4. Style**

-   Choose the **Stroke Colour** to set the border colour (the default is black) \> enter the **Stroke Width** to set the border size (the default is 5) \> choose the **Fill colour** to set the background colour (the default is white) \> enter a **Fill opacity** of between 0.0 and 1.0 (the default is 1) \> select the **Marker type** (the default is a circle) \> enter the **Marker size** (the default is 10).

**5. Labels**

Labels display the count and name of the location. Set them according to your needs from the options below:

-   Select the **Label type** from the drop-down menu (the default is Numbered) \> choose the **Label colour** (the default is black) \> enter the label size (the default is 10).

    The screenshot below shows how the point locations appear with numbered labels:

![](media/image470.jpeg){width="3.564583333333333in" height="2.2278641732283466in"}

-   Click on the **apply** ![](media/image471.png){width="0.36666666666666664in" height="0.3416666666666667in"} icon to apply the changes you have made. The layer is saved with the name given in the layer title.

You can modify the layers after saving. All added layers are displayed under **Layers**, in the settings.

To edit a layer, click on the **edit** ![](media/image472.png){width="0.2833333333333333in" height="0.275in"} icon \> apply the changes, and the layer is edited.

To delete a layer, click on the **delete** ![Inserting image\...](media/image280.png){width="0.21875in" height="0.20833333333333334in"} icon \> apply the changes, and the layer is deleted.

-   Repeat the actions above within **Step 2** to add more layers.

**Step 3.** Set the default map position.

-   Click on the map position \> zoom in and out to identify the position of your context.

-   Click on **Set Position**, and the map position is set.

-   Click on the **save** ![](media/image473.png){width="0.35833333333333334in" height="0.325in"} icon to save the map, and the map is rendered.

## 16.2 Mapping data for a particular location

For demonstration purposes, this guide uses the following example.

**Example 1.** Map total measles cases for Nambutu for 2018.

**Step 1.** Configure general settings.

-   Select **Menu** \> **Analysis** \> **Mapping** \> **Create New** \> enter a **Title** (e.g. "Measles Total").

**Step 2.** Add a **Layer** for total measles cases.

-   Select **Layers** \> click on the **add** ![](media/image474.png){width="0.3in" height="0.25833333333333336in"} icon.

-   Under **Visualization**, enter "Measles Total" as the **Layer title** \> set **Visualization** as **Single location** \> select the **Location** Nambutu.

-   Under **Data source**, set **Data source** as **Indicator** \> select the **Indicator** (e.g. Measles Total) \> set **From** as 2018-01-01 in the calendar \> set **To** as 2018-12-31 in the calendar.

-   Under **Thresholds**, click on the **add** ![](media/image475.png){width="0.2916666666666667in" height="0.25833333333333336in"} icon \> enter "0" to "10000", choose ![](media/image476.png){width="0.2in" height="0.2in"} \> click on the **add** ![](media/image475.png){width="0.2916666666666667in" height="0.25833333333333336in"} icon again \> enter "10001" to "20000", choose ![](media/image477.png){width="0.2in" height="0.2in"} \> click on the **add** ![](media/image475.png){width="0.2916666666666667in" height="0.25833333333333336in"} icon again \> enter "20001" to "30000", choose ![](media/image478.png){width="0.2in" height="0.2in"}.

-   Under **Style**, set **Stroke Colour** as ![](media/image479.png){width="0.15833333333333333in" height="0.15833333333333333in"} \> set **Stroke Width** as 2 \> set **Fill colour** as ![](media/image480.png){width="0.2in" height="0.2in"} \> set **Fill opacity** as 0.9.

-   Under **Labels**, set **Label type** as Numbered \> set **Label colour** as ![](media/image479.png){width="0.15833333333333333in" height="0.15833333333333333in"} \> click on the **apply** ![](media/image481.png){width="0.275in" height="0.25833333333333336in"} icon.

**Step 3.** Set the default map position.

-   Select **Default** \> drag the map to your desired location \> click on **Set position**.

-   Click on the **save** ![](media/image482.png){width="0.325in" height="0.2833333333333333in"} icon, and the map below is shown:

![](media/image483.jpeg){width="5.0in" height="3.0625in"}

## 16.3 Mapping data for a particular type of location

For demonstration purposes, this guide uses the following two examples.

**Example 1.** Map total measles data by province for Nambutu for 2020.

**Step 1.** Configure general settings.

-   Select **Menu** \> **Analysis** \> **Mapping** \> **Create New** \> enter a **Title** (e.g. "Measles Total").

**Step 2.** Add a layer for measles case data

-   Select **Layers** \> click on the **add** ![](media/image474.png){width="0.3in" height="0.25833333333333336in"} icon.

-   Under **Visualization**, enter "Measles Total" as the **Layer title** \> set **Visualization** as **Locations of type** \> select the **Location** Nambutu \> select Provinces as the **Location type**.

-   Under **Data source**, set **Data source** as **Indicator**\> select the **Indicator** (e.g. Measles Total) \> set **From** as 2020-01-01 in the calendar \> set **To** as 2020-12-31 in the calendar.

-   Under **Thresholds**, click on the **add** ![](media/image475.png){width="0.2916666666666667in" height="0.25833333333333336in"} icon \> enter "0" to "1000", choose ![](media/image484.png){width="0.2in" height="0.2in"} \> click on the **add** ![](media/image475.png){width="0.2916666666666667in" height="0.25833333333333336in"} icon again \> enter "1001" to "2000", choose ![](media/image485.png){width="0.2in" height="0.2in"}, click on the **add** ![](media/image475.png){width="0.2916666666666667in" height="0.25833333333333336in"} icon again \> enter "2001" to "3000", choose ![](media/image486.png){width="0.2in" height="0.2in"} \> click on the **add** ![](media/image475.png){width="0.2916666666666667in" height="0.25833333333333336in"} icon again \> enter "3001" to "4000", choose ![](media/image487.png){width="0.2in" height="0.2in"} \> click on the **add** ![](media/image475.png){width="0.2916666666666667in" height="0.25833333333333336in"} icon again \> enter "4001" to "5000", choose ![](media/image488.png){width="0.2in" height="0.2in"}.

-   Under **Style**, set **Stroke colour** as ![](media/image479.png){width="0.15833333333333333in" height="0.15833333333333333in"} \> set **Stroke width** as 2 \> set **Fill colour** as ![](media/image480.png){width="0.2in" height="0.2in"} \> set **Fill opacity** as 0.8.

-   Under **Labels**, set **Label type** as Numbered \> set **Label colour** as ![](media/image479.png){width="0.15833333333333333in" height="0.15833333333333333in"} \> click on the **apply** ![](media/image481.png){width="0.275in" height="0.25833333333333336in"} icon.

**Step 3.** Set the default map position.

-   Select **Default** \> drag the map to your desired location \> click on **Set Position**.

-   Click on the **save** ![](media/image482.png){width="0.325in" height="0.2833333333333333in"} icon, and the map below is shown:

![](media/image489.jpeg){width="5.0in" height="3.8645833333333335in"}

**Example 2.** Map total acute watery diarrhoea (AWD) data by health facility for Elvoba Province in Nambutu for 2018.

**Step 1.** Configure general settings.

-   Select **Menu** \> **Analysis** \> **Mapping** \> **Create New** \> enter a **Title** (e.g. "AWD Cases -- Health facility Elvoba Province").

**Step 2.** Add a layer for AWD cases.

-   Select **Layers** \> click on the **add** ![](media/image474.png){width="0.3in" height="0.25833333333333336in"} icon.

-   Under **Visualization**, enter "AWD cases -- Health facility Elvoba Province" as the **Layer title** \> set **Visualization** as **Locations of type** \> select the **Location** Elvoba Province \> select Health Facility as the **Location Type**.

-   Under **Data source**, set **Data source** as **Indicator**\> select the **Indicator** AWD Cases Total \> set **From** as 2018-01-01 in the calendar \> set **To** as 2018-12-31 in the calendar.

-   Under **Style**, set **Stroke colour** as ![](media/image479.png){width="0.15833333333333333in" height="0.15833333333333333in"} \> set **Stroke width** as 2 \> set **Fill colour** as ![](media/image480.png){width="0.2in" height="0.2in"} \> set **Fill opacity** as 0.8 \> set **Marker type** as Circle \> set **Marker size** as 40.

-   Under **Labels**, set **Label type** as Numbered \> set **Label colour** as ![](media/image479.png){width="0.15833333333333333in" height="0.15833333333333333in"} \> click on the **apply** ![](media/image481.png){width="0.275in" height="0.25833333333333336in"} icon.

**Step 3.** Set the default map position.

-   Go to **Default** \> drag the map to your desired location \> click on **Set Position**.

-   Click on the **save** ![](media/image482.png){width="0.325in" height="0.2833333333333333in"} icon, and the map below is shown:

![](media/image490.png){width="5.0in" height="1.9583333333333333in"}

## 16.4 Mapping data for a particular group of locations

For demonstration purpose, this guide uses the following example.

**Example 1.** Map the total AWD data of locations served by nongovernmental organization (NGO) X in Nambutu for 2020.

**Step 1.** Configure general settings.

-   Select **Menu** \> **Analysis** \> **Mapping** \> **Create New** \> enter a **Title** (e.g. "AWD -- NGO X").

**Step 2.** Add a layer for AWD cases.

-   Select **Layers** \> click on the **add** ![](media/image474.png){width="0.3in" height="0.25833333333333336in"} icon.

-   Under **Visualization**, enter "AWD -- EWARS Group" as the **Layer title** \> set **Visualization** as **Locations of Group** \> select NGO X as the **Group**.

-   Under **Data source**, set **Data source** as **Indicator** \> select the **Indicator** AWD Total \> set **From** as 2020-01-01 in the calendar \> set **To** as 2020-12-31 in the calendar.

-   Under **Thresholds**, click on the **add** ![](media/image475.png){width="0.2916666666666667in" height="0.25833333333333336in"} icon \> enter "0" to "1000", choose ![](media/image491.png){width="0.2in" height="0.2in"} \> enter "1000 to 3000", choose ![](media/image492.png){width="0.2in" height="0.2in"}.

-   Under **Style**, set Stroke colour as ![](media/image479.png){width="0.15833333333333333in" height="0.15833333333333333in"} \> set **Stroke width** as 2 \> set **Fill colour** as ![](media/image492.png){width="0.2in" height="0.2in"} \> set **Fill opacity** as 0.8 \> set **Marker type** as Circle \> set **Marker size** as 40.

-   Under **Labels**, set **Label type** as Numbered \> set **Label colour** as ![](media/image479.png){width="0.15833333333333333in" height="0.15833333333333333in"} \> click on the **apply** ![](media/image481.png){width="0.275in" height="0.25833333333333336in"} icon.

**Step 3.** Set the default map position.

-   Go to **Default** \> drag the map to your desired location \> click on **Set Position**.

-   Click on the **save**![](media/image482.png){width="0.325in" height="0.2833333333333333in"} icon, and the map below is shown:

![](media/image493.jpeg){width="5.133333333333334in" height="3.2083333333333335in"}

## 16.5 Mapping coordinate (latitude and longitude) data

For demonstration purposes, this guide uses the following example.

**Example 1.** Map the data from the weekly EWARS reporting form based on the **Collected Lat/Long** field for Nambutu from January 2021 to June 2021.

**Step 1.** Configure general settings.

-   Select **Menu** \> **Analysis** \> **Mapping** \> **Create New** \> enter a **Title** (e.g. "Reports based on Lat/Long").

**Step 2.** Add a layer for report data.

-   Select **Layers** \> click on the **add** ![](media/image474.png){width="0.3in" height="0.25833333333333336in"} icon.

-   Under **Visualization**, enter "EWARS Group" as the **Layer title** \> set **Visualization** as **Collected Lat/Long** \> select **Weekly EWARS Reporting** **Form** \> select GPS coordinates as the **Field** \> set **From** as 2021-01-01 in the calendar \> set **To** as 2021-06-30 in the calendar.

-   Under **Style**, set **Stroke colour** as ![](media/image479.png){width="0.15833333333333333in" height="0.15833333333333333in"} \> set **Stroke width** as 2 \> set **Fill colour** as ![](media/image485.png){width="0.2in" height="0.2in"} \> set **Fill opacity** as 0.8 \> set **Marker size** as 40.

-   Under **Labels**, set **Label type** as Numbered \> set **Label colour** as ![](media/image479.png){width="0.15833333333333333in" height="0.15833333333333333in"} \> click on the **apply** ![](media/image481.png){width="0.275in" height="0.25833333333333336in"} icon.

**Step 3.** Set the default map position.

-   Go to **Default** \> drag the map to your desired location \> click on **Set Position**.

-   Click on the **save** ![](media/image482.png){width="0.325in" height="0.2833333333333333in"} icon, and the map below is shown:

![](media/image494.jpeg){width="5.0625in" height="2.098827646544182in"}

## 16.6 Showing alert data on a map

For demonstration purposes, this guide uses the following example.

**Example 1.** Show AWD alerts for Nambutu for 2020.

**Step 1.** Configure general settings.

-   Select **Menu** \> **Analysis** \> **Mapping** \> **Create New** \> enter a **Title** (e.g. "AWD Alerts").

**Step 2.** Add a layer for AWD alerts.

-   Select **Layers** \> click on the **add** ![](media/image474.png){width="0.3in" height="0.25833333333333336in"} icon.

-   Under **Visualization**, enter "AWD Alerts" as the Layer title \> set **Visualization** as **Alerts Map** \> select the **Location** Nambutu \> select **AWD** as the **Alarm** \> set **Alerts triggered** as the **Dimension** \> set **From** as 2020-01-01 in the calendar \> set **To** as 2020-12-31 in the calendar.

-   Under **Style**, set **Stroke colour** as ![](media/image479.png){width="0.15833333333333333in" height="0.15833333333333333in"} \> set **Stroke width** as 3 \> set **Fill colour** as ![](media/image495.png){width="0.2in" height="0.2in"} \> set **Fill opacity** as 0.8 \> set **Marker size** as 15 \> click on the **apply** ![](media/image481.png){width="0.275in" height="0.25833333333333336in"} icon.

**Step 3.** Set the default map position.

-   Go to **Default** \> drag the map to your desired location \> click on **Set Position**.

-   Click on the **save** ![](media/image482.png){width="0.325in" height="0.2833333333333333in"} icon, and the map below is shown:

![](media/image496.jpeg){width="5.0in" height="4.229166666666667in"}

## 16.7 Mapping alerts for two different locations using a multilayer map

For demonstration purposes, this guide uses the following example.

**Example 1.** Map AWD alerts data for Aimal and Rimpar provinces for 2020.

**Step 1.** Configure general settings.

-   Select **Menu** \> **Analysis** \> **Mapping** \> **Create New** \> enter a **Title** (e.g. "AWD Alerts").

**Step 2.** Add a layer for AWD case data for Aimal Province for 2022.

-   Select **Layers** \> click on the **add** ![](media/image474.png){width="0.3in" height="0.25833333333333336in"} icon.

-   Under **Visualization**, enter "AWD Alerts -- Aimal" as the **Layer title** \> set **Visualization** as **Alerts Map** \> select the **Location** Aimal \> select AWD as the **Alarm** \> set Alerts triggered as the **Dimension** \> set **From** as 2020-01-01 in the calendar \> set **To** as 2020-12-31 in the calendar.

-   Under **Style**, set **Stroke colour** as ![](media/image479.png){width="0.15833333333333333in" height="0.15833333333333333in"} \> set **Stroke width** as 3 \> set **Fill colour** as ![](media/image495.png){width="0.2in" height="0.2in"} \> set **Fill opacity** as 0.8 \> set **Marker size** as 15 \> click on the **apply** ![](media/image481.png){width="0.275in" height="0.25833333333333336in"} icon.

    **Step 3.** Add a second layer for AWD case data for Rimpar province for 2022

-   Under **Visualization**, enter "AWD Alerts -- Rimpar" as the **Layer title** \> set **Visualization** as **Alerts Map** \> select the **Location** Rimpar \> select **AWD** as the **Alarm** \> set **Alerts triggered** as the **Dimension** \> set **From** as 2020-01-01 in the calendar \> set **To** as 2020-12-31 in the calendar.

-   Under **Style**, set **Stroke colour** as ![](media/image479.png){width="0.15833333333333333in" height="0.15833333333333333in"} \> set **Stroke width** as 3 \> set **Fill colour** as![](media/image485.png){width="0.2in" height="0.2in"} \> set **Fill opacity** as 0.8 \> set **Marker size** as 15 \> click on the **apply** ![](media/image481.png){width="0.275in" height="0.25833333333333336in"} icon.

**Step 4.** Set the default position of the map.

-   Go to **Default** \> drag the map to your desired location. Click on **Set Position**.

-   Click on the **save** ![](media/image482.png){width="0.325in" height="0.2833333333333333in"}icon, and the map below is shown:

![](media/image497.jpeg){width="5.0in" height="3.625in"}

## 16.8 Viewing, editing and downloading My maps

My maps are maps created by you and not shared with other EWARS users.

-   Select **Menu** \> **Analysis** \> **Mapping** \> **My Maps**, and all maps you have created are listed, as shown below:

![](media/image498.png){width="5.7in" height="2.55in"}

-   Click on the name of the map (e.g. Map of Malaria Alerts), and the map below is shown:

![](media/image499.jpeg){width="5.0in" height="2.9583333333333335in"}

-   If you want to edit saved maps \> click on the map you want edit \> make the required changes under the settings for the layers \> click on the **save** ![](media/image253.png){width="0.2833333333333333in" height="0.21666666666666667in"} icon \> click on the **download** ![](media/image458.png){width="0.35833333333333334in" height="0.2916666666666667in"} icon, and the map is downloaded as a PDF file.

## 16.9 Viewing shared maps

Shared maps are maps that are shared by other users in the EWARS system.

-   Select **Menu** \> **Analysis** \> **Mapping** \> **Shared maps**, and all shared maps are listed, as shown below:

![](media/image500.png){width="5.45in" height="1.9416666666666667in"}

-   Click on the name of the Map (e.g. Map of Malaria Alerts), and the map below is shown:

![](media/image501.jpg){width="3.1354166666666665in" height="5.0in"}

## 16.10 Sharing a map via a via a public link

You can share maps by setting access as public or by copying the link and sharing the copied link with another user via email. Users can view the map either by pasting the link into their browser or by clicking on the universal resource locator (URL) received in the email. The shared map can be used in other information products, such as Bulletins and dashboards.

To give public access to EWARS maps, follow the steps below.

-   Select **Menu** \> **Analysis** \> **Mapping** \> **My Maps**. Click on the map (e.g. Reported measles cases) \> set **Access** to **Public** \> click on the **save** ![](media/image253.png){width="0.2833333333333333in" height="0.21666666666666667in"} icon.

To share the URL/link of the map, follow the steps below.

-   Select **Menu** \> **Analysis** \> **Mapping** \> **My Maps**. Click on the **copy** ![](media/image502.png){width="0.2833333333333333in" height="0.25in"} icon next to the map you want to share (e.g. Reported measles cases), and the URL is copied. Email the copied URL/link to another user, who can view the map by clicking on the URL/link received in the email.

## 16.11 Sharing maps with EWARS account users

You can share the map with users of the same EWARS account by enabling sharing of the map under settings.

-   Select **Menu** \> **Analysis** \> **Mapping** \> **My Maps**. Click on the map (e.g. Reported measles cases) \> set **Shared** field to **Shared** \> click on the **save** ![](media/image253.png){width="0.2833333333333333in" height="0.21666666666666667in"} icon.

To view the shared map, follow the steps below.

-   Select **Menu** \> **Analysis** \> **Mapping** \> **Shared Maps**. The Reported measles cases map is visible.

The following chapter provides an overview of widgets and the configurations associated with them.

#  

# Chapter 17. Widgets and their configuration

Widgets are a vital feature of the Early Warning, Alert and Response System (EWARS). They act as the core configurable data visualization units for features like Bulletins, Dashboards, Notebooks and Websites. Widgets are used to display text data, charts, maps and similar in dashboards, bulletins and websites.

There are 28 widgets in use in EWARS that fulfil different data visualization needs. Their differential distribution among associated features in the menu is illustrated in Table 17.1.

If you are reading this guide electronically, you can hover over and click on any widget in the table to expand it.

Table 17.1. The EWARS widgets

  ---------------------------------------------------------------------------------------------------------------------------------------
  **Widgets**                                         **Associated feature in EWARS Menu**                                  
  --------------------------------------------------- -------------------------------------- --------------- -------------- -------------
                                                      **Dashboard**                          **Bulletins**   **Notebook**   **Website**

  **17.3 Row and Cell widgets**                       **✓**                                                                 **✓**

  **17.4 Text widget in Dashboards**                  **✓**                                                  **✓**          **✓**

  **17.5 Image widget in Dashboards**                 **✓**                                                                 **✓**

  **17.6 Raw widget**                                 **✓**                                  **✓**                          **✓**

  **17.7 Info widget**                                **✓**                                                                 

  **17.8 Metrics widget**                             **✓**                                                                 **✓**

  **17.9 Outbreaks widget**                           **✓**                                                                 **✓**

  **17.10 Tasks widget**                              **✓**                                                                 

  **17.11 Assignments widget**                        **✓**                                                                 

  **17.12 Overdue reports widget**                    **✓**                                                                 

  **17.13 Documents widget**                          **✓**                                                                 

  **17.14 Recent submissions widget**                 **✓**                                                                 

  **17.15 Activity feed widget**                      **✓**                                                                 

  **17.16 Map widget**                                **✓**                                  **✓**           **✓**          **✓**

  **17.17 Alerts map widget**                         **✓**                                                                 

  **17.18 Series chart widget**                       **✓**                                  **✓**           **✓**          **✓**

  **17.19 Pyramid chart widget**                      **✓**                                  **✓**           **✓**          **✓**

  **17.20 Category widget**                           **✓**                                  **✓**           **✓**          **✓**

  **17.21 Table widget**                                                                     **✓**           **✓**          **✓**

  **17.22 Menu widget**                                                                                                     **✓**

  **17.23 Text widget in Website Builder**                                                                                  **✓**

  **17.24 Image widget in Website Builder**                                                                                 **✓**

  **17.25 Enhanced table widget**                     **✓**                                  **✓**           **✓**          **✓**

  **17.26 Enhanced map widget**                       **✓**                                  **✓**           **✓**          **✓**

  **17.27 Carousel widget**                                                                                                 **✓**

  **17.28 Video widget**                                                                                                    **✓**

  **17.29 HTML (HyperText Markup Language) widget**   **✓**                                                                 **✓**

  **17.30 Document widget**                                                                                                 **✓**

  **17.31 Document list widget**                                                                                            **✓**
  ---------------------------------------------------------------------------------------------------------------------------------------

  ---------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![](media/image43.png){width="0.65625in" height="0.3541666666666667in"}   This chapter is most valuable when it is read in conjunction with the dedicated chapters on Dashboards, Documents/bulletins, Notebooks and Website Builder.

  ---------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------

The topics set out how to add widgets to the associated menus and select periods for them.

## 17.1 How to add widgets

Different widget options are available under different features, but the same configuration rules apply across similar widgets.

### 17.1.1 Adding a widget to a bulletin

All widgets are available in the add widget drop-down menu in bulletins.

-   Select **Menu** \> **Document Templates** \> click on **New** at the top right-hand corner of the screen.

-   Click on the **Template** tab \> place the cursor where you want to insert the widget \> select a widget (e.g. series widget) from the ![](media/image503.png){width="0.9270833333333334in" height="0.34375in"} drop-down menu in the toolbar, and the widget is added, as shown below:

![](media/image504.png){width="6.258333333333334in" height="2.816666666666667in"}

### 17.1.2 Adding a widget to a dashboard

-   Select **Menu** \> **Dashboards** \> click on **Create New** at the top right-hand corner of the screen.

In a dashboard, widgets cannot be dragged directly into an empty space; they can only be dragged onto an empty row. So the first step is to drag a row into the empty space. All the widgets are listed in the left-hand column.

-   Drag and drop a **Row** widget from the left-hand column to the middle section \> click on the **expand** ![](media/image505.png){width="0.23958333333333334in" height="0.23958333333333334in"} icon to expand a widget category (e.g. Chart Component) \> drag a widget (e.g. Category Chart) onto a row, and the widget is added, as shown below:

![](media/image506.png){width="6.90625in" height="2.4166666666666665in"}

### 17.1.3 Adding a widget to a website 

In Website Builder, widgets cannot be dragged directly into an empty space; they can only be dragged onto an empty row. All the widgets are listed in the left-hand column.

-   Select **Menu** \> **Website Builder**. Click on the **edit** ![](media/image231.png){width="0.2916666666666667in" height="0.28125in"} icon next to any of the websites.

-   Drag and drop a **Row** widget from the left-hand column to the right-hand side \> click on the **expand** ![](media/image507.png){width="0.175in" height="0.175in"} icon to expand the widget category (e.g. Chart Component) \> drag a widget (e.g. Series Chart) onto a row, and the widget is added, as shown below:

![](media/image508.png){width="6.5in" height="2.941666666666667in"}

### 17.1.4 Adding a widget to a notebook

-   Select **Menu** \> **Notebooks** \> **My Notebooks** \> click on **Create Notebook**. All the widgets are listed in the left-hand column.

-   Drag and drop a widget (e.g. Pyramid Chart) from the left-hand column to middle section, and the widget is added, as shown below:

![](media/image509.png){width="6.5in" height="2.808333333333333in"}

## 17.2 How to select time period/date range in widgets

Most of the widgets -- including raw widget, map widget, series chart widget, pyramid chart widget, category chart widget and table widget -- require you to set up a time interval or period.

Selecting a time period can be simple in some instances but more complex in others. Because it is vital element in all widgets, while many different options exist for selection, this section explains the time period or date range selection as a separate entity. The explanations below should help you to select the date range/time period easily in any particular widget where there is a date period component.

You can select and specify data intervals using the following period selection user interface:

![](media/image510.png){width="6.366666666666666in" height="1.425in"}

  ---------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------
  ![](media/image43.png){width="0.65625in" height="0.3541666666666667in"}   [You can check with your national or regional surveillance guidance for the epidemiological week (]{.mark}epi week[) calculation.]{.mark}

  ---------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------

***17.2.1 Selecting start and end dates using the EWARS calendar***

To select start and end dates using the EWARS calendar, follow the steps below.

-   Click on the **calendar** ![](media/image511.png){width="0.23333333333333334in" height="0.21666666666666667in"} icon \> select the year and month using the **previous** ![](media/image512.png){width="0.2916666666666667in" height="0.2604166666666667in"} and **next** ![](media/image513.png){width="0.20833333333333334in" height="0.21666666666666667in"} icons and select a date, as shown below:

![](media/image514.png){width="2.9in" height="2.1166666666666667in"}

### 17.2.2 Selecting start and end dates using named options

To select start and end dates using named options, follow the steps below.

-   Click on the **calendar** ![](media/image515.png){width="0.2916666666666667in" height="0.28125in"} icon, and named options are listed, as shown below:

![](media/image516.png){width="4.991666666666666in" height="2.091666666666667in"}

-   Click on the named option to select it.

To help you understand the available named options, they are defined below, with examples.

-   **Today:** the current date: if you are configuring EWARS on 17 August 2021, it will consider the date to be 17 August 2021.

-   **This week start:** the start date of the current week: if you are configuring EWARS on (Tuesday) 17 August 2021, it will consider the start date to be (Monday) 16 August 2021.

-   **This week end:** the end date of the current week: if you are configuring EWARS on (Tuesday) 17 August 2021, it will consider the date to be (Sunday) 22 August 2021.

-   **This month start:** the start date of the current month: if you are configuring EWARS on 17 August 2021, it will consider the date to be 1 August 2021.

-   **This month end:** the end date of the current month: if you are configuring EWARS on 17 August 2021, it will consider the date to be 31 August 2021.

-   **This year start:** the start date of the current year: if you are configuring EWARS on 17 August 2021, it will consider the date to be 1 January 2021.

-   **This year end:** the end date of the current year: if you are configuring EWARS on 17 August 2021, it will consider the date to be 31 December 2021.

![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"} **Note:** the following named options are only available in **Document Templates**.

-   **Document week start:** the start date of the week for which the document is published. Let's assume that a bulletin is prepared for Week 30 of 2021: 26 July to 1 August. In this case, it will consider 26 July 2021 to be the document week start.

-   **Document weekend:** the end date of the week for which the document is published.

-   **Document month start:** the start date of the month for which the document is published.

-   **Document month end:** the end date of the month for which the document is published.

-   **Document year start:** the start date of the year for which the document is published.

-   **Document year end:** the end date of the year for which the document is published.

### 17.2.3 Using offset for named options

Using offset, you can add or subtract days, weeks, months or years from the selected named option date. For example, if you set offset as -1D, it subtracts 1 day from the date of the named option, as shown below:

![](media/image517.png){width="4.991666666666666in" height="2.4916666666666667in"}

-   Click on ![](media/image511.png){width="0.23333333333333334in" height="0.21666666666666667in"} in the **From** field \> select a named option \> enter the **Offset** value (e.g. -1D).

To help you understand the available Offset options, they are defined below, with examples.

-   **-1Y:** 1 year back from the date of the selected named option.

-   **-2M:** 2 months back from the date of the selected named option.

-   **-3D:** 3 days back from the date of the selected named option.

-   **-4W:** 4 weeks back from the date of the selected named option.

-   **1Y:** 1 year ahead of the date of the selected named option.

-   **2M:** 2 months ahead of the date of the selected named option.

-   **3D:** 3 days ahead of the date of the selected named option.

-   **4W:** 4 weeks ahead of the date of the selected named option.

### 17.2.4 Selecting start and end dates using quick ranges

-   Click on a desired **Quick Range** (e.g. Previous week). Both start and end dates are selected, as shown below:

![](media/image518.png){width="6.35in" height="1.8583333333333334in"}

To help you understand the available quick ranges, they are defined below, with examples.

-   **Last 30 days:** 30 days before the current date: if you are configuring EWARS on 17 August 2021, it will consider the start date to be 18 July 2021 and the end date to be 17 August 2021.

-   **Last 60 days:** 60 days before the current date.

-   **Last 6 months:** 6 months before the current date: if you are configuring EWARS on 17 August 2021, it will consider the start date to be 17 Feb 2021 and the end date to be 17 August 2021.

-   **Last 1 year:** 1 year before the current date: if you are configuring EWARS on 17 August 2021, it will consider the start date to be 17 August 2020 and the end date to be 17 Aug 2021.

-   **Last 2 years:** 2 years before the current year.

-   **Last 5 years:** 5 years before the current year.

-   **Yesterday:** the date of the day before the day you are viewing the widget: if you are configuring EWARS on 17 August 2021, it will consider the start and end dates to be 16 August 2021.

-   **Day before yesterday:** if you are configuring EWARS on 17 August 2021, it will take start and end dates to be 15 August 2021.

-   **This day last week:** the current day of the last week: if you are configuring EWARS on 17 August 2021, it will consider the date to be 10 August 2021.

-   **Previous week:** the week before the current week: if you are configuring EWARS on 17 August 2021, it will consider the start date to be (Monday) 9 August 2021 and the end date to be (Sunday) 15 August 2021.

-   **Previous 52 weeks:** 52 weeks before the current week: if you are configuring EWARS on 17 August 2021, it will consider the start date to be 15 August 2020 and the end date to be 15 August 2021.

-   **Previous month:** the month before the current month: if you are configuring EWARS on 17 August 2021, it will consider the start date to be 1 July 2021 and the end date to be 31 July 2021.

-   **Previous year:** the year before the current year: if you are configuring EWARS on 17 August 2021, it will consider the start date to be 1 January 2020 and the end date to be 31 December 2020.

-   **Today:** the current date: if you are configuring EWARS on 17 August 2021, it will consider both the start and end dates to be 17 August 2021.

-   **This week:** the current week: if you are configuring EWARS on 17 August 2021, it will consider the start date to be (Monday) 16 August 2021 and the end date to be (Sunday) 22 August 2021.

-   **This month:** the current month: if you are configuring EWARS on 17 August 2021, it will consider the start date to be 1 August 2021 and the end date to be 31 August 2021.

-   **This year:** the current year: if you are configuring EWARS on 17 Aug 2021, it will consider the start date to be 1 January 2021 and the end date to be 31 December 2021.

  ---------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![](media/image43.png){width="0.65625in" height="0.3541666666666667in"}   If you are developing a weekly bulletin, always keep the EWARS calendar set as Document week start: Document week end. If you are making a daily dashboard, keep the EWARS calendar as Today for both entries.

  ---------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The following topics give details about individual widgets.

## 17.3 Row and cell widgets

***Available in***: Dashboards, Website Builder

Row widget is a container widget. It can hold static and dynamic widgets such as text, image, video, carousel, HTML, charts and others. You can add multiple rows. Rows divide the page into multiple horizontal segments. You can drag and drop any widget of your choice onto a row.

Cell widget divides the row widget into vertical segments. To add a cell widget, drag it onto a row. You can add multiple cell widgets to a row. You can drag and drop any widget of your choice onto the cell.

Right-click on the row or cell you have dragged to view more options, as shown below:

![](media/image519.png){width="6.358333333333333in" height="2.466666666666667in"}

The highlighted part above can be seen once you right-click the row or cell. You can move rows or cells, duplicate them or remove them using these options.

If you click on **Cell Settings**, a cell editor screen opens, in which you can define the width of the cell (%), and give a description of the cell and cell classes.

## 17.4 Text widget in Dashboards

***Available in***: Dashboards

The text widget in Dashboards is used to display textual content. The screenshot below is an example of what the text widget looks like following configuration in a notebook or dashboard:

![](media/image520.png){width="6.408333333333333in" height="1.0583333333333333in"}

To add a text widget to a dashboard and configure it, follow the steps below.

-   Select **Menu** \> **Dashboards** \> click on **Create New** at the top right-hand corner of the screen.

-   Drag and drop a **Row** widget \> click on the **expand** ![](media/image505.png){width="0.23958333333333334in" height="0.23958333333333334in"} icon to expand the **Content** category \> drag and drop a **Text** widget onto the row \> click on it, and the widget editor opens, as shown below:

![](media/image521.png){width="6.458333333333333in" height="2.8583333333333334in"}

-   Populate the fields as follows.

```{=html}
<!-- -->
```
-   **Widget Title**: enter a title for the widget (e.g. "Measles Case Study"). This is visible at the top of the screen.

-   **Widget Icon:** enter a relevant widget icon. The icon is visible just before the widget title.

  ---------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![](media/image43.png){width="0.65625in" height="0.3541666666666667in"}   To change and incorporate the widget icons, refer to websites like that of the United Nations Office for the Coordination of Humanitarian Affairs (OCHA): https://brand.unocha.org/d/xEPytAUjC3sH/icons

  ---------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-   **Header Colour:** enter the colour name or hex colour code for the background colour of the header (e.g. ![](media/image522.png){width="0.15833333333333333in" height="0.15833333333333333in"} [(orange)]{.mark}). To obtain the hex code, refer to any colour-code picker website.

-   **Header Text Colour:** [enter the]{.mark} colour name or [hex colour code for the text colour of the header (e.g. #fff).]{.mark} To obtain the hex code, refer to any colour-code picker website.

-   **Content:** enter a relevant paragraph of text.

```{=html}
<!-- -->
```
-   Click on **Save Change(s)**.

    For more information on Text widget in Website Builder, refer to topic **17.23 Text widget in Website Builder**.

## 17.5 Image widget in Dashboards

***Available in***: Dashboards

Use an image widget when you want to add an image in Dashboards. It also allows you to add a heading to the image if needed. Fig. 17.1 shows an example of what the image widget looks like on a dashboard with and without a heading.

Fig. 17.1. A configured image widget, with and without a heading

![](media/image523.png){width="2.6333333333333333in" height="2.566666666666667in"} ![](media/image524.png){width="2.7645723972003498in" height="2.5904090113735783in"}

To configure an image widget, follow the steps below.

-   Select **Menu** \> **Dashboards** \> click on **Create New** at the top right-hand corner of the screen.

-   Drag and drop a **Row** widget \> click on the **expand** ![](media/image505.png){width="0.23958333333333334in" height="0.23958333333333334in"} icon to expand the **Content** category \> drag and drop an **Image** widget onto the row \> click on it, and the widget editor opens, as shown below:

![](media/image525.png){width="6.333333333333333in" height="2.7583333333333333in"}

-   Populate the fields as follows.

```{=html}
<!-- -->
```
-   **Widget Title**: enter a title for the widget (e.g. "Ministry of Health of Nambutu"). This is visible at the top of the screen.

-   **Widget Icon:** enter a relevant widget icon. The icon is visible just before the widget title. (If you want to change the icon, refer to the **Tip** in topic **17.4 Text widget**).

-   **Header Colour:** enter the colour name or hex colour code for the background colour of the header (e.g. ![](media/image522.png){width="0.15833333333333333in" height="0.15833333333333333in"} [(orange)]{.mark}).

-   **Header Text Colour:** [enter the colour]{.mark} name or [hex colour code for the text colour of the header (e.g. #fff).]{.mark}

-   **Image URL** \[Mandatory\]:\
    **Either** click on the **upload** ![https://lh3.googleusercontent.com/5s86Vw-j_1lKcSue3j1M2e98ahw-rwzpaziK3PXCjSrcKpGC-ZJfwBqoFGAtXe3fR88jMfcVHSwvQwN-Qf2RCoAokm5ObhH7J4WNP7YjxVbjbSAASu4DrKoe9YXea0ZKaKuxmkSj](media/image526.png){width="0.2916666666666667in" height="0.3333333333333333in"} icon to upload an image saved on your computer. It is uploaded as web content, and the newly created universal resource locator (URL) is populated automatically in the textbox beside it. The recommended size for an image is approximately 2GB. You should make sure that the image is already properly sized for display on the dashboard.\
    \
    **Or** copy and paste an existing URL or type the URL manually in the textbox. The address specified must resolve to a publicly accessible image. The image file is not copied to EWARS but remains in its source location. EWARS fetches it when displaying it on the page.

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** there is an inherent risk in this approach -- if you choose an URL for a location that you don't control (for example, if you reference an image on another website or via a search engine), if that image is ever removed by its owner, it will disappear from EWARS.
  --------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-   **Image link:** enter the URL for a website/webpage that is to be opened when the link is clicked (e.g. http://who.int). Once the user clicks on the image, a new tab is opened and the user is redirected to the specified URL.

```{=html}
<!-- -->
```
-   Click on **Save Change(s)**.

For more information on Text widget in Website Builder, refer to topic **17.24 Image widget in Website Builder**.

## 17.6 Raw widget

***Available in***: Dashboards, Bulletins and Website Builder

The raw widget allows the user to show an indicator value in a well defined format. The r[aw widget available in Dashboards is different from the one available in Bulletins and Website Builder, so its configuration is explained separately.]{.mark}

### 17.6.1 Raw widget in Dashboards

***Available in***: Dashboards

This section assumes that you have already created a dashboard for your account, to which you can now start adding widgets for configuration. Refer to **Chapter 19. Dashboards** for more information on how to create a dashboard.

Fig. 17.2 shows an example of a configured raw widget in a dashboard.

Fig. 17.2. A configured raw widget in a dashboard

![](media/image527.png){width="5.875in" height="2.692707786526684in"}

To configure the raw widget, follow the steps below.

-   Select **Menu** \> **Dashboards** \> click on **Create New** at the top right-hand corner of the screen.

-   Drag and drop a **Row** widget \> click on the **expand** ![](media/image505.png){width="0.23958333333333334in" height="0.23958333333333334in"} icon to expand the **Other** category \> drag and drop a **Raw** widget onto the row \> click on it, and the widget editor opens, as shown below:

![](media/image528.png){width="6.225in" height="3.1333333333333333in"}

-   Populate the fields as follows.

```{=html}
<!-- -->
```
-   **Title:** enter a title for the widget. This is visible at the top of the screen.

-   **Location Specification:** you can limit the source of data for the indicator used in the widget by specifying the location source and its sub-options:\
    \
    **Either** set **Location Specification** as **Specific Location**: select a **location** in the drop-down menu (e.g. Nambutu), and data reported from a specific location are considered.\
    \
    **Or** set **Location Specification** as **Location Group(s)**: select a **location group** from the drop-down menu (e.g. NGO A). If you want several location groups to be considered, select more from the drop-down menu (e.g. NGO B, NGO C).\
    **Or** set **Location Specification** as **User's Location**. Once set as this option, only data reported from the **User's Location** are considered.

-   **Data Source:** you can set data source as **Indicator** for a single indicator, or as **Complex** to generate a Composite indicator.\
    \
    **Either** set **Source Type** as **Indicator** \> select the **Indicator** whose values you want to display in the chart from the drop-down menu \> set **Reduction** as **Sum** or **Average** to calculate the indicator values\
    \
    **Or** set **Source Type** as **Complex** \> enter an arithmetic formula in the **Formula** textbox \> click on **Add Variable** \> click on the **edit** ![https://lh3.googleusercontent.com/oQPzlOtszncFAz6shiVjMM-ac4gqgxZvp3EJXwmqxypMhcShBp3wzsLp4cDj4z4EW40pxP6ai-4iaweH2\--E3vmFjeOA5e7dT9HhguYaZHazJlPFdCEk91b5mzVprFzxYNGvDS67](media/image529.png){width="0.20833333333333334in" height="0.20833333333333334in"} icon \> enter the **Variable Name** (e.g. "Consultations 5 and over") \> select Consultations 5 and over from the **Indicator** drop-down menu.

-   **Aggregation:** select the aggregation period (e.g. Week).

-   **Source** **period:** select the date range in the **From** and **To** drop-down menus or directly from the **Quick Ranges** menu. The default **From** and **To** dates are today.

-   **Value Text Size:** enter the font size.

-   **Number Formatting:** select how numbering need to be formatted (e.g. 0.00).

-   **Prefix:** if a prefix is needed, add it here (e.g. "AIM") to indicate a location. Prefix is an optional field: you may leave it blank if not needed.

-   **Suffix:** if a suffix is needed, enter it here (e.g. "AWD") to indicate the disease. Suffix is an optional field: you may leave it blank if not needed.

-   **Value Colouring:** once enabled, you can add colours to your numbers, depending on where they fit in a range (e.g. any value in the range 0--10 will be displayed in green, any value in the range 100--1000 will be displayed in red). To add a colour range, click on the **add** ![https://lh4.googleusercontent.com/Prm1-cZnhNmrn2GFWT94xFs6SKqAGA0_4L8dIteJTkbB3T8UpZUpOdCOfU7FpwDky4DPXatY2F_OgIZKE_kyuff_52Wrj3PvCkwfjd5j6GEWOfEs4tAWUZnIa_SSzO0rkk-874Zp](media/image530.png){width="0.1875in" height="0.1875in"} icon \> enter **min** and **max** values for the range and specify the colour via the colour picker drop-down menu, as shown below:

![](media/image531.png){width="6.008333333333334in" height="1.7916666666666667in"}

-   **Value Mapping:** once enabled, you can show a mapped value or text instead of the original value (e.g. if the original value is 0 you may select to display it as Null, range 0--10 as Low and range 100--1000 as High). Click on the **add** ![https://lh4.googleusercontent.com/Prm1-cZnhNmrn2GFWT94xFs6SKqAGA0_4L8dIteJTkbB3T8UpZUpOdCOfU7FpwDky4DPXatY2F_OgIZKE_kyuff_52Wrj3PvCkwfjd5j6GEWOfEs4tAWUZnIa_SSzO0rkk-874Zp](media/image530.png){width="0.1875in" height="0.1875in"} icon \> enter **min** and **max** values for the range and specify the mapped value. Each value mapping range has two number inputs and a textbox for a mapped value.

-   **Base Colour:** enter the name of the base colour: the colour in the background of the title (e.g. "white").

-   **Highlight Colour:** enter the name of the highlight colour: the colour in the top border of the raw widget, which surrounds the icon (e.g. "yellow").

![](media/image532.png){width="2.1333333333333333in" height="0.38333333333333336in"}

-   **Icon:** Enter the icon name. The icon is displayed at the top of the widget, as shown below:

![](media/image533.png){width="2.075in" height="0.4in"}

![](media/image534.png){width="1.9333333333333333in" height="0.6666666666666666in"}

-   **Widget footer text:** enter widget footer text to be displayed as below, once the web user moves the mouse pointer over the icon:

![](media/image535.png){width="2.7333333333333334in" height="0.5416666666666666in"}

-   Click on **Save Change(s)**.

### 17.6.2 Raw widget in Bulletins and Website Builder

***Available in***: Bulletins and Website Builder

This section assumes that you have already created bulletins/document templates or a website for your account, to which you can now start adding raw widgets for configuration. Refer to **Chapter 21. Documents and Document Templates** and **Chapter 22. Website Builder** for more information on how to create these.

Fig. 17.3 shows an example of the configured raw widget in a bulletin.

Fig. 17.3. A configured raw widget in a bulletin

![](media/image536.png){width="1.5416666666666667in" height="1.3666666666666667in"}

To configure the raw widget, follow the steps below.

-   Select **Menu** \> **Document Templates** \> click on **New** at the top right-hand corner of the screen.

-   Click on the **Template** tab \> place the cursor where you want to insert the widget \> select **Series** widget from the ![](media/image503.png){width="0.9270833333333334in" height="0.34375in"} drop-down menu visible in the toolbar, and the widget is added. Double-click on it, and the widget editor opens, as shown below:

![](media/image537.png){width="6.325in" height="2.875in"}

-   Populate the fields as follows.

```{=html}
<!-- -->
```
-   **Title:** enter a title for the widget. This is visible at the top of the screen.

```{=html}
<!-- -->
```
-   **Location Specification:** you can limit the source of data for the indicator used in the widget by specifying the location source and its sub-options:\
    \
    **Either** set **Location Specification** as **Specific Location**: select a location via the location drop-down menu (e.g. Nambutu), and the data reported from a specific location are considered.\
    \
    **Or** set **Location Specification** as **Report Location**: the data reported from the location set in the location specification under general settings are considered.\
    \
    **Or** set **Location Specification** as **Group(s)**: select a **location group** from the drop-down menu (e.g. NGO A) \> set **Group Output** as **Aggregate**. If set as **Aggregate**, the system performs group-wide aggregation of the data and displays data for each group. If set as **Individual**, the system does location-wide aggregation of the data and displays data for each location of the group.\
    \
    **Or** set **Location Specification** as **User's Location**. Once set as this option, only data reported from the **User's Location** are considered.

```{=html}
<!-- -->
```
-   **Data Source:** you can set **Source Type** as **Indicator** for a single indicator, or as **Complex** to generate a calculated value:\
    \
    **Either** set **Source Type** as **Indicator** \> select the **Indicator** whose values you want to display in the chart from the drop-down menu \> select **Reduction** as **Sum** or **Average** to calculate the indicator values.\
    \
    **Or** set **Source Type** as **Complex** \> enter an arithmetic formula in the **Formula** textbox \> click on **Add Variable** \> click on the **edit** ![https://lh3.googleusercontent.com/oQPzlOtszncFAz6shiVjMM-ac4gqgxZvp3EJXwmqxypMhcShBp3wzsLp4cDj4z4EW40pxP6ai-4iaweH2\--E3vmFjeOA5e7dT9HhguYaZHazJlPFdCEk91b5mzVprFzxYNGvDS67](media/image529.png){width="0.20833333333333334in" height="0.20833333333333334in"} icon \> enter the **Variable Name** (e.g. "Consultations 5 and over") \> select Consultations 5 and over from the indicator drop-down menu.

-   **Aggregation:** select the aggregation period (e.g. Week).

-   **Source** **period:** select the date range in the **From** and **To** drop-down menus or directly from the **Quick Ranges** menu. Default **From** and **To** dates are today.

-   **Number Formatting:** select the formatting style of the value from the drop-down menu (e.g. 0.00).

-   **Value Mapping:** once enabled, instead of the original value, the mapped value is displayed. Click on the **add** ![https://lh4.googleusercontent.com/Prm1-cZnhNmrn2GFWT94xFs6SKqAGA0_4L8dIteJTkbB3T8UpZUpOdCOfU7FpwDky4DPXatY2F_OgIZKE_kyuff_52Wrj3PvCkwfjd5j6GEWOfEs4tAWUZnIa_SSzO0rkk-874Zp](media/image530.png){width="0.1875in" height="0.1875in"} icon \> enter **min** and **max values** for the range and specify the mapped value. Each value mapping range has two number inputs and a textbox for a mapped value.

```{=html}
<!-- -->
```
-   Click on **Save Change(s)**.

## 17.7 Info widget

***Available in***: Dashboards

The info widget is a special purpose widget that displays the current date and time (Fig. 17.4).

Fig. 17.4. A configured info widget, showing date and time

![](media/image538.png){width="5.55in" height="1.6166666666666667in"}

To configure an info widget, follow the steps below.

-   Select **Menu** \> **Dashboards** \> click on **Create New** at the top right-hand corner of the screen.

-   Drag and drop a **Row** widget \> click on the **expand** ![](media/image505.png){width="0.24166666666666667in" height="0.24166666666666667in"} icon to expand the **Other** category \> drag and drop an **Info** widget onto the row \> click on it, and the widget editor opens, as shown below:

![](media/image539.png){width="6.033333333333333in" height="2.6666666666666665in"}

Populate the fields as follows.

-   **Widget Title**: enter a title for the widget (e.g. "Information"). This is visible at the top of the screen.

-   **Widget Icon:** enter a widget icon. The icon is visible just before the widget title. (If you want to change the icon, refer to the **Tip** in topic **17.4 Text widget**.)

-   **Header Colour:** enter the colour name or hex colour code for the background colour of the header (e.g. ![](media/image522.png){width="0.15833333333333333in" height="0.15833333333333333in"} [(orange)]{.mark}).

-   **Header Text Colour:** [enter the]{.mark} colour name or [hex colour code for the text colour of the header (e.g. #030B0C).]{.mark}

```{=html}
<!-- -->
```
-   Click on **Save Change(s)**.

## 17.8 Metrics widget

***Available in***: Dashboards, Website Builder

The metrics widget allows you to display a numerical value and its label in a specific format. You can select numerical values from a predefined set.

Fig. 17.5 shows examples of the configured metrics widget.

Fig. 17.5. A configured metrics widget in bar layout and tabular layout

![](media/image540.png){width="6.475in" height="2.2333333333333334in"}

![](media/image541.png){width="6.475in" height="2.2583333333333333in"}

To configure a metrics widget, follow the steps below.

-   Select **Menu** \> **Dashboards** \> click on **Create New** at the top right-hand corner of the screen.

-   Drag and drop a **Row** widget \> click on the **expand** ![](media/image505.png){width="0.23958333333333334in" height="0.23958333333333334in"} icon to expand the **User** category \> drag and drop a **Metrics** widget onto the row \> click on it, and the widget editor opens, as shown below:

![](media/image542.png){width="6.35in" height="3.325in"}

-   Populate the fields as follows.

```{=html}
<!-- -->
```
-   **Widget Title:** enter a title for the widget. This is visible at the top of the screen.

-   **Widget Icon:** enter a widget icon. The icon is visible just before the widget title. (If you want to change the icon, refer to the **Tip** in topic **17.4 Text widget**.)

-   **Header Colour:** enter the colour name or hex colour code for the background colour of the header (e.g. ![](media/image522.png){width="0.15833333333333333in" height="0.15833333333333333in"} [(orange)]{.mark}).

-   **Header Text Colour:** [enter the]{.mark} colour name or [hex colour code for the text colour of the header (e.g. #030B0C).]{.mark}

-   **Layout:** the layout displays the design in which the metrics are displayed. Choose either of the following layouts:\
    **Bar --** metrics data are displayed in a bar layout.\
    **Table --** metrics data are displayed in a tabular format.

-   **Selected Metrics:** this allows you to select the field for which the metric count is to be generated (e.g. form submissions, devices and so on). To select all fields for the metric count, click on **Select All**.

```{=html}
<!-- -->
```
-   Click on **Save Change(s)**.

## 17.9 Outbreaks widget

***Available in***: Dashboards, Website Builder

The outbreaks widget allows the user to display an active outbreak list on the website. It is linked to the Outbreaks feature in the main menu.

Fig. 17.6 shows an example of the configured outbreaks widget.

Fig. 17.6. A configured outbreaks widget

![](media/image543.png){width="6.475in" height="3.158333333333333in"}

You can view the total count of active outbreaks (e.g. 4) at the top and a list of active outbreak names, along with their start dates, as shown above.

To configure an outbreaks widget, follow the steps below.

-   Select **Menu** \> **Dashboards** \> click on **Create New** at the top right-hand corner of the screen.

-   Drag and drop a **Row** widget \> click on the **expand** ![](media/image505.png){width="0.23958333333333334in" height="0.23958333333333334in"} icon to expand the **User** category \> drag and drop an **Outbreaks** widget onto the row \> click on it, and the widget editor opens, as shown below:

![](media/image544.png){width="6.433333333333334in" height="2.1333333333333333in"}

-   Populate the fields as follows.

```{=html}
<!-- -->
```
-   **Widget Title:** enter a title for the widget. This is visible at the top of the screen.

-   **Widget Icon:** enter a widget icon. The icon is visible just before the widget title. (If you want to change the icon, refer to the **Tip** in topic **17.4 Text widget**.)

-   **Header Colour:** enter the colour name or hex colour code for the background colour of the header (e.g. ![](media/image522.png){width="0.15833333333333333in" height="0.15833333333333333in"} [(orange)]{.mark}).

-   **Header Text Colour:** [enter the colour]{.mark} name or [hex colour code for the text colour of the header (e.g. #110502).]{.mark}

```{=html}
<!-- -->
```
-   Click on **Save Change(s)**.

## 17.10 Tasks widget

***Available in***: Dashboards

The tasks widget is a special purpose widget that displays a list of requests (Fig. 17.7). These requests are generally made by the Reporting User, and include:

-   amendment requests

-   deletion requests

-   assignment requests

-   user account requests.

For more information on tasks and notifications, refer to **Chapter 9. User profile, tasks and notifications**.

Fig. 17.7. A configured tasks widget

![](media/image545.png){width="4.1in" height="3.8in"}

You can view the requests by clicking on any of the above tasks.

To configure a tasks widget, follow the steps below.

-   Select **Menu** \> **Dashboards** \> click on **Create New** at the top right-hand corner of the screen.

-   Drag and drop a **Row** widget \> click on the **expand** ![](media/image505.png){width="0.24166666666666667in" height="0.24166666666666667in"} icon to expand the **User** category \> drag and drop a **Tasks** widget onto the row \> click on it, and the widget editor opens, as shown below:

![](media/image546.png){width="6.5in" height="2.933333333333333in"}

-   Populate the fields as follows.

```{=html}
<!-- -->
```
-   **Widget Title**: enter a title for the widget (e.g. "Pending Tasks"). This is visible at the top of the screen.

-   **Widget Icon:** enter a widget icon. The icon is visible just before the widget title. (If you want to change the icon, refer to the **Tip** in topic **17.4 Text widget**.)

-   **Header Colour:** enter the colour name or hex colour code for the background colour of the header (e.g. ![](media/image522.png){width="0.15833333333333333in" height="0.15833333333333333in"} [(orange)]{.mark}).

-   **Header Text Colour:** [enter the]{.mark} colour name or [hex colour code for the text colour of the header (e.g. #fff).]{.mark}

```{=html}
<!-- -->
```
-   Click on **Save Change(s)**.

## 17.11 Assignments widget

***Available in***: Dashboards

The assignments widget is a special purpose widget that is visible to the Reporting User, but can be configured by the Account Administrator (Fig. 17.8). It allows the Reporting User to view a list of all the assigned reporting forms. Using this widget, the Reporting User can also request assignment of a reporting form.

Fig. 17.8. A configured assignments widget

![](media/image547.png){width="5.875in" height="3.2583333333333333in"}

To configure an assignments widget, follow the steps below.

-   Select **Menu** \> **Dashboards** \> click on **Create New** at the top right-hand corner of the screen.

-   Drag and drop a **Row** widget \> click on the **expand** ![](media/image505.png){width="0.24166666666666667in" height="0.24166666666666667in"} icon to expand the **User** category \> drag and drop an **Assignments** widget onto the row \> click on it, and the widget editor opens, as shown below:

![](media/image548.png){width="6.275in" height="2.7666666666666666in"}

-   Populate the fields as follows.

```{=html}
<!-- -->
```
-   **Widget Title**: enter a title for the widget (e.g. "Assigned Tasks"). This is visible at the top of the screen.

-   **Widget Icon:** enter a relevant widget icon. The icon is visible just before the widget title. (If you want to change the icon, refer to the **Tip** in topic **17.4 Text widget**.)

-   **Header Colour:** enter the colour name or hex colour code for the background colour of the header (e.g. ![](media/image522.png){width="0.15833333333333333in" height="0.15833333333333333in"} [(orange)]{.mark}).

-   **Header Text Colour:** [enter the colour]{.mark} name or [hex colour code for the text colour of the header (e.g. #030B0C).]{.mark}

```{=html}
<!-- -->
```
-   Click on **Save Change(s)**.

## 17.12 Overdue reports widget

***Available in***: Dashboards

The overdue reports widget is a special purpose widget that is visible only to the Reporting User but can be configured only by the Account Administrator (Fig. 17.9). It displays a list of the records/reports for which the reporting due date has been reached but the record has not yet been submitted to the server, grouped by the form name.

Fig. 17.9. A configured overdue reports widget

![](media/image549.png){width="4.625in" height="2.9583333333333335in"}

To configure an overdue reports widget, follow the steps below.

-   Select **Menu** \> **Dashboards** \> click on **Create New** at the top right-hand corner of the screen.

-   Drag and drop a **Row** widget \> click on the **expand** ![](media/image505.png){width="0.24166666666666667in" height="0.24166666666666667in"} icon to expand the **User** category \> drag and drop an **Overdue Reports** widget onto the row \> click on it, and the widget editor opens, as shown below:

![](media/image550.png){width="6.441666666666666in" height="2.8916666666666666in"}

-   Populate the fields as follows.

```{=html}
<!-- -->
```
-   **Widget Title**: enter a title for the widget (e.g. "Overdue Reports"). This is visible at the top of the screen.

-   **Widget Icon:** enter a relevant widget icon. The icon is visible just before the widget title. (If you want to change the icon, refer to the **Tip** in topic **17.4 Text widget**.)

-   **Header Colour:** enter the colour name or hex colour code for the background colour of the header (e.g. ![](media/image522.png){width="0.15833333333333333in" height="0.15833333333333333in"} [(orange)]{.mark}).

-   **Header Text Colour:** [enter the colour]{.mark} name or [hex colour code for the text colour of the header (e.g. #fff).]{.mark}

-   **Specific Form (Optional)**: you can choose a specific form for the widget to display (e.g. Weekly EWARS Reporting Form). If not selected, the widget will display all the overdue records for all the forms, grouped by the form name.

```{=html}
<!-- -->
```
-   Click on **Save Change(s)**.

## 17.13 Documents widget

***Available in***: Dashboards

The documents widget allows you to display a list of documents on the dashboard. You can open any document from the list. Fig. 17.10 shows an example of a configured documents widget.

Fig. 17.10. A configured documents widget

![](media/image551.png){width="5.275in" height="1.2583333333333333in"}

To configure the documents widget, follow the steps below.

-   Select **Menu** \> **Dashboards** \> click on **Create New** at the top right-hand corner of the screen.

-   Drag and drop a **Row** widget \> click on the **expand** ![](media/image505.png){width="0.24166666666666667in" height="0.24166666666666667in"} icon to expand the **User** category \> drag and drop a **Documents** widget onto the row \> click on it, and the widget editor opens, as shown below:

![](media/image552.png){width="6.191666666666666in" height="2.5083333333333333in"}

-   Populate the fields as follows.

```{=html}
<!-- -->
```
-   **Widget Title:** enter a title for the widget (e.g. "Available documents"). This is visible at the top of the screen.

-   **Widget Icon:** enter a widget icon. The icon is visible just before the widget title. (If you want to change the icon, refer to the **Tip** in topic **17.4 Text Widget**.)

-   **Header Colour:** enter the colour name or hex colour code for the background colour of the header (e.g. ![](media/image522.png){width="0.15833333333333333in" height="0.15833333333333333in"} [(orange)]{.mark}).

-   **Header Text Colour:** [enter the colour]{.mark} name or [hex colour code for the text colour of the header (e.g. #110502).]{.mark}

```{=html}
<!-- -->
```
-   Click on **Save Change(s)**.

## 17.14 Recent submissions widget

***Available in***: Dashboards

The recent submissions widget is a special purpose widget that displays a list of all submitted records, starting with the most recently submitted record (Fig. 17.11). It displays 10 entries on the screen at a time.

Fig. 17.11. A configured recent submissions widget

![](media/image553.png){width="4.3in" height="3.591666666666667in"}

To configure a recent submissions widget, follow the steps below.

-   Select **Menu** \> **Dashboards** \> click on **Create New** at the top right-hand corner of the screen.

-   Drag and drop a **Row** widget \> click on the **expand** ![](media/image505.png){width="0.24166666666666667in" height="0.24166666666666667in"} icon to expand the **User** category \> drag and drop a **Recent Submissions** widget onto the row \> click on it, and the widget editor opens, as shown below:

![](media/image554.png){width="6.425in" height="2.7333333333333334in"}

-   Populate the fields as follows.

```{=html}
<!-- -->
```
-   **Widget Title**: enter a title for the widget (e.g. "Recent Submissions"). This is visible at the top of the screen.

-   **Widget :** enter a relevant widget icon. The icon is visible just before the widget title. (If you want to change the icon, refer to the **Tip** in topic **17.4 Text widget**.)

-   **Header Colour:** enter the colour name or hex colour code for the background colour of the header (e.g. ![](media/image522.png){width="0.15833333333333333in" height="0.15833333333333333in"} [(orange)]{.mark}).

-   **Header Text Colour:** [enter the colour]{.mark} name or [hex colour code for the text colour of the header (e.g. #fff).]{.mark}

```{=html}
<!-- -->
```
-   Click on **Save Change(s)**.

## 17.15 Activity feed widget

***Available in***: Dashboards

The activity feed widget is a special purpose widget that displays two types of activities: **report submission** activity and **user registration** activity (Fig. 17.12).

Fig. 17.12. A configured activity feed widget, showing report submission and user registration activity

![](media/image555.png){width="5.71666447944007in" height="3.6166666666666667in"}

To configure an activity feed widget, follow the steps below.

-   Select **Menu** \> **Dashboards** \> click on **Create New** at the top right-hand corner of the screen.

-   Drag and drop a **Row** widget \> click on the **expand** ![](media/image505.png){width="0.24166666666666667in" height="0.24166666666666667in"} icon to expand the **User** category \> drag and drop an **Activity Feed** widget onto the row \> click on it, and the widget editor opens, as shown below:

![](media/image556.png){width="6.291666666666667in" height="2.6666666666666665in"}

-   Populate the fields as follows.

```{=html}
<!-- -->
```
-   **Widget Title**: enter a title for the widget (e.g. "Activity Feed"). This is visible at the top of the screen.

-   **Widget Icon:** enter a relevant widget icon. The icon is visible just before the widget title. (If you want to change the icon, refer to the **Tip** in topic **17.4 Text widget**.)

-   **Header Colour:** enter the colour name or hex colour code for the background colour of the header (e.g. ![](media/image522.png){width="0.15833333333333333in" height="0.15833333333333333in"} [(orange)]{.mark}).

-   **Header Text Colour:** [enter the colour]{.mark} name or [hex colour code for the text colour of the header (e.g. #030B0C).]{.mark}

```{=html}
<!-- -->
```
-   Click on **Save Change(s)**.

## 17.16 Map widget

***Available in***: Dashboards, Bulletins, Notebooks and Website Builder

The map widget allows the user to add a choropleth map. It can be incorporated into Dashboards, Bulletins, Notebooks and Website Builder.

Fig. 17.13 shows an example of a configured map in a notebook.

Fig. 17.13. A configured map widget in a notebook

![](media/image557.png){width="4.808333333333334in" height="3.9in"}

To configure a map widget, follow the steps below.

-   Select **Menu** \> **Notebooks** \> **My Notebooks** \> click on **Create Notebook**. All the widgets are listed in the left-hand column.

-   Drag and drop a **Row** widget \> click on the **expand** ![](media/image505.png){width="0.24166666666666667in" height="0.24166666666666667in"} icon to expand the **Mapping** category \> drag and drop a **Map widget** onto the row \> click on it, and the widget editor opens, as shown below:

![](media/image558.png){width="6.416666666666667in" height="2.433333333333333in"}

-   Populate the fields as follows.

```{=html}
<!-- -->
```
-   **Title:** enter a title for the map. This is visible at the top of the screen.

-   **Location(s):** you can limit the source of data for the indicator used in the map by specifying the location source and its sub-options:

    **Either** set **Location source** as **Specific**: select a location via the **Location** drop-down menu (e.g. Nambutu), and data reported from a specific location are considered for the map.

    **Or** set **Location source** as **Of Type**: select the location from the **Location** drop-down menu (e.g. Nambutu) \> select location type from the **Location Type** drop-down menu (e.g. Provinces) \> set **Location** **Status** as **Active**, and data reported from the provinces of Nambutu with active status are considered for the map,.

    **Or** set **Location source** as **Location Group(s)**: select a **location group** from the drop-down menu (e.g. NGO A) (if you need to select multiple groups, keep selecting from the drop-down menu (e.g. NGO B, NGO C).

    **Or** set **Location source as User Location**: Once set as this option, only data reported from the **User Location** are considered.

-   **Query Type:** set as **Indicator** to specify a single indicator, or as **Complex** to generate a calculated value.

    **Either** set **Query Type** as **Indicator**: select the **Indicator** whose values you want to display in the map from the drop-down menu.

    **Or** set **Query Type** as **Complex**: enter an arithmetic formula in the **Formula** textbox \> click on **Add Variable** \> click on the **edit** ![](media/image529.png){width="0.20833333333333334in" height="0.20833333333333334in"} icon \> enter the variable name (e.g. "Consultations 5 and over") \> select Consultations 5 and over from the **Indicator** drop-down menu \> select the **Formula Aggregation Interval** (e.g. Week).

-   **Period:** select the date range in the **From** and **To** drop-down menus or directly from the **Quick** **Ranges** menu. The default **From** and **To** dates are today.

-   **Thresholds:** click on the **add** ![https://lh4.googleusercontent.com/Prm1-cZnhNmrn2GFWT94xFs6SKqAGA0_4L8dIteJTkbB3T8UpZUpOdCOfU7FpwDky4DPXatY2F_OgIZKE_kyuff_52Wrj3PvCkwfjd5j6GEWOfEs4tAWUZnIa_SSzO0rkk-874Zp](media/image530.png){width="0.1875in" height="0.1875in"} icon \> enter **min** and **max values** for the threshold and specify the colour via the colour picker drop-down menu (e.g. areas with data aggregates in the range 0--100 will be displayed in green, and areas with data aggregates in the range 500--1000 will be displayed in red), as shown below:

![](media/image559.png){width="3.7416666666666667in" height="1.4583333333333333in"}

The map location is filled with the colour of a threshold whose value is within the specified range.

-   **Legend**: set as **Show**:

    **Show** -- the legend is visible.

    **Hide** -- the legend is not visible.

-   **Opacity:** Enter the opacity of the map. Opacity determines how opaque or transparent a map is. It can take a value from **0.0 to 1.0.** The lower the value, the more transparent the map (e.g. 0.5 for 50% transparency).

-   **Base Geometry Colour:** choose the base geometry colour (inside the map).

-   **Background Colour:** choose the background colour (behind the map).

-   **Stroke Colour:** choose the stroke colour (border colour).

-   **Stroke Width:** enter the stroke width.

-   **Width:** enter the width in pixels, % or em (e.g. 100px, 20% or 300em).

-   **Height:** enter the height in pixels, % or em (e.g. 100px, 20% 300em).

-   **Show labels:** set as **Yes**.

    **Yes** -- The labels are visible.

    **No** -- The labels are not visible.

-   **Labelling style:** choose the labelling style (e.g. Default).

-   **Label Font Size (px):** enter the font size of the label.

-   **Label Colour:** choose the label colour.

-   **Label Threshold (gte):** enter the label threshold.

```{=html}
<!-- -->
```
-   Click on **Save Change(s)**.

## 17.17 Alerts map widget

***Available in***: Dashboards

The alerts map widget is a special purpose widget that allows the user to view the map location of selected alerts (Fig. 17.14). By default, it will display all alerts, irrespective of their stage, stage state or risk factor in two tabs: **active** and **inactive**.

Fig. 17.14. A configured alerts map widget

![](media/image560.png){width="6.43333552055993in" height="4.375in"}

Click on any of the alerts on the map (e.g. Bilnula PHCC) to view the report associated with the alert.

To configure an alerts map widget, follow the steps below.

-   Select **Menu** \> **Dashboards** \> click on **Create New** at the top right-hand corner of the screen.

-   Drag and drop a **Row** widget \> click on the **expand** ![](media/image505.png){width="0.24166666666666667in" height="0.24166666666666667in"} icon to expand the **User** category \> drag and drop an **Alerts Map** widget onto the row \> click on it, and the widget editor opens, as shown below:

![](media/image561.png){width="6.225in" height="3.475in"}

-   Populate the fields as follows.

```{=html}
<!-- -->
```
-   **Widget Title**: enter a title for the widget (e.g. "Consultations Alerts"). This is visible at the top of the screen.

-   **Widget Icon:** enter a relevant widget icon. The icon is visible just before the widget title. (If you want to change the icon, refer to the **Tip** in topic **17.4 Text widget**.)

-   **Header Colour:** enter the colour name or hex colour code for the background colour of the header (e.g. ![](media/image522.png){width="0.15833333333333333in" height="0.15833333333333333in"} [(orange)]{.mark}).

-   **Header Text Colour:** [enter the colour]{.mark} name or [hex colour code for the text colour of the header (e.g. #030B0C).]{.mark}

-   **Specific Alarm (Optional):** select an alarm (e.g. Consultations total).

-   **Alert Stage**: select the stage of the **Alert Workflow** process -- **Verification/Risk assessment/Risk characterization/Outcome**.

-   **Alert Stage State**: select the state of the alert stage -- **Pending/Active/Completed**.

-   **Alert Risk**: select the risk level of the alert -- **Low Risk/Moderate Risk/High Risk/Very High Risk**.

```{=html}
<!-- -->
```
-   Click on **Save Change(s**).

## 17.18 Series chart widget

***Available in***: Dashboards, Bulletins, Notebooks and Website Builder

The series chart widget allows the user to plot time series data using seven different types of visualizations: line, bar, area, scatter, spline and waterfall (Fig. 17.15).

The series chart widget allows the user to add multiple data series, and each series can have the same or different types of visualization.

Fig. 17.15. Examples of configured series charts widgets

+----------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
| **1. Line**                                                                                  | **2. Bar**                                                                      |
|                                                                                              |                                                                                 |
| ![](media/image562.png){width="2.7583333333333333in" height="1.4833333333333334in"} | ![](media/image563.png){width="2.725in" height="1.4416666666666667in"} |
+----------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
| **3. Scatter**                                                                               | **4. Area**                                                                     |
|                                                                                              |                                                                                 |
| ![](media/image564.png){width="2.75in" height="1.4833333333333334in"}               | ![](media/image565.png){width="2.7in" height="1.4666666666666666in"}   |
+----------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
| **5. Spline**                                                                                | **6. Waterfall**                                                                |
|                                                                                              |                                                                                 |
| ![](media/image566.png){width="2.7416666666666667in" height="1.4166666666666667in"} | ![](media/image567.png){width="2.6666666666666665in" height="1.4in"}   |
+----------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+

To configure the series chart widget, follow the steps below.

**Step 1.** Configure general settings.

-   Select **Menu** \> **Dashboards** \> click on **Create New** at the top right-hand corner of the screen.

-   Drag and drop a **Row** widget \> click on the **expand** ![](media/image505.png){width="0.24166666666666667in" height="0.24166666666666667in"} icon to expand the **Chart Component** category \> drag and drop a **Series chart** widget onto the row \> click on it, and the widget editor opens, as shown below:

![](media/image568.png){width="6.447916666666667in" height="3.5463538932633423in"}

-   Populate the fields as follows.

```{=html}
<!-- -->
```
-   **Chart Title** \[Mandatory\]: enter an appropriate chart title (e.g. "Measles Cases in Nambutu"). This is displayed at the top centre of the chart.

-   **Aggregation** \[Mandatory\]: select the aggregation period. Available options are **Daily**, **Weekly**, **Monthly** and **Yearly**. The aggregation period is used to aggregate the data while plotting the chart. It will be applied to all the data series added to the chart.

-   **Period:** select the date range in the **From** and **To** drop-down menus or directly from the **Quick Ranges** menu. The default **From** and **To** dates are today.

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** if the dataset doesn't have any corresponding value for that period, nothing is displayed on the chart.
  --------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-   **Title:** set as **Show**. This allows you to display or hide the chart title:

    **Show** -- the chart title is visible.

    **Hide** -- the chart title is not visible.

-   **Export:** set as **Show**. This controls the visibility of the export button on the chart rendered on the published website. The button allows export of the chart in various file formats, including .pdf, .png, .jpg and .svg:

    **Show** -- the export button is visible.

    **Hide** -- the export button is not visible.

-   **Zoom**: set as **Enabled**:

    **Enabled** -- allows you to zoom into the chart (to see an enlarged view).

    **Disabled** -- does not allow you to zoom into the chart.

-   **Navigator:** set as **Show**. Navigator is a small series below the main series, displaying a view of the entire dataset. It provides tools to zoom in and out on parts of the data as well as panning across the dataset:

    **Show** -- you can navigate around the timeline.

    **Hide** -- you can't navigate around the timeline.

-   **Legend**: set as **Show**. Legends are used to explain the chart. They display the series in a chart with a predefined symbol and name:

    **Show** -- the legend is visible.

    **Hide** -- the legend is not visible.

-   **Y Axis title:** set Y axis title as **Show** \> enter a title for the Y axis in the **Y Axis title** textbox.

-   **Y Axis format:** select an appropriate format from the drop-down menu (e.g. 0.00) to set the format of the Y axis value.

-   **Decimals:** set as **Show**. Decimals control whether the value of the Y axis tick can be in decimals or not:

    **Show** -- the Y axis tick value is in decimals.

    **Hide** -- the Y axis tick value is not in decimals.

-   **Max. Y value:** Specify the maximum value of Y axis ticks. If left empty, the maximum value is automatically calculated based on the data and the period specified. If it is set, the axis may be extended beyond the data range.

-   **Y Axis interval:** specify the interval of the tick marks in axis units.

-   **X Axis title:** set as **Show** \> enter a title for the X axis in the **X Axis title** textbox.

-   **X Axis labels:** set as **Show**. This controls the visibility of the labels on the X axis:

    **Show** -- the labels on the X axis are displayed.

    **Hide** -- the labels on the X axis are hidden.

-   **X Axis interval:** specify the interval of the tick marks in axis units.

-   **X Axis label rotation:** enter the degree of rotation for the X axis labels (e.g. 10). The X axis labels are rotated by the degree entered here.

-   **Chart width:** enter the chart width. You can specify the chart width in different formats, including pixels, % and em.

-   **Chart height:** enter the chart height. You can specify the chart height in different formats, including pixels, % and em.

-   **Stacked:** set to **Enabled**. Once enabled, the values of each series are stacked on top of each other.

**Step 2.** Configure the data tab.

-   Click on the **Data** tab \> click on **Add Series**, and a new series is added. Click on the **edit** ![https://lh5.googleusercontent.com/wp5n0n7qGLp-DslzBmC9GPavytOdBlEZImqer0WXSMxGchIwWjUyTklw5Zp3FmMd9_zqhinIbwTahDD3eYKSLCrH2-MqCtMtymE9GAaDV1ehkmxniJSQrA1FM2Vpoax7DtRhLedF](media/image99.png){width="0.22916666666666666in" height="0.21875in"} icon of the new series, and the screen below appears:

![](media/image569.png){width="6.416666666666667in" height="2.95in"}

-   Populate the fields as follows.

```{=html}
<!-- -->
```
-   **Title:** enter a title for the data series. If left empty, the indicator name is used as a title.

-   **Location Specification:** you can limit the source of data for the indicator used in the series by specifying the location source and its sub-options:

    **Either** set **Location Specification** as **Specific Location**: select a location via the location drop-down menu (e.g. Nambutu), and data reported from a specific location are considered for the series.

    **Or** set **Location Specification** as **Generator**: select the location whose Child location needs to be selected by the generator from the **Generator parent location** drop-down menu (e.g. Nambutu) \> select location type from the **Generator location type** drop-down menu (e.g. Provinces) \> set **Location Status** as **Active**, and data reported from the provinces of Nambutu with active status are considered for the series.

    **Or** set **Location Specification** as **Group(s)**: select a **location group** from the drop-down menu (e.g. NGO A) \> set **Group Output** as **Aggregate**. If set as **Aggregate**, the system performs group-wide aggregation of the data and displays data for each group. If set as **Individual**, the system performs location-wide aggregation of the data and displays data for each location of the group.

    **Or** set **Location Specification** as **User's Location**: once set as this option, only data reported from the **User's Location** are considered.

-   **Data Source**: you can set **Data Source** as **Indicator** for a single indicator, or as **Complex** to generate a calculated value:

    **Either** set **Data Source** as **Indicator** \> select the **Indicator** whose values you want to display in the chart from the drop-down menu.

    **Or** set **Data Source** as **Complex** \> enter an arithmetic formula in **Formula** textbox \> click on **Add Variable** \> click on the **edit** ![](media/image529.png){width="0.20833333333333334in" height="0.20833333333333334in"} icon \> enter the variable name (e.g. "Consultations 5 and over") \> select Consultations 5 and over from the indicator drop-down menu.

-   **Period**: set as **Inherit**:

    **Inherit** -- takes the period specified in the chart settings tab.

    **Override** -- does not take the period specified in the chart settings tab but it takes the data period specified in the fields below this option.

-   **Style**: select an appropriate visualization type (e.g. bar, line, spline).

-   **Colour**: select an appropriate colour from the drop-down menu (if **Style** is selected as **Line**, the line's colour changes to the colour chosen in this field). The colour of the line and tooltip border will change. The default colour is white.

-   **Line Width:** enter the line width of the chart, in pixels. The default width is 2.

-   **Line Style:** select an appropriate line style from the drop-down menu (e.g. dot). The **Line** **Style** option is available only for a line chart.

-   **Marker Radius:** enter the radius of the point marker (e.g. 10).

-   **Marker style**: set the marker style as **Square**. Marker style is the shape or symbol of the marker. Available options are **Circle**, **Square**, **Diamond**, **Triangle** and **Triangle-Down**.

```{=html}
<!-- -->
```
-   Add another series using the steps above, if required.

```{=html}
<!-- -->
```
-   Click on **Save Change(s)**.

## 17.19 Pyramid chart widget

***Available in***: Dashboards, Bulletins, Notebooks and Website Builder

The pyramid chart widget allows you to configure a pyramid chart on the website. This is divided into horizontal sections and is used to represent hierarchies.

Fig. 17.16 shows an example of a configured pyramid chart widget.

Fig. 17.16. A configured pyramid chart widget

![](media/image570.png){width="4.958333333333333in" height="2.65in"}

To configure the pyramid chart widget, follow the steps below.

**Step 1.** Configure general settings.

-   Select **Menu** \> **Dashboards** \> click on **Create New** at the top right-hand corner of the screen.

```{=html}
<!-- -->
```
-   Drag and drop a **Row** widget \> click on the **expand** ![](media/image505.png){width="0.24166666666666667in" height="0.24166666666666667in"} icon to expand the **Chart Component** category \> drag and drop a **Pyramid chart** widget onto the row \> click on it, and the widget editor opens.

![](media/image571.png){width="6.078425196850394in" height="3.305143263342082in"}

-   Populate the fields as follows.

```{=html}
<!-- -->
```
-   **Chart Title** \[Mandatory\]: enter an appropriate chart title (e.g. "Measles Cases in Nambutu"). This is displayed at the top centre of the chart.

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** to display the title on the chart, **Title** must be set as **Show** under **Controls**.
  --------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-   **Aggregation** \[Mandatory\]: select the aggregation period. Available options are **Daily**, **Weekly**, **Monthly** and **Yearly**. The aggregation period is used to aggregate the data while plotting the chart. It will be applied to all the data series added to the chart.

-   **Cumulative:** set as **Yes** to apply a sum.

-   **Group by Indicators**: set as **Yes**. If set as **Yes**, you should add more than one data series to the chart. For each series added, a layer of the pyramid is displayed. If set as **No**, the feature is disabled, and you should not add more than one series in the **Data** tab. If more than one is added if **Group by Indicators** is set as **No**, the system will consider the first one and ignore the rest of the series.

-   **Period:** select the date range in the **From** and **To** drop-down menus or directly from the **Quick Ranges** menu. The default **From** and **To** dates are today.

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** if the dataset doesn't have any corresponding value for that period, nothing is displayed on the chart.
  --------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-   **Title:** set as **Show**. This allows you to display or hide the chart title:

    **Show** -- the chart title is visible.

    **Hide** -- the chart title is not visible.

-   **Export:** set as **Show**. This controls the visibility of the export button on the chart rendered on the published website. The button allows export of the chart in various file formats, including .pdf, .png, .jpg and .svg:

    **Show** -- the export button is visible.

    **Hide** -- the export button is not visible.

-   **Zoom**: set as **Enabled**:

    **Enabled** -- allows you to zoom into the chart (to see an enlarged view).

    **Disabled** -- does not allow you to zoom into the chart.

-   **Navigator:** set as **Show**. Navigator is a small series below the main series, displaying a view of the entire dataset. It provides tools to zoom in and out on parts of the data as well as panning across the dataset:

    **Show** -- you can navigate around the timeline.

    **Hide** -- you can't navigate around the timeline.

-   **Legend**: set as **Show**. Legends are used to explain the chart. They display the series in a chart with a predefined symbol and name:

    **Show** -- the legend is visible.

    **Hide** -- the legend is not visible.

-   **Chart width**: enter the chart width. You can specify the chart width in different formats, including pixels, % and em.

-   **Chart height:** enter the chart height. You can specify the chart height in different formats, including pixels, **%** and em.

**Step 2.** Configure the data tab.

-   Click on the **Data** tab \> click on **Add Series**, and a new series is added. Click on the **edit** ![](media/image240.png){width="0.2916666666666667in" height="0.275in"} icon of the new series, and the screen below appears:

![](media/image572.png){width="6.216666666666667in" height="2.9in"}

-   Populate the fields as follows.

```{=html}
<!-- -->
```
-   **Title:** enter a title for the data series. If left empty, the indicator name is used as a title.

-   **Location Specification:** you can limit the source of data for the indicator used in the series by specifying the location source and its sub-options:

    **Either** set **Location Specification** as **Specific Location**: select a location via the location drop-down menu (e.g. Nambutu), and data reported from a specific location are considered for the series.

-   **Or** set **Location Specification** as **Generator**: select the location whose Child location needs to be selected by the generator from the **Generator parent location** drop-down menu (e.g. Nambutu) \> select location type from the **Generator location type** drop-down menu (e.g. Provinces) \> set **Location Status** as **Active**, and data reported from the provinces of Nambutu with active status are considered for the series.

    **Or** set **Location Specification** as **Group(s)**: select a **location group** from the drop-down menu (e.g. NGO A) \> set **Group Output** as **Aggregate**. If set as **Aggregate**, the system performs group-wide aggregation of the data and displays data for each group. If set as **Individual**, the system does location-wide aggregation of the data and displays data for each location of the group.

    **Or** set **Location Specification** as **User's Location**: once set as this option, only data reported from the **User's Location** are considered.

-   **Data Source**: you can set **Data Source** as **Indicator** for a single indicator, or as **Complex** to generate a calculated value:

    **Either** set **Data Source** as **Indicator** \> select the **Indicator** whose values you want to display in the chart from the drop-down menu.

    **Or** set **Data Source** as **Complex** \> enter an arithmetic formula in the **Formula** textbox \> click on **Add** **Variable** \> click on the **edit** ![](media/image529.png){width="0.20833333333333334in" height="0.20833333333333334in"} icon \> enter the variable name (e.g. "Consultations 5 and over") \> select Consultations 5 and over from the indicator drop-down menu.

-   **Period**: set as **Inherit**:

    **Inherit** -- takes the period specified in the chart settings tab.

    **Override** -- does not take the period specified in the chart settings tab, but it takes the data period specified in the fields below this option.

```{=html}
<!-- -->
```
-   Add another series using the steps above, if required.

-   Click on **Save Change(s)**.

## 17.20 Category widget

***Available in***: Dashboards, Bulletins, Notebooks and Website Builder

The category widget allows the user to visualize categorical variables in a pie, donut, arc or bar chart.

Fig. 17.17 shows examples of configured category widgets.

Fig. 17.17 Examples of configured category widgets

+------------------------------------------------------------------------------+----------------------------------------------------------------+
| **Pie chart (default)**                                                      | **Donut chart**                                                |
|                                                                              |                                                                |
| ![](media/image573.png){width="2.9in" height="2.699364610673666in"} | ![](media/image574.png){width="2.9in" height="2.7in"} |
+------------------------------------------------------------------------------+----------------------------------------------------------------+
| **Arc chart**                                                                | **Bar chart**                                                  |
|                                                                              |                                                                |
| ![](media/image575.png){width="2.9in" height="2.7in"}               | ![](media/image576.png){width="2.9in" height="2.7in"} |
+------------------------------------------------------------------------------+----------------------------------------------------------------+

To configure the category widget, follow the steps below.

-   Select **Menu** \> **Dashboards** \> click on **Create New** at the top right-hand corner of the screen.

**Step 1.** Configure general settings.

-   Drag and drop a **Row** widget \> click on the **expand** ![](media/image505.png){width="0.24166666666666667in" height="0.24166666666666667in"} icon to expand the **Chart Component** category \> drag and drop a **Category** chart onto the row \> click on it, and the widget editor opens, as shown below:

    ![](media/image577.png){width="6.0625in" height="3.3848950131233595in"}

-   Populate the fields as follows.

```{=html}
<!-- -->
```
-   **Chart Title** \[Mandatory\]: enter an appropriate chart title (e.g. "Measles Cases in Nambutu"). This is displayed at the top centre of the chart.

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** to display the title on the chart, **Title** must be set as **Show** under **Controls**.
  --------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-   **Sample Interval** \[Mandatory\]: select one of the intervals. Available options are **Daily**, **Weekly**, **Monthly** and **Yearly** (for example, if you select **Weekly**, the chart is rendered against weekly aggregated data).

-   **Group by Indicators**: set as **Yes**. If set as **Yes**, you should add more than one data series to the chart. For each series added, a layer of the chart is displayed. If set as **No**, the feature is disabled, and you should not add more than one series in the **Data** tab. If more than one is added if **Group by Indicators** is set as **No**, the system will consider the first one and ignore the rest of the series.

-   **Period:** select the date range in the **From** and **To** drop-down menus or directly from the **Quick Ranges** menu. The default **From** and **To** dates are today.

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** if the dataset doesn't have any corresponding value for that period, nothing is displayed on the chart.
  --------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-   **Chart** **Title:** set as **On**. This control allows you to display or hide the chart title:

    **On** -- the chart title is visible.

    **Off** -- the chart title is not visible.

-   **Legend**: set as **Show**. Legends are used to explain the chart. They display the series in a chart with a predefined symbol and name:

    **Show** -- the legend is visible.

    **Hide** -- the legend is not visible.

-   **Chart Style**: Select an appropriate visualization type. Different types of visualizations are **Default** (Pie), **Donut**, **Arc** and **Bar Graph**.

```{=html}
<!-- -->
```
-   For the **Bar Graph** visualization type, configure the following:

```{=html}
<!-- -->
```
-   **Y Axis label:** enter a label for the Y axis (e.g. **"**Number of cases").

-   **Y Axis format:** select an appropriate format from the drop-down menu (e.g. 0.00) to set the format of the Y axis value.

-   **Y Axis decimals:** set as **Show**. Decimals control whether the value of the Y axis tick can be in decimals or not:

    **Show** -- the Y axis tick value is in decimals.

    **Hide** -- the Y axis tick value is not in decimals.

-   **Slice Ordering:** select slice ordering based on title or values (e.g. value ascending).

-   **Width:** enter the width value (e.g. 300) \> select the format (e.g. px).

-   **Height**: enter the height value (e.g. 500) \> select the format (e.g. px).

-   **Slices with no data**: set to **Show** to display slices with no data, or set to **Hide** to hide slices with no data.

**Step 2.** Configure the data tab.

-   Click on the **Data** tab \> click on **Add Category**, and a new series is added. Click on the **edit** ![](media/image529.png){width="0.20833333333333334in" height="0.20833333333333334in"} icon of the new series, and the screen below appears:

![](media/image578.png){width="6.125in" height="3.3049475065616796in"}

-   Populate the fields as follows.

```{=html}
<!-- -->
```
-   **Slice Label:** enter a label for the slice. This appears at the top of the slice.

-   **Colour:** Select a colour from the drop-down menu. The slice is displayed in the selected colour.

-   **Location Specification:** You can limit the source of data for the indicator that is used in the series by specifying the location source and its sub-options:

    **Either** set **Location Specification** as **Specific Location**: select a location via the location drop-down menu (e.g. Nambutu), and data reported from a specific location are considered for the series.

    **Or** set **Location Specification** as **Generator**: select the location whose Child location needs to be selected by the generator from the **Generator parent location** drop-down menu (e.g. Nambutu) \> select location type from the **Generator location type** drop-down menu (e.g. Provinces) \> set **Location Status** as Active, and data reported from the provinces of Nambutu with active status are considered for the series.

    **Or** set **Location Specification** as **Group(s)**: select a **location group** from the drop-down menu (e.g. NGO A) \> set **Group Output** as **Aggregate**. If set as **Aggregate**, the system performs group-wide aggregation of the data and displays data for each group. If set as **Individual**, the system performs location-wide aggregation of the data and displays data for each location of the group.

    **Or** set **Location Specification** as **User's Location**: once set as this option, only data reported from the **User's Location** are considered.

-   **Data Source**: you can set **Source Type** as **Indicator** for a single indicator, or as **Complex** to generate a calculated value:

    **Either** set **Source Type** as **Indicator** \> select the **Indicator** whose values you want to display in the chart from the drop-down menu \> select **Reduction Type** to apply **Sum** or **Average/Median** to the indicator values.

-   **Or** set **Source Type** as **Complex** \> enter an arithmetic formula in the **Formula** textbox \> click on **Add Variable** \> click on the **edit** ![](media/image529.png){width="0.20833333333333334in" height="0.20833333333333334in"} icon \> enter the variable name (e.g. "Consultations 5 and over") \> select Consultations 5 and over from the indicator drop-down menu.

-   **Period**: set as **Inherit**.

    **Inherit** -- takes the period specified in the chart settings tab.

    **Override** -- does not take the period specified in the chart settings tab but it takes the data period specified in the fields below this option.

```{=html}
<!-- -->
```
-   Click on **Save Change(s)**.

## 17.21 Table widget

***Available in***: Bulletins, Notebooks and Website Builder

The table widget allows the user to display location-wise tabular data. By default, it adds columns for the location and parent location names. After that, user-defined columns are displayed in the order specified.

Fig. 17.18 shows an example of a configured table widget in a notebook.

Fig. 17.18. A configured table widget in a notebook

![](media/image579.png){width="4.802083333333333in" height="2.7031255468066493in"}

To configure a table widget in Notebooks, Bulletins and Website Builder, follow the steps below.

-   Select **Menu** \> **Notebooks** \> **My Notebooks** \> click on **Create Notebook**. All the widgets are listed in the left-hand column.

-   Drag and drop a **Table** widget onto the middle section \> click on it, and the widget editor opens, as shown below:

![](media/image580.png){width="6.341666666666667in" height="3.158333333333333in"}

-   Populate the fields as follows.

```{=html}
<!-- -->
```
-   **Title:** enter a name for the table.

-   **Location Specification:** you can limit the source of data for the indicator that is used in the table by specifying the location source and its sub-options:

    **Either** set **Location Specification** as **Specific Location**: select a location via the location drop-down menu (e.g. Nambutu), and data reported from a specific location are considered for the table.

-   **Or** set **Location Specification** as **Generator**: select the location whose child location needs to be selected by the generator from the **Generator parent location** drop-down menu (e.g. Nambutu) \> select location type from the **Generator location type** drop-down menu (e.g. Provinces) \> set **Location Status** as **Active**, and data reported from the provinces of Nambutu with active status are considered for the series.

    **Or** set **Location Specification** as **Group(s)**: select a **location group** from the drop-down menu (e.g. NGO A) \> set **Group Output** as **Aggregate**. If set as **Aggregate**, the system performs group-wide aggregation of the data and displays data for each group. If set as **Individual**, the system performs location-wide aggregation of the data and displays data for each location of the group.

    **Or** set **Location Specification** as **User's Location**: once set as this option, the data reported from the **User's Location** are considered.

-   **Column Header**: set as **Show**. This controls the visibility of the column heading:

    **Show** -- the column heading is visible.

    **Hide** -- the column heading is hidden.

-   **Additional Class Name**: enter the name of the Cascading Style Sheets (CSS) class. You can apply styling through the CSS class, and this is defined in the CSS settings.

-   **Hide rows with 0 or no data**: set as **Yes**:

    **Yes** -- rows with 0 or no data in all cells are hidden.

    **No** -- rows with 0 or no data in all cells are not hidden.

-   **Sorting column**: you can specify the order by column name from the drop-down menu (e.g. **Location Name Asc.**).

-   **Limit rows**: this allows you to limit the table rows while rendering the table. Provide the maximum row count to be displayed (e.g. 10). If more rows of data than the maximum value specified here are available, the rest of the rows are ignored.

**Step 2.** Configure the data tab.

-   Click on the **Data** tab \> click on **Add Column**, and a new column is added. Click on the **edit** ![](media/image99.png){width="0.22984689413823273in" height="0.2202701224846894in"} icon of the new column, and the screen below appears:

-   

![](media/image581.png){width="6.495276684164479in" height="3.404861111111111in"}

-   Populate the fields as follows.

```{=html}
<!-- -->
```
-   **Title:** enter a title for the column.

-   **Data Source:** set **Source Type** as **Indicator** for a single indicator, or as **Complex** to generate a calculated value:

    **Either** set **Source Type** as **Indicator** \> select the **Indicator** whose values you want to display in the table from the drop-down menu \> select **Reduction** to apply **Sum** or **Avg.** (Average/Median) to the indicator values.

    **Or** set **Source Type** as **Complex**: enter an arithmetic formula in the **Formula** textbox \> click on **Add Variable** \> click on the **add** ![https://lh5.googleusercontent.com/wp5n0n7qGLp-DslzBmC9GPavytOdBlEZImqer0WXSMxGchIwWjUyTklw5Zp3FmMd9_zqhinIbwTahDD3eYKSLCrH2-MqCtMtymE9GAaDV1ehkmxniJSQrA1FM2Vpoax7DtRhLedF](media/image99.png){width="0.22916666666666666in" height="0.21875in"} icon \> enter the variable name (e.g. "Consultations 5 and over") \> select Consultations 5 and over from the indicator drop-down menu.

-   **Period**: select the date range in the **From** and **To** drop-down menus or directly from the **Quick** **Ranges** menu. The default **From** and **To** dates are today.

-   **Value Formatting**: choose the formatting style of the value (e.g. 0.00).

-   **Prefix**: enter a prefix for the value that will be concatenated with it accordingly.

-   **Suffix**: enter a suffix for the value that will be concatenated with it accordingly.

-   **Value Colouring**: once enabled, you can provide value colouring ranges. Click on the **add** ![](media/image530.png){width="0.1875in" height="0.1875in"} icon \> enter **min** and **max** values for the range and specify the colour via the colour picker drop-down menu, as shown below:

![](media/image531.png){width="6.008333333333334in" height="1.7916666666666667in"}

The value is displayed with the colour of the **Value range** whose criteria are satisfied.

-   **Value Mapping:** once enabled, instead of the original value, the mapped value is displayed. Click on the **add** ![](media/image530.png){width="0.1875in" height="0.1875in"} icon \> enter **min** and **max** values for the range and specify the mapped value. Each value mapping range has two number inputs and a textbox for a mapped value.

```{=html}
<!-- -->
```
-   Click on **Save Change(s)**.

Please note that designing tables (shading columns, borders) requires HTML coding. If you are not familiar with HTML, please contact the EWARS Super Administrator for support.

## 17.22 Menu widget

***Available in***: Website Builder

This section assumes that you have already created a website for your account. Refer to **Chapter 22. Website Builder** for more information on how to do this.

The menu widget provides page navigation capability for a website. It enables the user to create main menu and submenu items, which need to be linked to the relevant pages. These pages are displayed between the header and footer sections on the website. The menu is displayed horizontally.

It is recommended that the menu widget should be configured in the header section so that it appears at the top of the page.

Fig. 17.19 shows an example of what a configured menu widget looks like on a published website.

Fig. 17.19. A configured menu widget on a published website

![](media/image582.png){width="6.375in" height="1.9083333333333334in"}

To configure a Menu widget, follow the steps below.

**Step 1.** Configure general settings.

-   Select **Menu** \> **Website Builder**. Click on the **edit** ![](media/image231.png){width="0.2916666666666667in" height="0.2833333333333333in"} icon next to any of the websites.

-   Drag and drop a **Row** widget \> drag and drop a **Menu** widget onto the row \> click on it, and the widget editor opens, as shown below:

![](media/image583.png){width="5.841666666666667in" height="1.525in"}

**Step 2.** Add a menu item to the menu bar.

-   Click on **Add Menu**, and a menu is added \> click on the **add** ![](media/image584.png){width="0.2in" height="0.2in"} icon \> enter a **Menu Title** (e.g. "EWARS Technical Guidance") \> select a page from **Page** drop-down menu to link to the menu (e.g. Technical Guidance), as shown below:

![](media/image585.png){width="5.825in" height="2.533333333333333in"}

**Step 3.** Add a submenu item inside a menu item.

-   Enable the **Secondary Menu?** option \> click on **Add Menu Items**, and a submenu item is added. Click on the **edit** ![](media/image99.png){width="0.225in" height="0.21666666666666667in"} icon in the submenu \> enter a **Menu Item Name** \> select the page to link to the submenu item name (e.g. Homepage), as shown below:

![](media/image586.png){width="6.15in" height="3.0083333333333333in"}

-   Click on **Save Change(s)**.

## 17.23 Text widget in Website Builder

***Available in***: Website Builder

The text widget is used to display textual content on a webpage. Fig. 17.20 shows an example of what a text widget looks like on a published website.

Fig. 17.20. A configured text widget on a published website

![](media/image587.png){width="6.108333333333333in" height="1.825in"}

To configure an text widget on the website, follow the steps below.

-   Select **Menu** \> **Website Builder**. Click on the **edit** ![](media/image231.png){width="0.2916666666666667in" height="0.2833333333333333in"} icon next to any of the websites.

-   Drag and drop a **Row** widget \> click on the **expand** ![](media/image505.png){width="0.24166666666666667in" height="0.24166666666666667in"} icon to expand the **Content** **category** \> drag and drop a **Text** widget onto the row \> click on it, and the widget editor opens, as shown below:

![](media/image588.png){width="6.333333333333333in" height="3.5833333333333335in"}

-   Populate the fields as follows.

```{=html}
<!-- -->
```
-   **Content:** enter a relevant paragraph of text.

-   **Text Font Size:** enter the font size for the text (e.g. 14px). The default font size is set as 12 pixels.

-   **Text Colour:** enter the colour for the text in (hex code or RGB or the name of the colour). For example, for the colour red, you can enter the hex value 0xFF0000, **or** RGB (255, 0, 0) **or** the name "red".

-   **Letter Spacing:** enter the spacing for the text (e.g. 2). This increases or decreases the space between the letters in a text. The default value is 1.

-   **Line Height:** enter the line height (e.g. 10). This specifies the vertical distance between the lines of text by adding space above and below the lines. Negative values are not allowed. If left blank, the default spacing is used by the system. The ideal size for line height is 15--20.

-   **Text Style:** choose any of the given styles. Available options are **Bold**, **Italic** and **Underline**. The default value is no text style selected. You can select one or more styles. To select all styles, click on **Select All**.

-   **Margin:** enter the margin (e.g. 12). This creates white space around the text. The default is 10. This field accepts both positive and negative values. A positive value places it away from its parent container, while a negative value places it closer to the parent container.

```{=html}
<!-- -->
```
-   Click on **Save Change(s)**.

## 17.24 Image widget in Website Builder

***Available in***: Website Builder

The image widget in Website Builder lets you add an image to a website. It also allows you to set up a heading for the image if needed, and this heading can also be given under the image description. Fig. 17.21 shows an example of what the image widget looks like on a published website.

Fig. 17.21. A configured image widget on a published website

![](media/image589.png){width="4.364583333333333in" height="3.2916666666666665in"}

To configure an image widget, follow the steps below.

-   Drag and drop a **Row** widget \> click on the **expand** ![](media/image505.png){width="0.24166666666666667in" height="0.24166666666666667in"} icon to expand the **Content** category \> drag and drop an **Image** widget onto the row \> click on it, and the widget editor opens, as shown below:

![](media/image590.png){width="6.553129921259843in" height="3.2629122922134735in"}

-   Populate the fields as follows.

```{=html}
<!-- -->
```
-   **Image URL** \[Mandatory\]: you can either upload the image from your local drive or add the link to the image directly:

    **Either** upload an image from your local drive: click on the **upload** ![](media/image591.png){width="0.2833333333333333in" height="0.275in"} icon to upload a new image saved on your laptop/desktop. It is uploaded as web content, and the newly created URL is populated automatically in the textbox beside it. It is important to ensure that the image is already properly sized for display on a webpage. Providing a very large image at high resolution may slow down delivery of the webpage to end-users.

    **Or** add the link to the image directly: copy and paste an existing URL or type the URL manually into the textbox. The address specified must resolve to a publicly accessible image. The image file is not copied to EWARS, but remains in its source location. EWARS fetches it when displaying it on the page.

    ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"} **Note:** there is an inherent risk in this approach -- if you choose a URL to a location that you don't control (for example, if you reference an image on another website or via a search engine) and if that image is ever removed by its owner, it will disappear from EWARS.

-   **Link URL and link action:** if you want to allow a web user to download a file or to be redirected to any other website by clicking on the image, follow the steps below.

    **Either** configure the image to open a website or webpage in a new window or tab (e.g. once the user clicks on this image, it redirects to http://who.int): set **Link Action** as **Redirect** and enter the **Link URL** of the website/webpage that is to be opened. For example, if the **Link URL** is set as <https://www.who.int>, when you click on the image, the WHO webpage opens.

    **Or** configure the image to download a file: select **Link Action** as **Download** \> enter the **Link URL** for a file that is to be downloaded \> enter an **Image Description** for the image (this appears as a heading at the top of the image) \> enter the **Frame Width (in px)** of the image container (e.g. 600) \> enter the **Frame Height (in px)** of the image container (e.g. 400) (this is the sum of image height and image heading in pixels) \> enter the **Opacity** of the image (this determines how opaque or transparent an image is -- it can take a value from 0.0 to 1.0, and the lower the value, the more transparent the image (e.g. 0.5 for 50% transparency) \> enter a **Box Shadow** for the image (this attaches one or more shadows to an image -- it takes a value in the format **x-offset y-offset blur spread colour** (e.g. 1px 1px 1px 1px #333) \> enter a **Margin (in px)** for the image (this creates extra space around the image with respect to the parent container): enter the value of the space that you want around the image (e.g. 10, -10, 20, -20). This accepts both positive and negative values. A positive value places it away from its parent container, while a negative value places it closer to the parent container.

```{=html}
<!-- -->
```
-   Click on **Save Change(s)**.

## 17.25 Enhanced table widget

***Available in***: Dashboards, Bulletins, Notebooks and Website Builder

The enhanced table widget is an enhanced version of the table widget. The primary advantage of using this widget is improvement in performance while loading the widget. Fig. 17.22 shows an example of a configured enhanced table widget in a notebook**.**

Fig. 17.22. A configured enhanced table widget in a notebook

![](media/image592.png){width="6.78125in" height="3.1927088801399823in"}

To configure an enhanced table widget, follow the steps below.

**Step 1.** Configure general settings.

-   Select **Menu** \> **Notebooks** \> **My Notebooks** \> click on **Create Notebook**. All the widgets are listed in the left-hand column.

-   Drag and drop a **Row** widget \> drag and drop an **Enhanced Table** widget onto the middle section \> click on it, and the widget editor opens, as shown below:

![](media/image593.png){width="6.713542213473316in" height="3.7916666666666665in"}

-   Populate the fields as follows.

```{=html}
<!-- -->
```
-   **Title:** enter a name for the table.

-   **Source:** You can limit the data for the indicator used in the table by specifying the source and its sub-options:

    Either set **Source** as **Forms**: only data reported from **Forms** and their related indicators will be considered. To consider data reported from a specific form, select **Specific Form** under **Source form** \> select the form name from the **Select Form** drop-down menu (e.g. Weekly EWARS Reporting Form) \> set **Apply condition on fields** as **Yes** \> select the form field from the drop-down menu (e.g. Under 5 cases \[AWD\]) \> select a **Condition** from the drop-down menu, (e.g. **Is equal to**) \> enter the number in the box (e.g. 10). To add another condition, click on the **add** ![](media/image594.png){width="0.17708333333333334in" height="0.22916666666666666in"} icon and repeat the steps above. After adding multiple conditions, if you want all conditions to be true, select **All** from the drop-down menu or select **Any** if you want any one of the conditions to be true.

    **Or** set **Source** as **Alerts**: only data reported from **Alerts** and their related indicators will be considered. To consider data reported from specific alarms, set **Source Alarm** as **Selected Alarms** \> select one or more alarms from the **Select Alarms** drop-down menu (e.g. Cholera, Measles).

    **Or** set **Source** as **Performance indicators**: only data reported from performance indicators (i.e. **System indicators** \> **Form Submissions** \> timeliness, completeness, etc.) will be considered.

-   **Group by:** this allows you to group the data based on **Time Interval**, **Reporting Location**, **Location type** or **Form field**. Note: grouping by **Form field** is only available for a **Source** set as **Forms**; grouping by **Alert Data** is only available for a **Source** set as **Alerts**. You can select any one, according to your requirements:

    **Either** set **Group by** as **No Grouping**: if this is selected, no grouping is performed on the data.

    **Or** set **Group by** as **Time Interval**: select a suitable interval. Available options are **Day**, **Week**, **Month** and **Year**. For example, if the selection is **Week**, the table shows weekly data.

    **Or** set **Group by** as **Reporting Location**: data are grouped on the basis of the locations from which they were reported -- for example, you can use this to form a group using all the reporting locations in Nambutu for the weekly EWARS reporting form.

    **Or** set **Group by** as **Location type**: select a suitable location type (e.g. Provinces) from the **Location Type** drop-down menu. For example, if the selection is Provinces, the data are grouped on the basis of the available province.

    **Or** set **Group by** as **Locations**: select one or more locations (e.g. Aimal, Dirran, Jobrar) from the **Select Locations** drop-down menu. For example, if you select Aimal and Dirran, the data are grouped for only those locations.

    **Or** set **Group by** as **Location Group(s)**: the data are grouped on the basis of the location group. Select **All** in the **Groups** field if you want to group data for all the available groups. If you want to group data for specific groups only, select **Selected** in the **Groups** field and select one or more groups from the **Location Group(s)** drop-down menu.

    **Or** set **Group by** as **Form field**: select a form name from the **Select Form** drop-down menu (e.g. Weekly EWARS Reporting Form) \> select an appropriate field from the **Form field** drop-down menu (e.g. Morbidity and Mortality: Acute Watery Diarrhoea (AWD): Under 5 cases). The data are grouped on the basis of the selected form field.

    **Or** set **Group by** as **Alert Data**: select an appropriate option from the **Column** drop-down menu (e.g. Alarm Name). The data are grouped on the basis of the name of the alarm.

-   **Column Title:** enter a name for the **Group by** column.

-   **Show totals**: set as **Enabled**:

> **Enabled** -- the sum of an entire column is visible in the last row.
>
> **Disabled** -- the sum of an entire column is not visible.

-   **Location Spec.:** you can limit the source of data for the indicator used in the widget by specifying the location source:

    **Either** set **Location spec.** as **Specific Location**: select a location via the location drop-down menu (e.g. Nambutu). The data reported from a specific location are considered.

    **Or** set **Location spec.** as **Locations**: select one or more locations via the select locations drop-down menu (e.g. Aimal, Dirran). The data reported from all added locations are considered.

    **Or** set **Location spec.** as **Location Group(s)**: select a location group from the drop-down menu (e.g. NGO A, NGO B). The data reported from any added groups are considered.

    **Or** set **Location spec.** as **User's Location**: once set as this option, only data reported from the **User's Location** are considered.

-   **Period:** select the date range in the **From** and **To** drop-down menus or directly from the **Quick Ranges** menu. The default **From** and **To** dates are today.

-   **Value Aliasing:** set to **Enabled**. This allows you to display an alias name for each cell of the **Group by** column. Note: this function is available every time you aggregate data by a group -- it is applicable to all data aggregation groups except **No Grouping**. If **No Grouping** is selected, value aliasing will not appear for you to enable the function.

    **Enabled** -- value aliasing is performed. For example, if you want to display Aimal as Province 1 and Dirran as Province 2 \> click on **Fetch** to display the cell values of the **Group by** column \> enter "Province 1" under **Alias** for Aimal and "Province 2" under **Alias** for Dirran. Value aliasing also allows you to hide any row from the table. For example, if you want to hide the first row, click on the **Exclude** box in the first row with the original value Aimal \> click on **Save Change(s)**. The first row is excluded from the table.

    **Disabled** -- value aliasing is not performed.

-   **Hide rows with 0 or no data**: set as **Yes**:

    **Yes** -- rows with 0 or no data in all cells are hidden.

    **No** -- rows with 0 or no data in all cells are not hidden.

-   **Sorting column:** you can specify the order by column name from the drop-down menu (e.g. Location Name Asc).

-   **Limit rows:** this allows you to limit table rows while rendering. Provide the **maximum row count** to be displayed (e.g. "10"). If more rows of data than the maximum value specified here are available, the rest of the rows are ignored.

-   **Column Header:** set as **Show**. This controls the visibility of the column heading:

    **Show** -- the column heading is visible.

    **Hide** -- the column heading is hidden.

-   **Table CSS Class:** enter the name of the CSS class. You can apply styling through the CSS class, and it is defined in the CSS settings.

**Step 2.** Configure the data tab.

-   Click on the **Data** tab \> click on **Add Column**, and a new column is added. Click on the **edit** ![](media/image99.png){width="0.22984689413823273in" height="0.2202701224846894in"} icon of new column, and the screen below appears:

![](media/image595.png){width="6.734375546806649in" height="3.7379790026246718in"}

-   Populate the fields as follows.

```{=html}
<!-- -->
```
-   **Title:** enter a title for the column.

-   **Description:** enter a description for the column.

-   **Source Type:** you can set **Source Type** as **Indicator** for a **single indicator**, or as **Complex** to generate a calculated value:

    **Either** set **Source Type** as **Indicator**: select the **Indicator** whose values you want to display in the table from the drop-down menu. For example, if you want to display all the alerts triggered for the Measles alarm within 72 hours, set **Indicator source** as **System** \> select **Alerts** \> select Measles from the **Alarm** drop-down menu \> select **Alerts Triggered** from the **Dimension** drop-down menu \> select the appropriate event from the **Likely Event** drop-down menu \> select **Verified within** from the **Include** drop-down menu \> enter "72" in the **No. of hours** box.

    **Or** set **Source Type** as **Complex**: enter an arithmetic formula in the **Formula** textbox \> click on **Add** **Variable** \> click on the **edit** ![](media/image99.png){width="0.22984689413823273in" height="0.2202701224846894in"} icon \> enter the variable name (e.g. "Consultations 5 and over") \> select Consultations 5 and over from the **Indicator** drop-down menu.

-   **Period**: set to **Inherit**:

    **Inherit** -- takes the period specified in the table settings tab.

    **Override** -- does not take the period specified in the table settings tab but takes the data period specified in the fields below this option.

-   **Hide This Column:** set as **No**. This control allows you to display or hide the column in the table:

    **No** -- the column is visible.

    **Yes** -- the column is not visible.

-   **Value Formatting:** choose the formatting style of the value (e.g. 0.00).

-   **Prefix:** enter a prefix for the value that will be concatenated with it accordingly.

-   **Suffix:** enter a suffix for the value that will be concatenated with it accordingly.

-   **Value Mapping:** once enabled, instead of the original value, the mapped value is displayed. Click on the **add** ![](media/image596.png){width="0.25in" height="0.2421872265966754in"} icon \> enter **min** and **max** values for the range and specify the mapped value. Each value mapping range has two number inputs and a textbox for a mapped value.

Similarly, add another column if required.

-   Click on **Save Change(s)**.

## 17.26 Enhanced map widget

***Available in***: Dashboards, Bulletins, Notebooks and Website Builder

The enhanced map widget allows the user to add a choropleth map. It is an enhanced version of the map widget. The primary advantage of using this widget is improvement in performance while loading the widget.

Fig. 17.23 shows an example of a configured enhanced map widget in a notebook.

Fig. 17.23. A configured enhanced map widget in a notebook

![](media/image597.png){width="6.625in" height="3.776042213473316in"}

To configure an enhanced map widget, follow the steps below.

-   Select **Menu** \> **Notebooks** \> **My Notebooks** \> click on **Create Notebook**. All the widgets are listed in the left-hand column.

-   Drag and drop a **Row** widget \> click on the **expand** ![](media/image505.png){width="0.24166666666666667in" height="0.24166666666666667in"} icon to expand the **Mapping** category \> drag and drop an **Enhanced map** widget onto the row \> click on it, and the widget editor opens, as shown below:

![](media/image598.png){width="6.572916666666667in" height="3.494792213473316in"}

-   Populate the fields as follows.

```{=html}
<!-- -->
```
-   **Title:** enter a title for the map.

-   **Display by:** select the location type for which you want to display the map. For example, if you want to display a map for the provinces of Nambutu, select Provinces from the **Display by** drop-down menu.

-   **Location spec.:** you can limit the source of data for the indicator used in the map by specifying the location source and its sub-options:

    **Either** set **Location spec.** as **Specific Location**: select a location via the **Location** drop-down menu (e.g. Nambutu), and the data reported from a specific location are considered for the map.

    **Or** set **Location spec.** as **Locations**: select one or more locations (e.g. Aimal, Dirran, Jobrar) from the **Select Locations** drop-down menu. For example, if you select Aimal and Dirran, only the data reported from those locations are considered.

    **Or** set **Location spec.** as **Location Group(s)**: select one or more groups from the **Location Group(s)** drop-down menu. For example, if you select NGO A and NGO B, only the data reported from those location groups are considered.

-   **Or** set **Location spec.** as **User's Location**: once set as this option, only the data reported from the **User's Location** are considered.

-   **Query Type**: you can set **Query Type** as **Indicator** for a single indicator, or as **Complex** to generate a calculated value:

    **\
    Either** set **Query Type** as **Indicator**: select the **Indicator** whose values you want to display in the map from the drop-down menu.

    **Or** set **Query Type** as **Complex**: enter an arithmetic formula in the **Formula** textbox \> click on **Add Variable** \> click on the **edit** ![](media/image529.png){width="0.20833333333333334in" height="0.20833333333333334in"} icon \> enter the variable name ( e.g. "Consultations 5 and over") \> select Consultations 5 and over from the **Indicator** drop-down menu \> select a **Formula Aggregation Interval** (e.g. Week).

-   **Period:** select the date range in the **From** and **To** drop-down menus or directly from the **Quick Ranges** menu. The default **From** and **To** dates are today.

-   **Thresholds:** click on the **add** ![https://lh4.googleusercontent.com/Prm1-cZnhNmrn2GFWT94xFs6SKqAGA0_4L8dIteJTkbB3T8UpZUpOdCOfU7FpwDky4DPXatY2F_OgIZKE_kyuff_52Wrj3PvCkwfjd5j6GEWOfEs4tAWUZnIa_SSzO0rkk-874Zp](media/image530.png){width="0.1875in" height="0.1875in"} icon \> enter **min** and **max** values for the threshold and specify the colour via the colour picker drop-down menu, as shown below:

![](media/image559.png){width="3.7416666666666667in" height="1.4583333333333333in"}

The map location is filled with the colour of a threshold whose value is within the specified range.

-   **Legend**: set as **Show**:

    **Show** -- the legend is visible.

    **Hide** -- the legend is not visible.

-   **Base Geometry Colour:** choose the base geometry colour (inside the map).

-   **Hover colour:** choose the hover colour. When you hover over a particular region on the map, its colour changes.

-   **Background colour:** choose the background colour (behind the map).

-   **Stroke colour:** choose the stroke colour (border colour).

-   **Stroke width:** enter the stroke width.

-   **Width:** enter the width in pixels, % or em (e.g. 100px, 20% or 300em).

-   **Height:** enter the height in pixels, % or em (e.g. 100px, 20% or 300em).

-   **Show Labels:** Set as **Yes**.

    **Yes** -- The labels are visible.

    **No** -- The labels are not visible.

-   **Label Font Style(px):** enter the font size of the label.

-   **Label Colour:** choose the label colour.

-   **Label Threshold (gte):** Enter the label threshold.

```{=html}
<!-- -->
```
-   Click on **Save Change(s)**.

## 17.27 Carousel widget

***Available in***: Website Builder

The carousel widget is a slideshow of images in a single section on your website. It allows the user to display slides consisting of images, with optional descriptions. It can automatically change the display images with or without text after a predefined number of seconds, or they can be changed manually.

Fig. 17.24 shows an example of what a configured carousel widget looks like on a published website.

Fig. 17.24. A configured carousel widget on a published website

![](media/image599.png){width="5.27083552055993in" height="4.239583333333333in"}

To configuring a carousel widget, follow the steps below.

-   Select **Menu** \> **Website Builder**. Click on the **edit** ![](media/image231.png){width="0.2916666666666667in" height="0.2833333333333333in"} icon next to any of the websites.

-   Drag and drop a **Row** widget \> drag and drop a **Carousel** widget onto the row \> click on it, and the widget editor opens, as shown below:

> ![](media/image600.png){width="6.458333333333333in" height="3.3in"}

-   Populate the fields as follows.

```{=html}
<!-- -->
```
-   **Width:** enter an image **width** in percentage (e.g. 50). The default is 100%, and this matches the width of the cell.

-   **Height:** enter the image **height** in percentage (e.g. 50). The default is 100% and this matches the height of the cell.

-   **Allow Autoplay:** once enabled, the images automatically change within the interval defined, or you need to click to view the slideshow of images one by one.

-   **Interval:** enter the image rollover **interval**. The default is 3 seconds.

By default, two images are added, but you can add more images via the following steps.

-   Click on **Add Images**, and the screen below appears:

![](media/image601.png){width="6.3in" height="2.225in"}

-   Click on the **edit** ![](media/image99.png){width="0.225in" height="0.21666666666666667in"} icon, and the **Image URL** and **Image Text** options below appear:

![](media/image602.png){width="5.325in" height="1.8166666666666667in"}

![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"} **Note:** to upload any image, the image needs to be stored in your computer or uploaded to web content in EWARS. You should not directly copy an image URL from the web.

Follow the steps below to upload preferred images to web content, where all images will be stored.

-   Select **Menu** \> **Web Content** \> click on **Upload Files** \> enter the **Folder Path** (e.g. Images) \> click on **Upload** \> double-click on the image file, and it is uploaded.

Once you have uploaded the image in web content, follow the instructions below to add the image URL to the carousel widget.

-   Enter the **URL** of the uploaded image \> enter a caption that describes the image in **Image Text**. This caption is displayed at the bottom centre of the image.

-   Click on **Save Change(s)**.

To delete an image, click on the **delete** ![](media/image603.png){width="0.2in" height="0.2in"} icon.

## 17.28 Video widget

***Available in***: Website Builder

You can add videos to the website using the video widget. The video you want to add needs to be uploaded on YouTube already.

Fig. 17.25 shows an example of what the configured video widget looks like on a published website.

Fig. 17.25. A configured video widget on a published website

![](media/image604.png){width="5.197915573053368in" height="2.9479166666666665in"}

To configure a video widget, follow the steps below.

-   Select **Menu** \> **Website Builder**. Click on the **edit** ![](media/image231.png){width="0.2916666666666667in" height="0.2833333333333333in"} icon next to any of the websites.

-   Drag and drop a **Row** widget \> click on the **expand** ![](media/image505.png){width="0.24166666666666667in" height="0.24166666666666667in"} icon to expand the **Content** category \> drag and drop a **Video** widget onto the row \> click on it, and the widget editor opens, as shown below:

![](media/image605.png){width="6.266666666666667in" height="2.558333333333333in"}

-   Populate the fields as follows.

```{=html}
<!-- -->
```
-   **Video URL** \[Mandatory\]: enter the URL of a YouTube video. You can copy and paste the URL of the YouTube video or type the URL into the textbox manually. The video should be publicly accessible (In case of sensitive/private material, it is not advisable to share).

-   **Frame Width (in px):** enter the width of the video container in pixels (e.g. 600).

-   **Frame Height (in px):** enter the height of the video container in pixels (e.g. 400).

-   **Opacity:** enter the opacity of the video. This determines how opaque or transparent a video is. It can take a value from 0.0 to 1.0. The lower the value, the more transparent it is: 1 indicates fully opaque and 0 indicates fully transparent (e.g. 0.5 for 50% transparency).

-   **Box Shadow:** enter a box shadow for the video -- this attaches one or more shadows to an element. It takes a value in the format **x-offset y-offset blur spread colour** (e.g. 1px 1px 1px 1px #333).

```{=html}
<!-- -->
```
-   Click on **Save Change(s)**.

## 17.29 HTML widget

***Available in***: Dashboards and Website Builder

You can use the HTML widget when you want to add multiple content like text, images charts and maps in a single block. You can add these individually too, but the HTML widget provides flexibility to style and format them using CSS. It is a powerful way to add content, but at the same time it requires knowledge of HTML and CSS.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** the HTML widget allows direct editing of HTML/CSS, so any errors or inconsistencies could lead to display issues on the webpage.
  --------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To configure an HTML widget, follow the steps below.

-   Select **Menu** \> **Dashboards** \> click on **Create New** at the top right-hand corner of the screen.

-   Drag and drop a **Row** \> click on the **expand** ![](media/image505.png){width="0.24166666666666667in" height="0.24166666666666667in"} icon to expand the **Content** category \> drag and drop an **HTML** widget onto the row \> click on it, and the widget editor screen opens, as shown below:

![](media/image606.png){width="6.216666666666667in" height="2.8666666666666667in"}

For demonstration purposes, this guide uses the following example.

**Example 1.** Add an image and a map inside an HTML widget.

-   Click on the **image** ![](media/image607.png){width="0.24166666666666667in" height="0.21666666666666667in"} icon, and the popup screen below appears:

![](media/image608.png){width="3.658333333333333in" height="4.033333333333333in"}

-   Populate the fields as follows.

```{=html}
<!-- -->
```
-   **URL:** enter the image **URL**.

-   **Alternative Text:** enter alternative text. If the image does not exist at the specified URL, the text entered here is shown.

-   **Width:** enter the image width in pixels (e.g. 100).

-   **Height:** enter the image height in pixels (e.g. 100).

-   **Border:** enter the border for an image in pixels.

-   **HSpace:** enter space in pixels. this adds horizontal space to the left and right of an image.

-   **VSpace:** enter space in pixels. This adds vertical space to the top and bottom of an image.

-   **Alignment:** select **Left** from the drop-down menu.

    **Left** -- the image is aligned to the left.

    **Right** -- image is aligned to the right.

```{=html}
<!-- -->
```
-   Click on **OK** \> click on **Save Change(s)**.

To add a map widget inside the HTML widget, follow the steps below.

-   Place the cursor where you want to insert the widget \> click on ![](media/image609.png){width="1.0208333333333333in" height="0.3541666666666667in"} \> select **Map** widget, and the widget is added, as shown below:

![](media/image610.png){width="6.33333552055993in" height="2.5416666666666665in"}

-   Double-click on it, and the map widget configuration screen opens.

-   Configure it \> click on **Save Change(s)**.

## 17.30 Document widget

***Available in***: Website Builder

This allows you to display EWARS bulletins on the website, as shown in the example of a configured document widget below:

![](media/image611.png){width="5.11666447944007in" height="1.6166666666666667in"}

In the screenshot above, you can see a yearly list of documents generated for the document template and can switch between years by clicking on it.

You can download the document by clicking on the **PDF** ![](media/image612.png){width="0.3in" height="0.31666666666666665in"} icon.

To view the document, click on it and it opens in a new browser window/tab.

To subscribe/unsubscribe to a document using this widget on a public website, follow the steps below.

-   Click on **Subscribe**, and the popup window below appears:

![](media/image613.png){width="5.0in" height="1.3583333333333334in"}

-   Enter your email address \> click on **Subscribe**.

Once the subscribed document is generated, the system will email it automatically. An **Unsubscribe** link is available in all subsequent documents emailed to you. You can click on the link to unsubscribe from the document.

To configure a document widget, follow the steps below.

-   Select **Menu** \> **Website Builder**. Click on the **edit** ![](media/image231.png){width="0.2916666666666667in" height="0.2833333333333333in"} icon next to any of the websites.

-   Drag and drop a **Row** widget \> click on the **expand** ![](media/image505.png){width="0.24166666666666667in" height="0.24166666666666667in"} icon to expand the **Other** category \> drag and drop a **Documents** widget onto the row \> click on it, and the widget editor opens, as shown below:

![](media/image614.png){width="6.333333333333333in" height="1.3166666666666667in"}

-   Select the template from the drop-down menu for which documents are to be displayed (e.g. Weekly EWARS bulletin) \> click on **Save Change(s)**.

## 17.31 Documents list widget

***Available in***: Website Builder

The documents list widget allows you to list all the available documents for the account and subscribe to them.

Fig. 17.26 shows an example of a configured documents list widget.

Fig. 17.26. A configured documents list widget

![](media/image615.png){width="6.475in" height="1.925in"}

To configure a documents list widget, follow the steps below.

-   Select **Menu** \> **Website Builder**. Click on the **edit** ![](media/image231.png){width="0.2916666666666667in" height="0.2833333333333333in"} icon next to any of the websites.

-   Drag and drop a **Row** widget \> click on the **expand** ![](media/image505.png){width="0.24166666666666667in" height="0.24166666666666667in"} icon to expand the **Other** category \> drag and drop a **Documents list** widget on the row \> click on it, and the widget editor opens, as shown below:

![](media/image616.png){width="6.083333333333333in" height="2.1in"}

-   Populate the fields as follows.

```{=html}
<!-- -->
```
-   **Widget Title**: enter a title for the widget (e.g. **"**Documents list").

-   **Widget Icon**: enter a widget icon. The icon is visible just before the widget title. (If you want to change the icon, refer to the **Tip** in topic **17.4 Text widget**.)

-   **Header Colour:** enter the colour name or hex colour code for the background colour of the header (e.g. ![](media/image522.png){width="0.15833333333333333in" height="0.15833333333333333in"} [(orange)]{.mark}).

-   **Header Text Colour:** [enter the colour]{.mark} name or [hex colour code for the text colour of the header (e.g. #0C0105).]{.mark}

```{=html}
<!-- -->
```
-   Click on **Save Change(s)**.

  ---------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------
  ![](media/image43.png){width="0.65625in" height="0.3541666666666667in"}   Contact the EWARS Super Administrator for help and support on different widgets and their configuration.

  ---------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------

The following chapter explores the Notebooks feature in EWARS. Notebooks can be created using different widgets, enabling you to explore various visualization possibilities for data in the system. This feature is valuable for your analysis and data sharing needs.

# Chapter 18. Notebooks

Notebooks facilitate analysis, presentation, and sharing of Early Warning, Alert and Response System (EWARS) data using different widgets such as series chart, category chart, pyramid chart, map and table, enabling a variety of visualization possibilities. You can easily create a notebook by dragging and dropping widgets and configuring them further according to your requirements. The Notebooks feature saves both time and effort, and facilitates quick analysis. This analysis can be saved and is also updated automatically as data are updated. You can also share the notebook externally and internally.

To get started, please navigate to the Model account and then to a sample notebook inside it. Sample notebooks can be copied to your account to illustrate different functions, and can be modified according to your context.

## 18.1 Copying a sample notebook from the Model account

The example below sets out how to copy the Measles Case Study notebook from the Model account.

**Step 1.** Copy the Measles Case Study notebook to your account.

-   Select **Menu** \> **Configuration Transfer**. Select **Model account** from the **Source Account** drop-down menu. The system displays the **List of transferable items**.

-   Enter "Measles Case Study" in the search box \> select **Measles Case Study** \> click on the **transfer** ![](media/image617.png){width="0.28125in" height="0.23958333333333334in"} icon \> click on **Confirm**, and the notebook is copied to your account.

**Step 2.** View the Measles Case Study notebook.

-   Select **Menu** \> **Notebooks** \> click on **Measles Case Study** under **My Notebooks**, and the notebook is visible, as shown below:

![](media/image618.png){width="4.822916666666667in" height="5.302084426946632in"}

## 18.2 Editing the sample notebook

For demonstration purposes, this guide uses the example of removing the category chart from the Measles Case Study notebook and adding a pyramid chart to it.

**Step 1.** Remove the category chart from the Measles Case Study notebook.

-   Select **Menu** \> **Notebooks** \> select **Measles Case Study** under **My Notebooks**. Click on the **edit** ![](media/image240.png){width="0.2916666666666667in" height="0.275in"} icon \> scroll down in the widget configuration section and look for the category chart, as shown below:

![](media/image619.png){width="6.05in" height="2.925in"}

-   Click on the **delete** ![](media/image620.png){width="0.2916666666666667in" height="0.2916666666666667in"} icon of the **Category Chart** \> click on **Save Change(s)**, and the chart is removed.

**Step 2.** Add a pyramid chart to display health facility-wide measles cases for Nambutu for 2017 to 2020.

-   Select **Menu** \> **Notebooks** \> select **Measles Case Study** under **My Notebooks** \> click on the **edit** ![](media/image240.png){width="0.2916666666666667in" height="0.275in"} icon, and the notebook opens in edit mode.

-   Drag and drop a **Pyramid Chart** from the left-hand side to the widget section in the middle, and the chart is added.

-   Click on the **settings** ![](media/image621.png){width="0.3125in" height="0.23958333333333334in"} icon of the pyramid chart under the **Settings** tab.

-   Enter the **Chart Title** "Measles cases by health facility (2017--2020)" \> set **Aggregation** as **Yearly** \> set **Period** as "2017-01-01" to "2020-12-31" \> set **Title**, **Export**, **Navigator** and **Legend** as **Show** \> set **Zoom as** enabled \> enter the **chart height** as 500 px.

-   Click on the **Data** tab \> click on **Add Series** \> click on the **edit** ![](media/image240.png){width="0.2916666666666667in" height="0.275in"} icon. Enter the **Title** "Total measles cases" \> set **Location Specification** as **Generator** \> set **Generator parent location** as Nambutu (Country) \> select Province from the **Generator location type** drop-down menu \> set **Location Status** as **Active** \> set **Data Source** as **Indicator** \> set **Indicator source** as Measles total \> set **Period** as **Inherit**.

-   Click on **Save Change(s)**.

-   Click on **View**, and the screen below appears:

![](media/image622.png){width="5.41666447944007in" height="3.25in"}

## 18.3 Creating a notebook

To create a notebook easily by dragging required widgets and then configuring them, follow the steps below.

-   Select **Menu** \> **Notebooks** \> click on **Create Notebook**, and the notebook design screen opens, as shown below:

![](media/image623.png){width="7.0in" height="4.125in"}

-   Enter the general settings of the notebook (Part 3 in the screenshot), then drag the desired widgets from Part 1 to Part 2 and configure them as set out as below.

**Step 1.** Name a notebook, and configure its general settings.

-   Enter the **Name** (e.g. "Measles Case Study") at Part 3 in the screenshot \> enter a **Description** (e.g. "Measles case analysis based on outbreak response")

-   Turn on **Shared** to share the notebook with other users of your account, and the notebook is visible under the **Shared** tabs of those users.

-   Set **Access** as **public** or **private** to allow or prevent access to the notebook through the notebook link.

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** the steps below show how to configure the widgets. For more detailed information on configuring widgets, refer to **Chapter 17. Widgets and their configuration**.
  --------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Step 2.** Add a text widget to display information on the Measles Case Study notebook.

-   Drag and drop a **Text** widget from the list at the left-hand side to the middle section of the notebook \> click on the **settings** ![](media/image621.png){width="0.3125in" height="0.23958333333333334in"} icon.

-   Enter the **Widget Title** "Measles Case Study" \> enter the relevant **Widget Icon**.

-   Enter the **Header Colour** as ![](media/image624.png){width="0.15833333333333333in" height="0.15833333333333333in"} (#004a87) \> enter the **Header Text** **Colour** as "#fff"(white).

-   Enter **Content**: **"**Measles is a major cause of childhood morbidity and mortality, accounting for nearly half of the morbidity associated with global vaccine-preventable diseases. This case study aims to analyse the number of cases and deaths due to measles in the Nambutu region over the last 4 years."

-   Click on **Save Change(s)**.

-   Click on **View**, and the screen below appears:

![](media/image625.png){width="6.27083552055993in" height="1.1875in"}

**Step 3.** Add a table widget to display provincial measles cases and deaths for Nambutu from 2017 to 2020.

-   Drag and drop a **Table** widget from the list at the left-hand side to the middle part of the notebook \> click on the **settings** ![](media/image621.png){width="0.3125in" height="0.23958333333333334in"} icon.

-   Enter the **Title** "Measles Cases and Deaths by Province (2017--2020)".

-   Set **Location Specification** as **Generator** \> set **Show parent column?** as **No** \> set **Parent location** as **Custom** \> set **Generator parent location** as Nambutu (Country) \> select Province from the **Generator location type** drop-down menu \> set **Location Status** as **Active**.

-   Set **Column Header** as **Show**.

-   Set **Hide Rows with 0 or no data** as **No** \> set **Sorting column** as **Location Name Asc**.

-   Click on the **Data** tab \> click on **Add Column** \> click on the **edit** ![](media/image240.png){width="0.2916666666666667in" height="0.275in"} icon.

-   Enter the **Title** "Measles Cases".

-   Set **Source Type** as **Indicator** \> select **Indicator Source** as **Measles Total** \> set **Reduction** as **Sum** \> set **Period** as "2017-01-01" to "2020-12-31".

Add another column for measles total deaths.

-   Click on **Add Column** \> click on the **edit** ![](media/image240.png){width="0.2916666666666667in" height="0.275in"} icon.

-   Enter the **Title** "Measles Total Deaths".

-   Set **Source Type** as **Indicator** \> select **Indicator Source** as **Measles Total Deaths** \> set **Reduction** as **Sum** \> set **Period** as "2017-01-01" to "2020-12-31".

-   Click on **Save Change(s)**.

-   Click on **View**, and the screen below appears:

![](media/image579.png){width="4.802083333333333in" height="2.7031255468066493in"}

**Step 4.** Add a map widget to display total measles deaths data by province for Nambutu from 2017 to 2020.

-   Drag and drop a **Map** widget from the list at the left-hand side to the middle part of the notebook \> click on the **settings** ![](media/image621.png){width="0.3125in" height="0.23958333333333334in"} icon.

-   Enter the **Title "**Measles Deaths".

-   Set **Location** as **Of Type** \> enter "Nambutu" as the **Location** \> select Province from the **Location Type** drop-down menu \> set **Location Status** as **Active**.

-   Set **Query Type** as **Indicator** \> select the **Indicator Measles Total Deaths** \> set **Reduction** as **Sum** \> set **Period** as "2017-01-01" to "2020-12-31".

-   In **Thresholds**, click on the **add** ![](media/image626.png){width="0.25in" height="0.21666666666666667in"} icon \> enter "0 to 100", choose ![](media/image627.png){width="0.15833333333333333in" height="0.15833333333333333in"} (#fddbc7) \> enter "100 to 200", choose ![](media/image628.png){width="0.15833333333333333in" height="0.15833333333333333in"} #FF8000 \> enter "200 to 300", choose ![](media/image629.png){width="0.15627187226596675in" height="0.15627187226596675in"} (#66CCFF) \> enter "300 to 400", choose ![](media/image624.png){width="0.15833333333333333in" height="0.15833333333333333in"} #000080.

-   Set **Legend** as **Show** \> set **Opacity** as 0.5 \> set **Base Geometry Colour** as white (#fff) \> set **Background Colour** as white (#fff) \> set **Stroke Colour** as black (#000) \> set **Stroke Width** as 2 \> set **Width** as 100 \> set **Height** as 500.

-   Set **Show labels** as **Yes** \> select the **Labelling style** Default \> enter **Label Font Size** as 12 \> choose **Label Colour** ![](media/image630.png){width="0.15833333333333333in" height="0.15833333333333333in"} (#000).

-   Click on **Save Change(s)**.

-   Click on **View**, and the screen below appears:

![](media/image631.png){width="4.841666666666667in" height="4.775in"}

**Step 5.** Add a series chart to display monthly total measles cases and monthly total measles deaths for Nambutu from 2017 to 2020.

-   Drag and drop a **Series chart** widget from the list at the left-hand side to the middle part of the notebook \> click on the **settings** ![](media/image621.png){width="0.3125in" height="0.23958333333333334in"} icon.

-   Enter the **Chart Title** "Measles -- Cases and Deaths (2017--2020)" \> set **Aggregation** as **Monthly**.

-   Set the **period** as "2017-01-01" to "2020-12-31".

-   Set **Title** as **Show** \> set **Export** as **Show** \> set **Zoom** as **Enabled** \> set **Navigator** as **Hide** \> set **Legend** as **Show**.

-   Set **Y Axis title** as **Show** \> set **X Axis title** as **Show** \> set **Chart height** as 400.

-   Click on the **Data** tab \> click on **Add Series** \> click on the **edit** ![](media/image240.png){width="0.2916666666666667in" height="0.275in"} icon.

-   Enter the **Title** "Total Measles Cases".

-   Set **Location Specification** as **Specific Location** \> select Nambutu (Country) from the **Location** drop-down menu.

-   Set **Data Source** as **Indicator** \> select Measles Total from the **Indicator** drop-down menu\> set **Period** as **Inherit**.

-   Set **Style** as **Line** \> select **Colour** as ![](media/image624.png){width="0.15833333333333333in" height="0.15833333333333333in"} \> enter **Line Width** "3" \> set **Line Style** as **Solid** \> enter **Marker Radius** "3" \> set **Marker style** as **Circle**.

Add another series for measles total deaths.

-   Click on **Add Series** \> click on the **edit** ![](media/image240.png){width="0.2916666666666667in" height="0.275in"} icon.

-   Enter the **Title** "Total Measles Deaths".

-   Set **Location Specification** as **Specific Location** \> select Nambutu (Country) from the **Location** drop-down menu.

-   Set **Data Source** as **Indicator** \> select Measles Total Deaths from the **Indicator** drop-down menu \> set **Period** as **Inherit**.

-   Set **Style** as **Line** \> select **Colour** as ![](media/image628.png){width="0.15833333333333333in" height="0.15833333333333333in"} \> enter **Line Width** "3" \> set **Line Style** as **Solid** \> enter **Marker Radius** "3" \> set **Marker style** as **Circle**.

-   Click on **Save Change(s)**.

-   Click on **View**, and the screen below appears:

![](media/image632.png){width="5.825in" height="3.0833333333333335in"}

**Step 6.** Add a pie chart to display measles under 5 cases, measles 5 and over cases and measles total cases for Nambutu from 2017 to 2020, aggregated by year.

![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"} **Note:** in this case, it is recommended that you group the category chart by indicators.

-   Drag and drop a **Category** widget from the list at the left-hand side to the middle part of the notebook \> click on the **settings** ![](media/image621.png){width="0.3125in" height="0.23958333333333334in"} icon.

-   Enter the **Chart Title** "Measles data distribution (2017--2020)" \> set **Sample Interval** as **Yearly** \> set **Group by Indicators** as **Yes** \> set **Period** as "2017-01-01" to "2020-12-31".

-   Set **Chart Title** as **On** \> set **Legend** as **Show** \> select **Legend position** as **Bottom** \> select **Chart style** as **Default** \> select **Slice Ordering** as **Category Title Ascending**.

Add a category for measles cases under 5.

-   Click on the **Data** tab \> click on **Add Category** \> click on the **edit** ![](media/image240.png){width="0.2916666666666667in" height="0.275in"} icon.

-   Enter "Measles under 5 cases" as the **Slice Label** \> set **Colour** as white ("#ff")***.***

-   Set **Location spec.** as **Specific Location** \> select Nambutu (Country) from the **Location** drop-down menu.

-   Set **Source Type** as **Indicator** \> select Measles Under 5 from the **Indicator Source** drop-down menu \> set **Reduction type** as **Sum** \> set **Period** as **Inherit**.

Add a category for Measles cases 5 and over.

-   Click on **Add Category** \> click on the **edit** ![](media/image240.png){width="0.2916666666666667in" height="0.275in"} icon.

-   Enter "Measles cases 5 and over" as the **Slice Label** \> set **Colour** as white ("#ff").

-   Set **Location spec.** as **Specific Location** \> select Nambutu (Country) from the **Location** drop-down menu.

-   Set **Source Type** as **Indicator** \> select Measles 5 and over from the **Indicator Source** drop-down menu \> set **Reduction type** as **Sum** \> set **Period** as **Inherit**.

Add a category for Measles deaths.

-   Click on **Add Category** \> click on the **edit** ![](media/image240.png){width="0.2916666666666667in" height="0.275in"} icon.

-   Enter "Measles deaths" as the **Slice** Label \> set Colour as white ("#ff").

-   Set **Location spec.** as **Specific Location** \> select Nambutu (Country) from the **Location** drop-down menu.

-   Set **Source Type** as **Indicator** \> select Measles Total Deaths from the **Indicator Source** drop-down menu \> set **Reduction type** as **Sum** \> set **Period** as **Inherit**.

-   Click on **Save Change(s).**

-   Click on **View**, and the screen below appears:

![](media/image633.png){width="6.010416666666667in" height="4.019466316710411in"}

**Step 7.** Add a pyramid chart to display annual measles cases for Nambutu from 2017 to 2020.

-   Drag and drop a **Pyramid chart** widget from the list at the left-hand side to the middle part of the notebook \> click on the **settings** ![](media/image621.png){width="0.3125in" height="0.23958333333333334in"} icon.

-   Enter the **Chart Title** "Measles cases (2017 -- 2020)" \> set **Aggregation** as **Yearly**.

-   Set the **Period** as "2017-01-01" to "2020-12-31".

-   Set **Title** as **Show** \> set **Export** as **Show** \> set **Zoom** as **Enabled** \> set **Navigator** as **Show** \> set **Legend** as **Show**.

-   Enter the **Chart width** as "500".

-   Enter the **Chart height** "500".

-   Click on the **Data** tab \> click on **Add Series** \> click on the **edit** ![](media/image240.png){width="0.2916666666666667in" height="0.275in"} icon.

-   Enter the **Title** "Total measles cases".

-   Set **Location Specification** as **Specific Location** \> select Nambutu (Country) from the **Location** drop-down menu.

-   Set **Data Source** as **Indicator** \> select Measles total from the **Indicator** drop-down menu \> set **Period** as **Inherit**.

-   Click on **Save Change(s)**.

-   Click on **View**, and the screen below appears:

![](media/image634.png){width="5.816666666666666in" height="3.4583333333333335in"}

-   Click on **Save Change(s)**, and the notebook is visible under **My Notebooks**.

## 18.4 Viewing a notebook

You can view notebooks under two tabs: **My Notebooks** and **Shared** as shown below:

![](media/image635.png){width="4.25in" height="2.6458333333333335in"}

**My Notebooks:** All the notebooks created or copied by you are visible under this tab.

**Shared:** All the notebooks shared by other users of the EWARS account are visible under this tab.

-   Select **Menu** \> **Notebooks**. Click on either the **My Notebooks** or the **Shared** tab, and the list of notebooks is visible. Click on the name of the notebook to view it.

## 18.5 Downloading a notebook

You can download the notebook as a PDF or as an Excel file.

-   Select **Menu** \> **Notebooks** \> **My Notebooks**. Click on a notebook from the list (e.g. Measles Case Study) \> click on the **download** ![](media/image636.png){width="0.4in" height="0.3333333333333333in"} icon.

```{=html}
<!-- -->
```
-   **Either** click on **Export as PDF** to download the notebook as a PDF file

-   **Or** click on **Export as Excel** to download the notebook as an Excel file.

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** you can download the notebook as and when required, as the data are updated in real time on the basis of the selected configurations.
  --------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 18.6 Editing a notebook

Notebooks visible in the **My Notebook** tab can be edited, but you cannot edit notebooks visible in the **Shared** tab.

-   Select **Menu** \> **Notebooks** \> **My Notebooks**. Click on a notebook from the list (e.g. Measles Case Study) \> click on the **edit** ![](media/image240.png){width="0.2916666666666667in" height="0.275in"} icon, and the notebook is open for editing. Make the desired changes \> click on **Save Change(s)**, and the notebook is edited.

## 18.7 Deleting a notebook

Notebooks visible in the **My Notebook** tab can be deleted, but you cannot delete notebooks visible in the **Shared** tab.

-   Select **Menu** \> **Notebooks** \> **My Notebooks**. Click on the **delete** ![](media/image620.png){width="0.2916666666666667in" height="0.2916666666666667in"} icon in the notebook (e.g. Measles Case Study) \> click on **Confirm**, and the notebook is deleted permanently.

## 18.8 Sharing a notebook via a public link

You can share a notebook with others via a public link.

**Step 1.** Set public access to the notebook.

-   Select **Menu** \> **Notebooks** \> **My Notebooks**. Click on the notebook (e.g. Measles Case Study) \> click on the **edit** ![](media/image240.png){width="0.2916666666666667in" height="0.275in"} icon in **Notebook Settings** \> set **Access** as **Public** \> click on **Save Change(s)**.

**Step 2.** Share the universal resource locator (URL) or link to the notebook.

-   Go to the Measles Case Study notebook \> click on the **copy** ![](media/image502.png){width="0.2916666666666667in" height="0.25in"} icon, and the URL is copied. Email the copied URL, and users can view the notebook by clicking on the URL/link received in the email.

-   This notebook link can also be shared via different mediums, and can be viewed via various browsers.

## 18.9 Sharing a notebook with EWARS account users

You can share a notebook with other users of the same EWARS account.

-   Select **Menu** \> **Notebooks** \> click on **My Notebooks** \> click on the notebook (e.g. Measles Case Study) \> click on **edit** \> set the **Shared** field as **Shared** \> Click on **Save Change(s).**

The notebook is shared, and all other users can view it in the **Shared** tab. You can also view it under the **My Notebooks** tab.

## 18.10 Copying or duplicating a shared notebook and viewing it

You can copy or duplicate notebooks visible in the **Shared** tab, which lists notebooks shared by other users of your account.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** you cannot normally edit notebooks under the **Shared** tab, but if you need to, you have to first copy or duplicate the shared notebook. After doing so, it is available under the **My Notebooks** tab, where you can edit it.
  --------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The steps below set out how to copy or duplicate a shared notebook and view it under the **My Notebooks** tab.

-   Select **Menu** \> **Notebooks**. Click on **Shared** \> click on the **duplicate** ![](media/image637.png){width="0.28468175853018374in" height="0.28207677165354333in"} icon of the notebook (e.g. Measles Case Study). Enter a new name for the notebook \> make the required changes. Click on **Save Change(s)**, and the notebook is copied under the **My Notebooks** tab, where it can be viewed.

The following chapter provides an overview of the Dashboards feature and helps you learn how to create them, facilitating the tracking, analysis and display of data, key performance indicators and more.

**\
**

# Chapter 19. Dashboards

Dashboards are the primary element for real-time data visualization in the Early Warning, Alert and Response System (EWARS). By leveraging dashboards, you can visually monitor, analyse and present crucial data, metrics and key performance indicators. Dashboards are customizable and designed to meet specific needs of different levels of users. Multiple dashboards can be designed in an EWARS account to fulfil diverse monitoring needs, such as the EWARS overview dashboard, measles dashboard and cholera dashboard. Each EWARS account should have an overview dashboard to illustrate EWARS implementation in general.

## 19.1 Overview dashboard

The overview dashboard illustrates EWARS implementation in your context. Regardless of other dashboards in the account, each implementation should have an overview dashboard.

It is recommended that you use the standardized overview dashboard to allow standardization and consistency of branding across EWARS implementations. The Model account provides a standard dashboard, which you can customize to suit your context.

All EWARS accounts have an overview dashboard. Fig. 19.1 shows an example.

Fig. 19.1. Example of an overview dashboard

![](media/image638.png){width="6.27083552055993in" height="3.6041666666666665in"}

This overview dashboard highlights the early warning, alert and system in place and acts as the EWARS landing page when you log in. All overview dashboards should follow the same standard format as suggested in the Model account. A typical overview dashboard consists of a top section showing the key stakeholders involved (e.g. the ministry of health and WHO). The middle section shows the EWARS coverage in your context and an overview of the activities of EWARS operations. The last section comprises the associated activity and tasks of your account.

## 19.2 Copying the overview dashboard

Instead of developing your own dashboard from scratch, you can copy a sample dashboard given from the Model account and modify it to suit your context.

**Step 1.** Copy an overview dashboard to your account.

-   Select **Menu** \> **Configuration Transfer**. Select **Model account** from the **Source Account** drop-down menu. The system displays the **List of transferable items**.

-   Enter "Overview (Account Admin)" in the search box \> select the dashboard **Overview (Account Admin)** \> click on the **transfer** ![](media/image639.png){width="0.3333333333333333in" height="0.3125in"} icon. Click on **Confirm**, and the dashboard is copied to your account.

**Step 2.** Assign a dashboard.

When you copy a dashboard, it is available only to your account in the list of dashboards. However, you can assign a dashboard, making it visible on the EWARS home screen and available to other web users and Reporting Users. In this way, you can have different dashboards that are available to different users, based on their roles.

-   Click on the **settings** ![](media/image640.png){width="0.3333333333333333in" height="0.3125in"} icon \> click on ![](media/image641.png){width="0.9583333333333334in" height="0.3541666666666667in"}.

```{=html}
<!-- -->
```
-   Select a role from the drop-down menu (e.g. Reporting User) \> click on the **add** ![](media/image642.png){width="0.3125in" height="0.3125in"} icon, and a list of dashboards is visible. Scroll down to **Overview (Account Admin)** \> click on the **add** ![](media/image643.png){width="0.3958333333333333in" height="0.3333333333333333in"} icon to add the dashboard to the list, as shown below:

![](media/image644.png){width="4.427083333333333in" height="2.4375in"}

-   Click on **Save Change(s)**.

**Step 3.** View the dashboard.

-   Click on **EWARS** ![](media/image645.png){width="2.2916666666666665in" height="0.3958333333333333in"} as highlighted, and the assigned dashboard can be seen at the left-hand side.

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** copying the sample dashboard merely brings the skeletal structure to your account. It is important to keep in mind that the copied sample dashboard has no content. After you copy it to your account, it won't be functional unless you apply modifications and link your data with the dashboard.
  --------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ---------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![](media/image43.png){width="0.65625in" height="0.3541666666666667in"}   The EWARS overview dashboard is the standard dashboard. EWARS recommends a similar pattern and format of dashboards for all accounts. This allows standardization across EWARS accounts .

  ---------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 19.3 Editing a sample dashboard

Editing a sample dashboard involves changing the country name and logo according to your requirements. You can also add/remove widgets in the overview dashboard.

-   Select **Menu** \> **Dashboards**. Click on the **edit** ![](media/image646.png){width="0.3125in" height="0.3125in"} icon of the Overview (Account Admin) dashboard, and the dashboard editor below appears:

![](media/image647.png){width="5.989584426946632in" height="2.4895833333333335in"}

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** the activity feed and tasks widgets will fetch the activities and tasks of your account automatically, so you may keep these widgets as they are. These don't require any modifications.
  --------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

For more information, refer to **Chapter 17. Widgets and their configuration**.

**Step 1.** Change the country name and logo.

-   Click on the first row with the label **HTML** (HyperText Markup Language), and the widget configuration screen opens. Replace "Nambutu" with "Country X", as shown below:

![](media/image648.png){width="5.677084426946632in" height="1.0625in"}

-   Click on ![](media/image649.png){width="0.9791666666666666in" height="0.3125in"}, and the **Web Content** screen opens in a new tab.

-   Click on ![](media/image650.png){width="1.09375in" height="0.28125in"} \> select **Folder Path** (e.g. images) \> click on ![](media/image651.png){width="0.75in" height="0.2708333333333333in"}, and a file chooser dialogue box opens. Select a logo file, and the logo is uploaded.

-   Look for the newly uploaded file and click on the **copy** ![](media/image652.png){width="0.28125in" height="0.28125in"} icon of the uploaded image \> close the **Web Content** browser tab, and you will be back on the Website Builder configuration screen.

The logo image file is uploaded. Next, you need to provide the copied universal resource locator (URL) of the uploaded image.

-   Double-click on the image you want to change, and the **Image Properties** screen below opens:

![](media/image653.png){width="3.15625in" height="3.3958333333333335in"}

-   Replace the **URL** under the **Image Info** tab with the copied URL of the uploaded image \> enter the new **Width** in pixels (e.g. "100") \> enter the new **Height** in pixels (e.g. "100").

-   Click on **OK** \> click on **Save Change(s),** and the HTML widget closes.

**Step 2.** Reconfigure the EWARS coverage and activity overview.

This widget is configured using locations, indicators and forms, and these are different for each EWARS account. Therefore, they need to be reconfigured in the dashboard.

-   Click on the second row with the label **HTML**, and the HTML editor screen appears. Look for **Raw Value** icon highlighted below:

![](media/image654.png){width="6.667253937007874in" height="2.8177088801399823in"}

-   Double-click on **Raw Value**, and the widget configuration screen below appears:

![](media/image655.png){width="4.966666666666667in" height="2.5in"}

-   Configure the widget according to your requirements. For more information about configuring the widget, refer to **Chapter 17. Widgets and their** **configuration**, topic **17.6.1 Raw widget in dashboards**.

-   Click on **Save Change(s)**.

**Step 3.** Remove the documents widget.

-   Right-click on the cell with the label **Documents**, and cell options are visible. Click on **Remove Cell**, as shown below, and the cell is removed:

![](media/image656.png){width="4.625in" height="2.8333333333333335in"}

-   Click on **Save Change(s)**, and the documents widget is removed.

**Step 4.** Add an outbreaks widget.

-   Drag and drop a **row** widget from the left-hand column to the middle section, and a row is added.

-   Click on the **expand** ![https://lh6.googleusercontent.com/J10_TJu_n6cODdAe708vpkoxY7zF1ZE1cR2tf_5kcbZg7uzaOJARvNAVl4IOW14rWA2meSwxlqx76nGJKzbNXCKNV8BGYSrNvmnZOF-xhWOEcvDuqDQflGCisFnmK19RqT1vk9mX](media/image657.png){width="0.19791666666666666in" height="0.21875in"} icon in front of the **User** widget in the left-hand hand column to expand the widget categories. Drag the **Outbreaks** widget from the category list, and drop it onto the added row in the middle section, as shown below:

> ![](media/image658.png){width="6.026042213473316in" height="4.721747594050743in"}

-   [Right-click on the **Outbreaks** row, and cell settings options appear. Click o]{.mark}n []{.mark}![https://lh5.googleusercontent.com/MNBW3qSU6EzN4hSG2R82P4mfzvCdTqAPsKGIwB_84THcHRGKGoOzyg3pC-RuEZGhy42rOXAo1t72gGUTGW-KAMlNbiRfaVyaKMYEquMmXMaG5OMIOQlyqP94pwU-BG3mzG3BOAW0](media/image659.png){width="1.40625in" height="0.3229166666666667in"} [, and the row is moved up.]{.mark}

-   [Click on the **Outbreaks** row and configure the widget]{.mark} according to [your needs.]{.mark} For more information about configuring this widget, refer to **Chapter 17. Widgets and their configuration**, topic **17.9 Outbreaks widget**.

-   Click on **Save Change(s)**, and the widget configuration screen closes.

**Step 5.** Save and view the dashboard.

-   Click on **Save Change(s)** to save all the changes made to the dashboard.

-   Click on **EWARS** ![](media/image645.png){width="2.2916666666666665in" height="0.3958333333333333in"} as highlighted, and the dashboard opens with the newly added changes, as shown below:

![](media/image660.png){width="7.0in" height="6.811111111111111in"}

## 19.4 Creating a new dashboard

Creating a new dashboard entails designing the dashboard, configuring the widgets in it and assigning the dashboard to your role.

To design the dashboard, you can drag and drop the relevant widgets according to your requirements, to achieve the desired structure. You can configure the dashboard using the various widgets such as text, image, HTML, chart, map and table widgets provided in the dashboard editor. To view the dashboard and the modifications, assign it to your role. For more information on how to assign dashboards, refer to topic **19.8 Assigning a dashboard**.

For technical support, please contact the EWARS Super Administrator.

Follow the steps below to create a new dashboard.

-   Select **Menu** \> **Administration** \> **Dashboard** \> **Create New**, and the dashboard editor screen below opens:

![](media/image661.png){width="6.5in" height="3.7777777777777777in"}

To create a new dashboard, follow the steps below.

-   Configure the general settings shown in Part 3 in the screenshot. Fill in the **Layout Name** \> set **Status** as **Active** or **Inactive**. Only dashboards whose status is **Active** are visible while assigning the dashboard to your role. Enter a **Description** \> enter **Tags**.

-   Drag and drop a **Row** widget from Part 1 to Part 2 of the screenshot.

-   Drag and drop a **Cell** widget onto the added row.

-   Drag and drop a desired widget (e.g. **Image** or **Video**) onto the cell.

Add all the widgets that you would like to have on your dashboard in the same way.

To move the row/cell up, down, right or left, or to remove it, right-click on it and select the appropriate option.

The screenshot below shows an example in which widgets are added to the dashboard.

![](media/image662.png){width="6.0625in" height="2.1354166666666665in"}

-   Configure all the widgets placed in the cells one by one. To learn more about configuring dashboard widgets, refer to **Chapter 17. Widgets and their configuration**.

-   Click on **Save Change(s)**, and the dashboard is saved.

## 19.5 Editing a dashboard

-   Select **Menu** \> **Dashboards**. Click on the **edit** ![](media/image663.png){width="0.2916666666666667in" height="0.28125in"} icon to edit the existing dashboard \> make the relevant changes. Click on **Save Change(s)**, and the dashboard is edited.

## 19.6 Duplicating a dashboard

Duplicating dashboards helps to save time and can be very helpful in scenarios where you want to replicate a layout but with different widgets.

-   Select **Menu** \> **Dashboards**. Click on the **duplicate** ![](media/image637.png){width="0.3125in" height="0.3333333333333333in"} icon to edit the existing dashboard \> enter a new name for the dashboard \> make the required changes to the dashboard. Click on **Save Change(s)**, and the dashboard is duplicated.

## 19.7 Deleting a dashboard

Deleting a dashboard is helpful in scenarios where there is no longer a need to monitor a trend in disease outbreak or an event.

-   Select **Menu** \> **Dashboards**. Click on the **delete** ![](media/image620.png){width="0.2916666666666667in" height="0.2916666666666667in"} icon to delete the existing dashboard. Click on **Confirm**, and the dashboard is deleted permanently.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image664.png){width="0.28125in" height="0.28125in"}   **Note:** once deleted, a dashboard cannot be recovered.
  ---------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 19.8 Assigning a dashboard

You can assign different dashboards to users according to their roles. For example, the overview dashboard is different for an Account Administrator and a Reporting User.

-   Click on the **settings** ![](media/image665.png){width="0.4166666666666667in" height="0.375in"} icon \> click on ![](media/image666.png){width="1.0416666666666667in" height="0.375in"}, and a screen with the option to select a role and the list of dashboards is visible, as shown below:

![](media/image667.png){width="5.0in" height="3.3125in"}

-   Select a role from the drop-down menu (e.g. Reporting User) \> click on the **add** ![](media/image642.png){width="0.3125in" height="0.3125in"} icon, and the list of dashboards below appears:

![](media/image668.png){width="5.052084426946632in" height="3.78125in"}

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** only dashboards with status set as active are visible in the list of dashboards.
  --------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-   Click on the **add** ![](media/image669.png){width="0.4375in" height="0.375in"} icon, and the dashboard is added to the list. Click on **Save Change(s)**.

-   Click on **EWARS**, and the assigned dashboard is visible, as shown below:

![](media/image670.png){width="5.0in" height="2.3541666666666665in"}

## 19.9 Assigning a dashboard to a specific user group

You can create a dashboard group and assign it to a role for viewing, as set out below.

-   Click on the **settings** ![](media/image665.png){width="0.4166666666666667in" height="0.375in"} icon \> click on ![](media/image666.png){width="1.0416666666666667in" height="0.375in"}, and the dashboard settings open.

-   Select a role from the drop-down menu (e.g. Reporting User).

-   Click on the **folder** ![](media/image671.png){width="0.375in" height="0.3125in"} icon, and the section screen below appears:

![](media/image672.png){width="5.0in" height="2.5833333333333335in"}

-   Enter the **Section Name** (e.g. COVID-19 Dashboards). Select a dashboard (e.g. Suspected COVID-19 Alerts) \> click on the **move** ![](media/image673.png){width="0.3958333333333333in" height="0.3541666666666667in"} icon, and the selected dashboard is added to the right-hand side.

-   Similarly, select one more dashboard (e.g. Weekly Aggregate Lab Report), click on the **move** ![](media/image673.png){width="0.3958333333333333in" height="0.3541666666666667in"} icon, and the dashboard is added to the right-hand side.

-   Click on **Save Change(s)**, and the section screen is closed.

-   Click on **Save Change(s)** to save the changes to the dashboard settings.

-   Click on **EWARS**, and the assigned dashboard group is visible, as shown below:

![](media/image674.png){width="4.885416666666667in" height="2.7708333333333335in"}

The following chapter explores how to use the outbreaks widget in EWARS to bring attention to ongoing outbreaks and facilitate speedy reporting.

# Chapter 20. Outbreaks

An outbreak is an occurrence of disease cases in excess of what would normally be expected in a defined community, geographical area or season. During Early Warning, Alert and Response System (EWARS) implementation, you may detect one or more outbreaks. EWARS allows users to manage outbreaks through the outbreaks function. Outbreaks added to EWARS can be seen under the outbreaks widget. [By adding an outbreaks widget to dashboards or bulletins, users can highlight ongoing outbreaks and provide easy access to the necessary reporting forms to facilitate rapid reporting.]{.mark}

For more information on this, refer to **Chapter 17. Widgets and their configuration**, topic **17.9 Outbreaks widget**.

## 20.1 Adding an outbreak in EWARS

All active outbreaks entered this way appear on the overview dashboard and on the website.

To add an outbreak in EWARS, follow the steps below.

-   Select **Menu** \> **Administration** \> **Outbreaks** \> **Create New**, and the following screen appears:

![](media/image675.png){width="5.94166447944007in" height="3.033333333333333in"}

-   Populate the fields as follows.

```{=html}
<!-- -->
```
-   **Outbreak Name** \[Mandatory\]: enter the name of the outbreak (e.g. "Cholera outbreak").

-   **Status** \[Mandatory\]: set as **Active**/**Inactive**/**Closed** according to your requirement.

-   **Start date** \[Mandatory\]: select the start date of the outbreak. You can edit the start date later.

  ---------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![](media/image43.png){width="0.65625in" height="0.3541666666666667in"}   If the start date is not clear, users can add a comment in the description section to clarify whether this is the date of the first case, the date when the emergency operations centre (EOC) was activated or when the outbreak was declared.

  ---------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-   **End date**: select the end date of the outbreak. This is not mandatory. It can be left empty for ongoing outbreaks.

-   **Description:** provide a description of the outbreak.

```{=html}
<!-- -->
```
-   Click on **Save Change(s)**, and a notification appears that the outbreak has been added.

  ---------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------
  ![](media/image43.png){width="0.65625in" height="0.3541666666666667in"}   When you define an outbreak in the Outbreaks feature, it appears in the overview dashboard and website.

  ---------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------

The overview dashboard displays a list of all the active outbreaks added under the outbreaks menu, as shown below:

![](media/image676.png){width="6.09375in" height="2.0625in"}

## 20.2 Linking reporting forms to an outbreak

You can link reporting forms in the system with the relevant outbreak.

-   Select **Menu** \> **Administration** \> **Outbreaks** \> click on the **edit** ![](media/image240.png){width="0.2833333333333333in" height="0.275in"} icon at the left-hand side of **Cholera** \> click on the **Forms** tab at the left-hand side, and the screen below appears:

![](media/image677.png){width="5.25833552055993in" height="2.691666666666667in"}

-   Select one or more forms by clicking on the relevant box \> click on **Save Change(s)**, and a notification appears that the form is associated.

## 20.3 Linking locations to an outbreak

You can define the locations in which the relevant outbreak is ongoing.

-   Select **Menu** \> **Administration** \> **Outbreaks**. Click on the **edit** ![](media/image240.png){width="0.2833333333333333in" height="0.275in"} icon of the relevant outbreak \> click on the **Locations** tab at the left-hand side. Click on the **folder** ![](media/image678.png){width="0.25in" height="0.24166666666666667in"} icon \> select the required location, and selected locations are displayed at the right-hand side, as shown below:

![](media/image679.png){width="5.9in" height="2.575in"}

-   Click on **Save Change(s)**, and a notification appears that the locations have been added.

## 20.4 Viewing existing outbreaks

-   Select **Menu** \> **Administration** \> **Outbreaks**, and a tabular listing of all the available outbreaks in the system appears, as shown below:

![](media/image680.png){width="5.925in" height="2.6333333333333333in"}

The following outbreak details are shown in the above screenshot:

-   **Outbreak Name** -- showing the name of the outbreak

-   **Status** -- showing whether the outbreak is active, inactive or closed

-   **Start date** -- showing the start date of the outbreak

-   **End date** -- showing the end date of the outbreak

-   **Locations** -- showing the count of locations with which the outbreak is associated

-   **Forms** -- showing the reporting forms with which the outbreak is associated

-   **Created** -- showing the date and time of the outbreak creation

-   **Modified** -- showing the date and time of the outbreak modification.

## 20.5 Editing an outbreak

-   Select **Menu** \> **Administration** \> **Outbreaks**. Click on the **edit** ![](media/image240.png){width="0.2833333333333333in" height="0.275in"} icon \> make the desired changes \> click on **Save Change(s)**, and a notification appears that the outbreak has been edited.

## 20.6 Deleting an outbreak

-   Select **Menu** \> **Administration** \> **Outbreaks**. Click on the **delete** ![](media/image681.png){width="0.275in" height="0.2833333333333333in"} icon \> click on **Confirm**, and a notification appears that the outbreak is deleted.

The following chapter explores the Documents and Document Templates features, which can be used to disseminate crucial data collected in the system rapidly with stakeholders, and trigger necessary action.

# Chapter 21. Documents and Document Templates

Documents in the Early Warning, Alert and Response System (EWARS) refer to bulletins. These are used to disseminate key data collected in the system. The terms "bulletins" and "documents" are used interchangeably, and the terms "document template" and "bulletin template" convey the same meaning.

EWARS facilitates automated production of bulletins. Once a document template for a specific bulletin is configured, there is no need to produce that bulletin manually daily, weekly or monthly: bulletin template creation is a one-off activity.

## 21.1 Configuring a bulletin template

EWARS recommends that you use the standardized sample bulletin template to allow for standardization and consistency of branding across EWARS documents/bulletins. The Model account provides you with this recommended template. If required, you can customize the template to suit your context.

There are two ways to configure a bulletin template in the system.

-   **Either** use a sample bulletin template: the Model account has a sample bulletin template (the Sample Weekly EWARS bulletin) which you can transfer to your account and modify according to your country's requirements

  ---------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![](media/image43.png){width="0.65625in" height="0.3541666666666667in"}   The Sample Weekly EWARS bulletin is the standard bulletin. EWARS recommends a similar pattern and outlook of bulletins for all accounts. This allows standardization across all EWARS accounts and comparisons between contexts.

  ---------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-   **Or** create a new bulletin template: you can create and configure a new bulletin template according to your country's requirements.

  ---------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![](media/image43.png){width="0.65625in" height="0.3541666666666667in"}   Modifying a sample bulletin template or creating a new one should be an end-stage activity of setting up an EWARS account. Before embarking on this activity, please ensure that the Locations, Forms and Indicators features are correctly configured in the system.

  ---------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** creating a new bulletin template or modifying complex parts of the sample bulletin template, such as adding new sections, adding rows in tables and similar, requires knowledge of Hypertext Markup Language (HTML) and Cascading Style Sheets (CSS). For technical support on the bulletin template, please contact the EWARS Super Administrator.
  --------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The screenshot below is of a standard bulletin produced for week 31 of 2021:

![](media/image682.png){width="3.838542213473316in" height="5.757812773403325in"}

## 21.2 Transferring the sample bulletin template

The sample bulletin template is in the Model account. Transfer it to your account using the following steps.

-   Select **Menu** \> **Configuration Transfer**. Select **Model account** from the **Source Account** drop-down menu. The system lists all transferable items. Search and select **Sample Weekly EWARS Bulletin** \> click on ![](media/image683.png){width="1.0916666666666666in" height="0.4in"}, and the sample template is transferred to your account, along with its dependencies.

To view the template in your account, follow the steps below.

-   Select **Menu** \> **Document Templates**, and the bulletin template is listed, as shown below:

![](media/image684.png){width="5.564722222222223in" height="2.1030555555555557in"}

-   Click on the **edit** ![](media/image685.png){width="0.2916666666666667in" height="0.2833333333333333in"} icon of Sample Weekly EWARS Bulletin \> click on the **Template** tab at the left-hand side, and the HTML editor screen below appears:

![](media/image686.png){width="5.64173665791776in" height="2.8636811023622046in"}

The above screenshot shows the editor screen in which the template is designed. The following topic sets out how to modify the sample bulletin template according to your country's requirements.

## 21.3 Modifying the sample bulletin template

The sample bulletin is not functional on its own: you need to modify it according to your requirements and reconfigure it with the data available in your account to make it functional. The list of modifications is as follows:

-   modifying the bulletin template settings

-   modifying the front page -- including modifying text and images on the front page

-   modifying the analysis page -- including modifying the heading of any section, reconfiguring widgets and adding or removing sections in bulletin template and rows in tables

-   modifying the last page -- including modifying the contact information on the last page.

### 21.3.1 Modifying the template settings

-   Select **Menu** \> **Document Templates**. Click on the **edit** ![](media/image687.png){width="0.35833333333333334in" height="0.3416666666666667in"} icon of the Sample Weekly EWARS Bulletin, and the screen below appears:

![](media/image688.png){width="7.0in" height="3.1951388888888888in"}

-   Modify the fields as follows.

```{=html}
<!-- -->
```
-   **Template name** \[Mandatory\]: modify the template name (e.g. "Nambutu Weekly EWARS Bulletin").

-   **Instance name** \[Mandatory\]: modify the instance name -- this format appears in the Documents feature when you view it, as in the following example:

+----------------------------------------------------------------+-------+-------------------------------------------------------------------+
| > Instance name                                                | **→** | Generated bulletin name                                           |
| >                                                              |       |                                                                   |
| > ***{location_name} Weekly EWARS Bulletin -- {report_date}*** |       | ***Nambutu Weekly EWARS Bulletin -- W16 2021 \| 18 -- 24 April*** |
+----------------------------------------------------------------+-------+-------------------------------------------------------------------+

> Here, **{report_date}** is a tag/special purpose variable. When it is used, the system replaces **{report_date}** with the week number and calendar date (e.g. W16 2021 \| 18 -- 24 April).\
> \
> The tag/special purpose variable is used to display specific values like the current month, year and location in the document. For example, the location name can be added as **{location_name}**.
>
> All tags, along with their purposes, are listed under the **Help** tab.

-   **UUID (universally unique identifier):** this is a system-generated unique number and cannot be edited.

-   **PDF Page Orientation**: set as **Portrait**.

-   **Status**: set as **Active**.

    **Active** -- the template that is configured and is in use

    **Draft** -- the template that is being configured

    **Inactive** -- inactive bulletins do not appear in the Documents feature

-   **Description:** modify the description of the bulletin template.

-   **Tag:** enter a tag for the bulletin template: this is an identifier that will help you to find your template using Configuration Transfer. You can add one or more tags.

-   **Generation:** the system generates a bulletin in accordance with time interval and location specification settings. To understand this function better, refer to the following examples.

**Example 1.** Generate a bulletin for Nambutu on a weekly basis for 2021.

-   Set **Interval** as **Weekly** \> set **Location spec.** as **Generate for specific location** \> set **Location** as Nambutu \> select the **Start date** 2021-01-01 in the calendar \> select the **End date** 2021-12-31 in the calendar, as shown below:

![A screenshot of a computer Description automatically generated with medium confidence](media/image689.png){width="4.75in" height="1.7166666666666666in"}

The bulletin is auto-generated for each week for Nambutu for 2021.

**Example 2.** Generate a bulletin for each province of Nambutu on a weekly basis for 2021.

![A screenshot of a computer Description automatically generated with medium confidence](media/image690.png){width="4.791666666666667in" height="1.9916666666666667in"}

-   Set **Interval** as **Weekly** \> set **Location spec** as **Generate for type** \> set **Location** as **Nambutu** \> set **Location type** as **Province** \> select the **Start date** 2021-01-01 in the calendar \> select the **End date** 2021-12-31 in the calendar, as shown below:

The bulletin is auto-generated for each week for all the provinces of Nambutu for 2021.

-   **Access constraints**: set as **Public**.

    **Public** -- the bulletin is accessible without logging into EWARS via an external link.

    **Private** -- the bulletin is accessible only for EWARS users who are logged in.

```{=html}
<!-- -->
```
-   Click on **Save Change(s)**.

### 21.3.2 Modifying the front page

You can change any text or images available on the front page of the sample bulletin. For demonstration purposes, this guide shows how to modify the country name and logo highlighted below:

![](media/image691.png){width="7.0in" height="3.6020833333333333in"}

**Step 1.** Modify the text on the front page*.*

-   Select **Menu** \> **Document Templates**. Click on the **edit** ![](media/image687.png){width="0.35833333333333334in" height="0.3416666666666667in"} icon of Sample Weekly EWARS Bulletin \> click on the **Template** tab, and the HTML editor screen appears.

-   Keep the cursor on **Model Country** \> click **delete** and delete the text "Model Country". Type the new name and the text is changed.

Use the same process to change any text on the front page.

**Step 2.** Modify images on the front page.

The front page contains images of logos, flags or photos. These should be uploaded and saved under web content. Hence, modifying images is a two-step process.

**Step 1.** Upload an image to web content.

First, select images you want to upload to web content: they should be in your laptop/desktop folder.

-   Select **Menu** \> **Document Templates**. Click on the **edit** ![](media/image687.png){width="0.35833333333333334in" height="0.3416666666666667in"} icon of Sample Weekly EWARS Bulletin \> click on the **Template** tab, and the HTML editor screen appears.

```{=html}
<!-- -->
```
-   Click on ![](media/image692.png){width="1.0333333333333334in" height="0.3in"}, and the **Web Content** screen opens in a new tab, as shown below:

![](media/image693.png){width="4.975in" height="1.725in"}

-   Click on ![](media/image694.png){width="1.1083333333333334in" height="0.2833333333333333in"} \> select the relevant **Folder Path** (e.g. images) \> click on ![](media/image695.png){width="0.75in" height="0.275in"}, and a file chooser dialogue box opens. Select an image file, and the file is uploaded.

-   Look for the newly uploaded file and click on the **copy** ![](media/image696.png){width="0.3in" height="0.2833333333333333in"} icon of the uploaded image \> close the **Web Content** browser tab, and you will be back on the editor screen.

The image file is now uploaded. The second step is to provide the copied universal resource locator (URL) of the uploaded image.

**Step 2.** Modify the image URL.

-   Double-click on the sample image you want to modify, and the **Image Properties** screen below opens:

![](media/image653.png){width="3.175in" height="3.4in"}

-   Replace the **URL** under the **Image Info** tab with the copied URL of the uploaded image \> enter the new **Width** in pixels (e.g. "100") \> enter the new **Height** in pixels (e.g. "100") \> click on **OK**.

-   Click on **Save Change(s)**, and the front page appears with the new text and logos.

### 21.3.3 Modifying the analysis pages

Analysis pages follow a standard structure, and modification is needed in specific places, including:

-   modifying the heading of any section

-   reconfiguring widgets

-   adding or removing sections in the bulletin template and rows in tables.

**Step 1.** Modify the heading of any section.

You can modify any section heading or subheading. For demonstration purposes, this guide shows how to change the section heading "C. Trend in consultations", as highlighted below:

![](media/image697.png){width="4.941666666666666in" height="1.9666666666666666in"}

-   Select **Menu** \> **Document Templates** \> click on the **edit** ![](media/image687.png){width="0.35833333333333334in" height="0.3416666666666667in"} icon of Sample Weekly EWARS Bulletin \> click on the **Template** tab, and the HTML editor screen appears.

-   Look for section C. Trend in consultations in the bulletin template. Keep the cursor on this section, click **delete** and delete the text "Trend in consultations". Enter the new heading name (e.g. "Trend in attend"), and the heading is changed, as shown below:

> ![](media/image698.png){width="4.96875in" height="2.1406255468066493in"}

Use the same steps to modify other headings of the section if required.

-   Click on **Save Change(s)**.

**Step 2.** Reconfigure the widget's indicators, forms and locations, according to your requirements.

The sample bulletin template contains the following types of widgets:

-   raw widget

-   series widget

-   map widget

-   table widget

-   category widget.

To modify each widget, follow the steps below.

-   Select **Menu** \> **Document Templates**. Click on the **edit** ![](media/image687.png){width="0.35833333333333334in" height="0.3416666666666667in"} icon of Sample Weekly EWARS Bulletin \> click on the **Template** tab, and the HTML editor screen appears. Scroll down and look for the widget to be modified, as shown below:

![](media/image699.png){width="4.95in" height="1.95in"}

-   Double-click on the widget, and the widget configuration screen below appears:

![](media/image655.png){width="4.966666666666667in" height="2.5in"}

-   Configure the widget as required. For more information about configuring widgets, refer to the relevant widget topic in **Chapter 17. Widgets and their configuration** as listed below:

```{=html}
<!-- -->
```
-   raw widget -- refer to topic **17.6.2 Raw widget in Bulletins and Website Builder**

-   series widget -- refer to topic **17.18 Series chart widget**

-   map widget -- refer to topic **17.16 Map widget**

-   table widget -- refer to topic **17.21 Table widget**

-   category widget -- refer to topic **17.20 Category widget**

```{=html}
<!-- -->
```
-   Click on **Save Change(s)**.

**Step 3.** Add or remove sections in the bulletin template and rows in the table.

Adding or removing a section or a row in a table requires knowledge of HTML and CSS. To perform any such modifications in the bulletin template, please contact the EWARS Super Administrator for technical support.

### 21.3.4 Modifying the final page

On the final page of the sample bulletin template, you need to change the contact information as highlighted in the screenshot below:

![](media/image700.png){width="7.0in" height="2.7291666666666665in"}

-   Select **Menu** \> **Document Templates**. Click on the **edit** ![](media/image685.png){width="0.2916666666666667in" height="0.2833333333333333in"} icon of Sample Weekly EWARS Bulletin. Click on the **Template** tab, and an HTML editor screen appears.

-   Scroll down to the bottom and look for the section on help and support as shown below:

![](media/image701.png){width="4.941666666666666in" height="2.2in"}

-   Place the cursor on the name of the contact person \> **delete** it \> **enter** the name and telephone number of the contact person for your country.

-   Click on **Save Change(s)**.

## 21.4 Creating a new bulletin template

Creating a new template requires basic knowledge of HTML and CSS. For technical support, please contact the EWARS Super Administrator.

You can create a new bulletin template by following the steps below.

**Step 1.** Configure general settings.

-   Select **Menu** \> **Document Templates**. Click on **New**, and the screen below appears:

![](media/image702.png){width="5.0in" height="2.4in"}

-   Populate the fields under the **Settings** tab. For information on how to populate these, refer to topic **21.3.1 Modifying the template settings**.

**Step 2.** Design the bulletin template.

The top-level guidelines on how to design a new template are set out below. It is a powerful way to add content, but it requires knowledge of HTML and CSS. For technical support on creating a bulletin template, please contact the Super Administrator.

-   Select **Template** tab and the document template editor opens, as shown below:

![](media/image703.png){width="4.941666666666666in" height="2.2583333333333333in"}

-   Insert sections and pages using HTML and CSS.

-   Enter section headings, subheadings and text, and format them.

-   Insert widgets such as table, image, series, category, pyramid and/or map widgets.

```{=html}
<!-- -->
```
-   Configure each of the widgets inserted. For more information on how to configure widgets, refer to **Chapter 17. Widgets and their configuration**.

```{=html}
<!-- -->
```
-   Configure special purpose variables/tags to display specific values like the current month, year and location in the document. For example, the location name can be added as **"{location_name}"**. More information on tags is listed under the **Help** tab.

```{=html}
<!-- -->
```
-   Click on **Save Change(s)**, and a notification appears that the template has been added.

## 21.5 Deleting and duplicating an existing bulletin template

To delete a bulletin template, follow the steps below.

-   Select **Menu** \> **Document Templates**. Click on the **delete** ![](media/image319.png){width="0.35833333333333334in" height="0.3416666666666667in"} icon of the bulletin template (e.g. Sample Weekly EWARS Bulletin). Click on **Confirm** and it is deleted.

To duplicate a bulletin template, follow the steps below.

-   Select **Menu** \> **Document Templates**. Click on the **duplicate** ![](media/image704.png){width="0.35833333333333334in" height="0.3416666666666667in"} icon of the bulletin template (e.g. Sample Weekly EWARS Bulletin). Edit the **Template name** \> click on **Save Change(s)**, and the template is duplicated.

## 21.6 Viewing bulletins

To view the bulletins available in your account, follow the steps below.

-   Select **Menu** \> **Documents**, and the screen below appears:

![](media/image705.png){width="4.975in" height="1.8333333333333333in"}

The bulletins available in your account are listed at the left-hand side as shown above.

-   Click on the **bulletin name** (e.g. Sample Weekly EWARS Bulletin), and bulletins are listed, by year, in the right-hand side panel, as shown below:

![](media/image706.png){width="4.966666666666667in" height="2.4583333333333335in"}

-   Select the year for which you want the bulletin (e.g. 2021). Click on the **view** ![](media/image707.png){width="0.31666666666666665in" height="0.275in"} icon at the right-hand side of the bulletin. Wait for few seconds while the bulletin loads completely, and the screen below appears:

![](media/image708.png){width="4.983333333333333in" height="2.375in"}

-   Click on the **collapse** ![](media/image709.png){width="0.2916666666666667in" height="0.275in"} icon to close the side panel.

## 21.7 Viewing a bulletin in a new browser window/tab

-   Select **Menu** \> **Documents**. Select the document name (e.g. Sample Weekly EWARS Bulletin) \> select the year (e.g. 2021). Click on the **new window** ![](media/image710.png){width="0.2916666666666667in" height="0.325in"} icon at the right-hand side of the bulletin, and the bulletin opens in a new browser window/tab.

## 21.8 Downloading a bulletin as a PDF file

-   Select **Menu** \> **Documents**. Select the document name (e.g. Sample Weekly EWARS Bulletin) \> select the year (e.g. 2021). Click on the **PDF** ![](media/image612.png){width="0.3in" height="0.31666666666666665in"} icon at the right-hand side of the bulletin. Wait for a few seconds while the PDF is prepared, and the PDF is downloaded.

## 21.9 Sharing a bulletin

You can share the bulletins in two different ways: via email or via a copied URL link.

### 21.9.1 Sharing via email

-   Select **Menu** \> **Documents** \> select the relevant document (e.g. Sample Weekly EWARS Bulletin) \> select the year (e.g. 2021) \> click on the **transfer** ![](media/image711.png){width="0.31666666666666665in" height="0.2833333333333333in"} icon at the right-hand side of the bulletin, and the popup screen below appears:

![](media/image712.png){width="4.991666666666666in" height="1.7916666666666667in"}

-   Enter the email address/addresses separated by a comma (,) \> click on **Share**, and the bulletin is shared to the email address/addresses entered.

### 21.9.2 Sharing via a copied URL link

-   Select **Menu** \> **Documents** \> select the relevant document (e.g. Sample Weekly EWARS Bulletin) \> select the year (e.g. 2021) \> click on the **copy** ![](media/image713.png){width="0.3in" height="0.3in"} icon at the right-hand side of the bulletin \> share the copied URL link using email or any medium.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** the bulletin shared must have access set as public or it will not be accessible.
  --------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The following chapter provides an overview of the Website Builder feature. It will help you build public-facing EWARS websites and share important data and reports with key personnel not registered as EWARS users.

#  

# Chapter 22. Website Builder

The Website Builder feature facilitates development of public-facing Early Warning, Alert and Response System (EWARS) websites. It helps with sharing data and reports with personnel not registered as EWARS users. It provides an excellent way of sharing key information with personnel of WHO, the ministry of health or health partners and donors: audiences who are not part of the EWARS reporting mechanism. The intended audience can access EWARS websites just like other live sites on the web. Multiple websites can be built under each account to fulfil different needs. While developing such sites using the Website Builder feature is largely self-explanatory, possessing a basic understanding of Hypertext Markup Language (HTML) and Cascading Style Sheets (CSS) is useful. This chapter contains key information about using the Website Builder feature.

## 22.1 Configuring a website

There are two ways to configure a website in the system:

-   copy and modify the sample website

-   create a new website

Before you embark on this activity, ensure that locations, indicators and forms are correctly configured in the system. Creating a website should be the last activity, having established a proper early warning system.

  ---------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![](media/image43.png){width="0.65625in" height="0.3541666666666667in"}   It is recommended to use the standard template provided in the Model account to build your website. If you need any technical support in building an EWARS website, please contact the EWARS Super Administrator*.*

  ---------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The sample website is accessible at [[https://sampleweb.ewars.ws]{.underline}](https://sampleweb.ewars.ws/), as shown below:

![](media/image714.png){width="5.0in" height="3.3333333333333335in"}

The following topic sets out how to copy the sample website and modify it. All EWARS websites should have similar formatting. The contents can differ, but it is recommended to follow the same landing page and similar page structures.

## 22.2 Copying the sample website

The sample website is in the Model account. To use it, you first need to copy it to your account, following the steps below.

-   Select **Menu** \> **Configuration Transfer**. Select **Model account** from the **Source Account** drop-down menu. The system lists all transferable items. Click on the **filter** ![](media/image715.png){width="0.2708333333333333in" height="0.2708333333333333in"} icon of the **Type** column: filter options are visible. In the **Filter by condition** drop-down menu, select **Website** and click on **Save**. All the sample websites are listed. Select **Sample Website** (sampleweb.ewars.ws). Click on ![](media/image716.png){width="1.1041666666666667in" height="0.3958333333333333in"}, and the sample website is copied to your account, along with its dependencies.

To view the website under Website Builder in the EWARS account, follow the steps below.

-   Select **Menu** \> **Website Builder**, and the sample website appears in the list, as shown below:

![](media/image717.png){width="5.79166447944007in" height="2.3645833333333335in"}

You can also view the website as a preview.

-   Click on the **edit** ![](media/image307.png){width="0.3541666666666667in" height="0.3333333333333333in"} icon of the website (e.g. Sample website ([[sampleweb.ewars.ws]{.underline}](https://sampleweb.ewars.ws/))), and the website editor screen opens. Click on ![](media/image718.png){width="0.9583333333333334in" height="0.3125in"}, and the sample website opens in a new browser tab.

The following topic sets out how to modify the sample website according to your requirements.

## 22.3 Modifying the sample website

Successful transfer of the website does not make it functional: you need to modify it so that your website displays information relevant to your context. Once the website is modified, you can publish it.

The screenshot below shows the header page, homepage and footer page that you can modify according to your requirements:

![](media/image719.png){width="5.331423884514436in" height="7.802083333333333in"}

The following topics demonstrate the five key modifications you can make to the sample website:

-   modifying the site settings

-   modifying the header page

-   modifying the footer page

-   modifying the homepage

-   adding or removing a new page.

### 22.3.1 Modifying the site settings

Site settings capture and store basic information such as name, domain, description and status for the website. The steps to modify these are as follows.

-   Select **Menu** \> **Website Builder**. Click on the **edit** ![](media/image307.png){width="0.3541666666666667in" height="0.3333333333333333in"} icon of the sample website, and the editor screen below appears:

![](media/image720.png){width="5.79166447944007in" height="2.9791666666666665in"}

-   Click on ![](media/image721.png){width="1.28125in" height="0.3125in"}, and the site settings open, as shown below:

![](media/image722.png){width="4.958333333333333in" height="2.9166666666666665in"}

-   Give a **Website Name** (e.g. "Country X EWARS website").

-   Set the appropriate **Status** option:

```{=html}
<!-- -->
```
-   **Published** -- the website is ready to use and accessible via the universal resource locator (URL)

-   **Unpublished** -- the website is not ready to use: unpublished status allows you to keep the website in a draft state before publishing. The following message appears when an unpublished website is accessed:

![](media/image723.png){width="5.0in" height="0.6875in"}

-   Enter the **Domain** of the website. By design, the domain is the same as the one under which the EWARS account is running. You cannot deliver the published website on a different URL. In the case of WHO hosting the server, it is "ewars.ws". Thus, the user can enter the subdomain of the "ewars.ws" domain. This is the URL/access point for the website.

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** subdomains are the part of a domain that comes before the main domain name and domain extension.
  --------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The domain name comprises two components: the first part (that you choose) and second (fixed) part (e.g. "xxx.ewars.ws", where "xxx" is the configurable part that you choose and ".ewars.ws" is the fixed part):

![](media/image724.png){width="4.395833333333333in" height="1.84375in"}

As illustrated above, **sampleweb** is the subdomain and **ewars.ws** is the domain. If the subdomain chosen is being used elsewhere, the following message is shown:

![](media/image725.png){width="2.0in" height="0.25in"}

Replace it with an unused subdomain.

-   Modify the **Description** (e.g. enter information about the purpose of the website, a target audience and special configuration points) likely to be useful in maintenance of the website.

-   Enter a **Tag** for the sample website. A tag is an identifier that will help you to find your website in the Configuration Transfer menu. You can add one or more tags.

-   ![](media/image726.png){width="1.3958333333333333in" height="0.3125in"} allows you to upload a CSS or JavaScript (JS) file to apply styles, but this is not mandatory. To create these files, you need knowledge of HTML and CSS and/or JS, but if you have no prior knowledge of these, you do not need to upload a file: failing to do so will not affect the existing style of the website. If you need further information or support, please contact the EWARS Super Administrator.

```{=html}
<!-- -->
```
-   Click on the ![](media/image726.png){width="1.3958333333333333in" height="0.3125in"}, and a file chooser dialogue box opens. Select a JS or CSS file and upload it.

-   When you don't need the file any more, click on the **delete** ![](media/image727.png){width="0.28125in" height="0.3125in"} icon to delete it.

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** CSS or JS are powerful ways to apply styling to a website, although this requires technical knowledge of HTML, CSS and/or JS. For technical support on CSS or JS files, please contact the EWARS Super Administrator.
  --------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-   Click on **Save Change(s)**; the site settings are modified, and you can open the website using the new domain.

### 22.3.2 Modifying the header page

The header page of the website contains the country name, logo and link button. These are annotated and highlighted below:

![](media/image728.png){width="5.6875in" height="1.0833333333333333in"}

To modify the header, follow the steps below.

-   Select **Menu** \> **Website Builder**. Click on the **edit** ![](media/image307.png){width="0.3541666666666667in" height="0.3333333333333333in"} icon of the website, and the website editor opens. By default, **Header Page** is selected in the page drop-down menu at the top left-hand corner \> click on the first row with the label **HTML**, and the widget configuration screen opens.

**Step 1.** Modify the country name.

-   Keep the cursor on **Nambutu Country** \> click the **Backspace** key to delete it. Enter the name of your country.

**Step 2.** Modify images on the header page.

Images on the header page include logos, flags and photos***.*** It is recommended that image sizes should not exceed 2GB to avoid performance degradation after uploading.

These images should be uploaded to web content first, so modifying them is a two-step process.

**Step 1.** Upload the images to web content.

First, select images you want to upload to web content: they should be in your laptop/desktop folder.

-   Click on ![](media/image729.png){width="1.0416666666666667in" height="0.2916666666666667in"}, and the **Web Content** screen opens in a new tab, as shown below:

![](media/image693.png){width="4.979166666666667in" height="1.7291666666666667in"}

-   Click on ![](media/image650.png){width="1.1041666666666667in" height="0.2916666666666667in"} \> select the relevant **Folder Path** (e.g. images) \> click on ![](media/image651.png){width="0.75in" height="0.2708333333333333in"}, and a file chooser dialogue box opens. Select a logo file, and the logo is uploaded. Look for the newly uploaded file and click on the **copy** ![](media/image652.png){width="0.2916666666666667in" height="0.2916666666666667in"} icon of the uploaded image \> close the **Web Content** browser tab, and you will be back on the Website Builder configuration screen.

The logo image file is now uploaded. The second step is to provide the copied URL of the uploaded image.

**Step 2.** Modify the image URL.

-   Double-click on the image you want to modify, and the **Image** **Properties** screen below opens:

![](media/image653.png){width="3.15625in" height="3.3958333333333335in"}

-   Replace the URL under the **Image Info** tab with the copied URL of the uploaded image \> enter the new **Width** in pixels (e.g. "100") \> enter the new **Height** in pixels (e.g. "100") \> click on **OK** to close the dialogue box, and the image is replaced.

**Step 3.** Link the ![](media/image730.png){width="0.7708333333333334in" height="0.3333333333333333in"} button so that it gets redirected to [<http://ewars.ws>.]{.underline}

-   Select the text **EWARS Login** in the![](media/image730.png){width="0.7708333333333334in" height="0.3333333333333333in"} button \> click on the **link** ![](media/image731.png){width="0.3645833333333333in" height="0.3333333333333333in"} icon, and the link screen below appears:

![](media/image732.png){width="3.9895833333333335in" height="3.75in"}

-   Enter "ewars.ws" in the **URL** field \> click on **OK** \> click on **Save widget changes**, and the widget closes.

-   Click on **Save Change(s)** -- the header page changes are saved, and the button is now linked to the EWARS login page.

-   Click on ![](media/image733.png){width="0.875in" height="0.25in"} \> click on ![](media/image730.png){width="0.7708333333333334in" height="0.3333333333333333in"}, and the EWARS login page appears, as shown below:

![](media/image734.png){width="5.41666447944007in" height="2.8541666666666665in"}

### 22.3.3 Modifying the footer page

The footer page contains the country name, project description and logo. These are annotated and highlighted below:

![](media/image735.png){width="5.065564304461942in" height="1.6021314523184602in"}

To modify the footer, follow the steps below.

-   Select **Menu** \> **Website Builder**. Click on the **edit** ![](media/image307.png){width="0.3541666666666667in" height="0.3333333333333333in"} icon of the website, and the website editor opens. Select **Footer Page** from the drop-down menu at the top left-hand corner \> click on the first row with the label **HTML**, and the widget configuration screen below appears:

![](media/image736.png){width="5.73579615048119in" height="2.6289063867016624in"}

**Step 1.** Modify the country name.

-   Keep the cursor on **Nambutu Country** \> click the **Backspace** key to delete it. Enter the name of your country. Similarly, change the description.

**Step 2.** Modify images on the footer page.

Images on the footer page include logos and flags*.* These images should be uploaded to web content, so modifying them is a two-step process.

**Step 1.** Upload the images to web content.

First, select images you want to upload to web content: they should be in your laptop/desktop folder.

-   Click on ![](media/image737.png){width="1.0416666666666667in" height="0.2916666666666667in"}, and the **Web Content** screen opens in a new tab, as shown below:

![](media/image693.png){width="4.979166666666667in" height="1.7291666666666667in"}

-   Click on ![](media/image738.png){width="1.0833333333333333in" height="0.2916666666666667in"} \> select the relevant **Folder Path** (e.g. images) \> click on ![](media/image651.png){width="0.75in" height="0.2708333333333333in"}, and a file chooser dialogue box opens. Select a logo file, and the logo is uploaded. Look for the newly uploaded file and click on the **copy** ![](media/image652.png){width="0.2916666666666667in" height="0.2916666666666667in"} icon of the uploaded image \> close the **Web Content** browser tab, and you will be back on the Website Builder configuration screen.

The logo image file is now uploaded. The second step is to provide the copied URL of the uploaded image.

**Step 2.** Modify the image URL.

-   Double-click on the image you want to modify, and the **Image Properties** screen below opens:

![](media/image653.png){width="3.15625in" height="3.3958333333333335in"}

-   Replace the URL under the **Image Info** tab with the copied URL of the uploaded image \> enter the new **Width** in pixels (e.g. "100") \> enter the new **Height** in pixels (e.g. "100") \> click on **OK** to close the dialogue box, and the image is replaced.

-   Click on **Save Change(s)** -- the changes are saved, and the widget closes.

-   Click on **Save Change(s)**, and the footer page changes are saved.

```{=html}
<!-- -->
```
-   Click on ![](media/image718.png){width="0.9583333333333334in" height="0.3125in"} to view the applied changes.

### 22.3.4 Modifying the homepage content

The homepage contains text paragraphs, images, image carousels and video widgets. These are annotated and highlighted below:

![](media/image739.png){width="5.0in" height="3.7708333333333335in"}

To find out more about configuring widgets, refer to the relevant widget topic in **Chapter 17. Widgets and their configuration**.

For demonstration purposes, this guide shows how to modify the text paragraph, add a new image to the carousel and modify the video.

-   Select **Menu** \> **Website Builder**. Click on the **edit**![](media/image307.png){width="0.3541666666666667in" height="0.3333333333333333in"}￼ icon of the sample website, and the website editor opens**.** Select **Home** from the page drop-down menu at the top left-hand corner, and the homepage configuration screen below appears:

![](media/image740.png){width="6.08333552055993in" height="2.8645833333333335in"}

Follow the steps below to perform the modifications in the highlighted widgets of the screenshot above.

**Step 1.** Change the text paragraph.

-   As shown in the screenshot above, click on the first row with the label **Text**, and the text widget configuration screen opens, as shown below:

![](media/image741.png){width="5.70833552055993in" height="3.9375in"}

-   Replace the text in the **Content** field with your desired content \> click on **Save Change(s)** -- the changes are saved and the widget closes.

**Step 2.** Add an image and related text to the carousel.

The carousel widget allows you to add multiple images in a single space.

-   On the homepage configuration screen, click on the cell with the label **Carousel**, and the widget editor screen below appears:

![](media/image742.png){width="4.958333333333333in" height="3.6354166666666665in"}

-   Click on ![](media/image743.png){width="1.0in" height="0.3333333333333333in"}, and an image URL row is added. Click on the **edit** ![](media/image307.png){width="0.3541666666666667in" height="0.3333333333333333in"} icon.

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** it is recommended that sizes should be kept identical for all the images you upload.
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-   Click on the **upload** ![](media/image744.png){width="0.2916666666666667in" height="0.3333333333333333in"} icon to upload the image, and the image URL is added. Alternatively, you can enter the URL in the **Image URL** field.

-   Enter **Image Text** (e.g. "Polio networks bolster pandemic response in the WHO South-East Asia Region").

-   Click on **Save Change(s)** -- the changes are saved, and the widget closes.

**Step 3.** Change the video.

-   On the homepage configuration screen, click on the cell with the label **Video**, and the widget editor opens, as shown below:

![](media/image745.png){width="5.52083552055993in" height="2.90625in"}

-   Replace the **Video URL** with your desired YouTube URL (e.g. <https://www.youtube.com/watch?v=-tKH6XARTG4)>.

  ---------------------------------------------------------------------------------- -------------------------------------------------------------
  ![](media/image43.png){width="0.65625in" height="0.3541666666666667in"}   Only YouTube URLs are supported in the video widget.

  ---------------------------------------------------------------------------------- -------------------------------------------------------------

-   Click on **Save Change(s)** -- the changes are saved, and the widget closes.

In addition to the modifications explained above, you can also add a new row to the homepage, with widgets like documents and outbreaks widgets, as shown below:

![](media/image746.png){width="5.604166666666667in" height="3.9696172353455816in"}

Follow the steps below to add a new row with two widgets: documents and outbreaks widgets.

**Step 1.** Add a documents widget in the left-hand cell.

The documents widget allows you to give the public access to the Weekly EWARS Bulletin or any other bulletin produced in EWARS.

-   On the homepage configuration screen, drag and drop a **Row** widget from the left-hand side to the mid-section, and a new row is added. Drag and drop a **Cell** widget onto the added row, and the row is divided into two vertical cells. Click on the **expand** ![](media/image505.png){width="0.24166666666666667in" height="0.24166666666666667in"} icon to expand the **Other** category \> drag a **Documents** widget to the left-hand cell.

-   Right-click on the cell, and cell options are visible. Click on ![](media/image747.png){width="1.4166666666666667in" height="0.3125in"} to move the row up to between the **HTML** and the **Video** widgets, as shown below:

![](media/image748.png){width="6.714285870516186in" height="1.978982939632546in"}

-   Click on the cell with the label **Documents**, and the documents widget editor opens, as shown below:

![](media/image749.png){width="5.54166447944007in" height="2.7708333333333335in"}

-   Select **Sample Weekly EWARS Bulletin** in the **Document Templates** field \> click on **Save Change(s)** -- the changes are saved, and the widget closes.

**Step 2.** Add an outbreaks widget to the right-hand cell.

The outbreaks widget allows you to display ongoing and concluded outbreaks in your context.

-   Click on the **expand** ![](media/image505.png){width="0.23958333333333334in" height="0.23958333333333334in"} icon to expand the **User** category \> drag and drop an **Outbreaks** widget onto the right-hand cell.

-   Click on the cell, and the outbreaks widget editor opens, as shown below:

![](media/image750.png){width="5.52083552055993in" height="3.0833333333333335in"}

-   Enter a title for the widget (e.g. "Active Outbreaks").

-   Click on **Save Change(s)** -- the changes are saved, and the widget closes.

To edit the outbreak details, refer to **Chapter 20. Outbreaks**.

-   Click on **Save Change(s)**, and the homepage content changes are saved.

-   Click on ![](media/image733.png){width="0.875in" height="0.25in"} to view the applied changes.

### 22.3.5 Adding or removing a new page

It is recommended that you retain the standard structure, but you can add pages under the various sections if required.

For demonstration purposes, this guide shows how to remove two pages (Hep E Outbreak (Jan -- Nov 2020) and Cholera Outbreak (Aug 19 -- Mar 21)) and to add one page (Malaria Outbreak (ongoing)) to the outbreaks menu, as shown below:

![](media/image751.png){width="4.979166666666667in" height="1.2708333333333333in"}

Follow the steps below to remove and add pages.

-   Select **Menu** \> **Website Builder**. Click on the **edit** ![](media/image307.png){width="0.3541666666666667in" height="0.3333333333333333in"} icon, and the website editor opens. Keep **Header Page** selected in the drop-down menu visible at the top left-hand corner \> click on the second row with the label **Menu**, and the menu editor below appears:

![](media/image752.png){width="5.66666447944007in" height="2.625in"}

**Step 1.** Remove the menu items for the hepatitis E and cholera outbreaks.

-   Click on the **expand** ![](media/image753.png){width="0.25in" height="0.3333333333333333in"} icon in the **Outbreaks** menu, and the menu expands, as shown below:

![](media/image754.png){width="4.9375in" height="3.1354166666666665in"}

-   Click on the **delete** ![](media/image319.png){width="0.3541666666666667in" height="0.3333333333333333in"} icon for both the menu items Hep E Outbreak (Jan-Nov 2020) and Cholera Outbreak (Aug 19 -- March 21).

-   Click on **Save Change(s)** -- the changes are saved, and the header page configuration screen opens, as shown below:

![](media/image755.png){width="5.79166447944007in" height="3.15625in"}

**Step 2.** Delete the associated pages for the hepatitis E and cholera outbreaks.

-   On the header page configuration screen, look for the page navigation drop-down menu at the top left-hand corner \> select the **Page Name** Hep E Outbreak (Jan-Nov 2020) \> scroll down to the bottom of the screen:

![](media/image756.png){width="2.75in" height="3.3333333333333335in"}

-   Click on ![](media/image757.png){width="1.125in" height="0.3333333333333333in"}, and the page is deleted.

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image211.png){width="0.41060695538057745in" height="0.3875in"}**WARNING:**   This action is irreversible as a page cannot be recovered once deleted.
  --------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-   Similarly, delete the Cholera Outbreak (Aug 19 -- March 21) page.

**Step 3.** Add a malaria outbreak page.

-   Select **Menu** \> **Website Builder**. Click on the **edit** ![](media/image307.png){width="0.3541666666666667in" height="0.3333333333333333in"} icon, and the website editor opens.

-   Click on ![](media/image758.png){width="1.0208333333333333in" height="0.2916666666666667in"}, and a new page and its properties are visible. Enter a **Page Name** \[Mandatory\] (e.g. "Malaria Outbreak (Ongoing)").

**Step 4.** Add a menu item for a malaria outbreak in the outbreaks menu and link it to the newly created malaria outbreak page.

-   Select **Header Page** from the page drop-down menu at the top left-hand corner \> click on the second row with the label **Menu**, and the menu editor opens.

-   Click on the **expand** ![](media/image753.png){width="0.25in" height="0.3333333333333333in"} icon in the **Outbreaks** menu, and the menu expands.

-   Click on ![](media/image759.png){width="1.3333333333333333in" height="0.3333333333333333in"} to add a new menu item row, and a new row is added, as shown below:

![](media/image760.png){width="6.208333333333333in" height="3.8020833333333335in"}

-   Click on the **edit** ![](media/image307.png){width="0.3541666666666667in" height="0.3333333333333333in"} icon \> enter the **Menu Item Name** (e.g. "Malaria Outbreak (Ongoing)") and a new menu item is added. Select the **Page Malaria Outbreak (Ongoing)**, and the page is linked.

-   Click on **Save Change(s)**.

-   Click on ![](media/image718.png){width="0.9583333333333334in" height="0.3125in"}, and the website opens in a new tab. Go to the **Outbreaks** menu**,** click on the menu item **Malaria Outbreak**, and the Malaria Outbreak page and its contents are visible.

## 22.4 Creating a new website

Instead of modifying the sample website, you may want to create a completely new website. To do so, follow the steps below.

-   Select **Menu** \> **Website Builder**. Click on **Create New**, and the screen below appears:

![](media/image761.png){width="5.3125in" height="2.8333333333333335in"}

-   Populate the fields, as shown below.

```{=html}
<!-- -->
```
-   **Website Name** \[Mandatory\]: enter the website name (e.g. "Ministry of Health Nambutu").

-   **Status** \[Mandatory\]: select the relevant option (**Published/Unpublished**) according to your requirements. For additional information, refer to the explanation of status fields in topic **22.3.1 Modifying the site** **settings**.

-   **Domain** \[Mandatory\]: enter the **Domain** of the website. For additional information, refer to the explanation of domain fields in topic￼**22.3.1 Modifying the site** ￼.

-   **Description:** enter a description of the website.

-   **Tags**: enter a tag for the bulletin template. A tag is an identifier that will help you to find your template in the configuration transfer menu. You can add **one or more** tags or leave the tag blank.

-   **Upload CSS or JS File:** upload a CSS or JS file to be applied to the header page. If you have no prior knowledge of CSS or JS, there is no need to upload a file: failing to do so will not affect the existing style of the website. If you need further information or support, please contact the EWARS Super Administrator.

```{=html}
<!-- -->
```
-   Click on **Save Change(s)**.

## 22.5 Configuring a newly created website

  ---------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------
  ![](media/image43.png){width="0.65625in" height="0.3541666666666667in"}   Please contact the EWARS Super Administrator if you need support in configuring a website for EWARS

  ---------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------

-   Select **Menu** \> **Website Builder**. Click on the **edit** ![](media/image687.png){width="0.3541666666666667in" height="0.3333333333333333in"} icon, and the website editor screen below appears:

![](media/image762.png){width="5.83333552055993in" height="2.8125in"}

The screen is divided into four parts.

**Part 1: the top toolbar actions**, including:

-   **Page navigation drop-down menu**, which allows you to switch between pages -- by default, header and footer pages are available inside menu

-   **Add Page**, **Site Settings**, **CSS Settings** and **Preview** -- these are described in topics **22.5.2 Adding a new page**, **22.5.6 Editing the site** **settings**, **22.5.7 Applying CSS settings** and **22.5.4 Previewing the website**.

**Part 2: the page settings**, including:

-   **Page Name** \[Mandatory\]: this should be a short **name** for the page (e.g. "Home", "About" or "Contact Us")

-   **Page Class:** this is an optional field -- you can enter a CSS class to apply extra styling to the page; you can also add multiple class names separated by a comma. You can provide any name for the CSS class, and the relevant code for the class needs to be provided in the Editor tab under CSS settings. A few in-built classes are available for use under the Help tab. It is not mandatory to use a CSS class if you have no prior knowledge of these. If you need further information or support, please contact the EWARS Super Administrator.

-   **Description**: this is an optional field -- you can enter text describing the page.

**Part 3: the widgets section,** containing widgets that are the building blocks of the page and can be dragged and dropped on to a webpage to populate it, including:

-   **Container** widgets (**Row** widgets and **Cell** widgets): these are required to build a page, and they can contain non-container widgets.

-   **Non-container widgets**: these are of two types:

    **Static** widgets are text, image, video, HTML, menu, and carousel widgets -- these are not linked to EWARS data in the system, and do not use or display data you have collected in EWARS

    **Dynamic** widgets are chart components, mapping, other and user group components -- these are tied to EWARS data.

For more information on container and non-container widgets, refer to **Chapter 17. Widgets and their configuration**.

**Part 4: the page designing area**, which is the central space where the container and non-container widgets are dragged and placed to design a page.

### 22.5.1 Setting up the header and footer

The header and footer are special purpose pages. These can be designed in the same way as any other page, but these sections are visible at the top and bottom of all pages of the website. To design the header and footer pages, refer to topic **22.5.3 Designing a page**.

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** unlike other pages on the website, you cannot delete the header page and footer page.
  --------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### 22.5.2 Adding a new page

-   Select **Menu** \> **Website Builder**. Click on the **edit** ![Inserting image\...](media/image307.png){width="0.3541666666666667in" height="0.3541666666666667in"} icon, and the website editor screen opens. Click on ![](media/image758.png){width="1.0208333333333333in" height="0.2916666666666667in"} \> enter the **Page** **Name** \[Mandatory\] \> enter the **Page** **Class** \> enter the **Description** \> click on **Save Change(s)**, and the page is created.

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** you can add several pages to your website. These appear in the page navigation drop-down menu and can be modified.
  --------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### 22.5.3 Designing a page

-   Select **Menu** \> **Website Builder**. Click on the **edit** ![Inserting image\...](media/image307.png){width="0.3541666666666667in" height="0.3541666666666667in"} icon of a website, and the website editor screen opens.

-   Drag and drop a **Row** widget from Part 3 to Part 4 in the screenshot above.

-   Drag and drop a **Cell** widget onto the row to divide a row into multiple cells. If more cells are added, the size will become smaller. Each cell represents a section you can add to the page.

-   Once the desired page structure is achieved, drag the relevant static or dynamic widget onto each of the cells.

-   Configure all the widgets placed in the cells. Refer to **Chapter 17. Widgets and their configuration** for detailed explanations of each type of widget before adding appropriate widgets to the webpage.

-   Right-click on the row or cell to view more options, as shown below:

![](media/image763.png){width="5.6875in" height="2.7083333333333335in"}

You can move the rows and cells, duplicate them or remove them as you configure the page. For more information, refer to **Chapter 17. Widgets and their configuration**, topic **17.3 Row and cell widgets**.

### 22.5.4 Previewing the website

Previewing allows users to browse the site and check how it will appear to the public before it is published. You can preview the website that is being configured, irrespective of its published or unpublished status.

-   Select **Menu** \> **Website Builder**. Click on the **edit** ![](media/image307.png){width="0.3541666666666667in" height="0.3333333333333333in"} icon of a website, and the website editor screen opens.

-   Click on ![](media/image764.png){width="0.9375in" height="0.2916666666666667in"} to preview the website in a new tab.

### 22.5.5 Deleting a page

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image211.png){width="0.41060695538057745in" height="0.3875in"}**WARNING:**   This action is irreversible as a page cannot be recovered once deleted.
  --------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-   Select **Menu** \> **Website Builder**. Click on the **edit** ![](media/image307.png){width="0.3541666666666667in" height="0.3333333333333333in"} icon, and the website editor screen opens. In the page navigation drop-down menu, select the page to be deleted. Scroll down \> click on ![](media/image757.png){width="1.125in" height="0.3333333333333333in"}, and the page is deleted.

### 22.5.6 Editing the site settings

Site settings allow you to edit already completed fields such as the website name, status, domain, description or tag, and to upload CSS or JS files.

-   Select **Menu** \> **Website Builder**. Click on the **edit** ![](media/image307.png){width="0.3541666666666667in" height="0.3333333333333333in"} icon, and the website editor screen opens. Click on ![](media/image765.png){width="1.2916666666666667in" height="0.3125in"} \> make the required changes (e.g. changing the description or website name). Click on **Save Change(s)**.

### 22.5.7 Applying CSS settings

CSS settings help to change the style and presentation of the webpage, such as the page layout, colours, fonts and so on. In EWARS, CSS settings help you to customize the style of your website by overriding the existing styles.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** CSS or JS are powerful ways to apply styling to a website, although these require technical knowledge of HTML, CSS and/or JS. It is not mandatory to modify the CSS settings, especially if you have no prior knowledge of CSS or JS. If no modification is made, the default EWARS styling will be applied to the settings. For technical support on CSS or JS files, please contact the EWARS Super Administrator.
  --------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To apply CSS settings, follow the steps below.

-   Select **Menu** \> **Website Builder**. Click on the **edit** ![](media/image307.png){width="0.3541666666666667in" height="0.3333333333333333in"} icon of a website, and the website editor screen opens. Click on ![](media/image766.png){width="1.2083333333333333in" height="0.3125in"}, and the **CSS Editor** popup window below appears:

![](media/image767.png){width="2.9166666666666665in" height="2.3333333333333335in"}

-   Click on the **Help** tab, and a list of CSS classes appears, as shown below:

> ![](media/image768.png){width="5.54916447944007in" height="3.619792213473316in"}

-   Copy any of these CSS classes (e.g. menu-bar-class) \> click on the **Editor** tab \> paste the CSS class into the editor screen and write the relevant code.

-   Click on **Save Change(s)** -- the CSS Settings are saved, and the popup window closes.

For example, you can change the menu bar background colour using CSS settings, as set out below.

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** it is recommended that you do not change the background colour of the menu, but if you want to build an outbreak website, then you can go for it.
  --------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](media/image769.png){width="5.70833552055993in" height="1.0in"}

-   Write the following CSS code in the **Editor** tab:

".menu-bar-class

{

background-color: #2a7da1;

}"

-   Click on **Save Change(s)** -- the CSS settings are saved, and the popup window closes.

-   Click on **Preview** to view the applied changes, as shown below:

![](media/image770.png){width="5.29166447944007in" height="1.0473097112860892in"}

## 22.6 Duplicating a website

You can duplicate an existing website and modify it according to your requirements.

-   Select **Menu** \> **Website Builder**. Click on the **duplicate** ![](media/image771.png){width="0.3125in" height="0.2916666666666667in"} icon of the website (e.g. Demo Website (web1.ewars.ws)). Click on **Confirm**, and a duplicate website named "Demo Website (web1.ewars.ws)\_copy" is added.

## 22.7 Deleting a website

You can delete an existing website when it is not in use.

-   Select **Menu** \> **Website Builder**. Click on the **delete** ![](media/image319.png){width="0.3541666666666667in" height="0.3333333333333333in"} icon of the website (e.g. Demo Website (web1.ewars.ws)). Click **Confirm**, and the website is deleted.

> The following chapter explores the Export feature, which facilitates the export of system data in different formats, according to your requirements.

# Chapter 23. Export

The Export feature facilitates the export of data from the Early Warning, Alert and Response System (EWARS) in different formats, including .zip, .csv, .doc and .pdf. Data related to the forms -- such as reporting forms, alerts, user data, indicator data and locations data -- can be exported with ease. If multiple individual reports are submitted, they can be downloaded as a single merged PDF file for easier perusal. Through this method, the data collected can be easily shared for multifaceted in-depth analysis, aiding both research and monitoring/tracking.

Table 23.1 summarizes data that can be exported and the supported formats.

Table 23.1. Data that can be exported and supported formats

  -------------------------------------------------------------------------------------------------------
  **Exporting data format**                                                            
  --------------------------- ------------------ ------------------ ------------------ ------------------
  **Data type**               **Format: .zip**   **Format: .csv**   **Format: .doc**   **Format: .pdf**

  Form Submissions            **✓**                                 **✓**              **✓**

  Indicators                                     **✓**                                 

  Alerts                      **✓**                                                    

  Locations                                      **✓**                                 

  Users                                          **✓**                                 
  -------------------------------------------------------------------------------------------------------

## 23.1 Exporting form submissions

Form submissions can be filtered and selected for export, based on the form, location and date. The exported file formats can be .zip, .pdf or .doc.

### 23.1.1 Exporting as a .zip file

-   Select **Menu** \> **Export** \> click on the **Form Submissions** tab. Populate the **Start date**, **End date**, **Location** and **Form** fields. Click on ![](media/image772.png){width="0.7361111111111112in" height="0.25in"}, and a .zip file is downloaded and can be viewed in Excel, as shown below after it is extracted:

    ![Graphical user interface, application, table, Excel Description automatically generated](media/image773.png){width="6.5in" height="1.8611111111111112in"}

### 23.1.2 Exporting as a .pdf file

By selecting the PDF option, you can export all individual reports submitted within the specified start date, end date and location as a .pdf file. For example, if there are 200 submitted reports meeting your criteria, they are downloaded as a merged PDF.

-   Select **Menu** \> **Export** \> click on the **Form Submissions** tab. Populate the **Start date**, **End date**, **Location** and **Form** fields. Click on ![](media/image774.png){width="0.6354166666666666in" height="0.25in"}, and a .pdf file is downloaded and can be viewed independently. A sample view is given below:

![](media/image775.png){width="5.927083333333333in" height="2.8153652668416447in"}

### 23.1.3 Exporting as a .doc file

By selecting the .doc option, you can export all individual reports submitted within the specified start date, end date, and location as a Microsoft Word file.

-   Select **Menu** \> **Export** \> click on the **Form Submissions** tab. Populate the **Start date**, **End date**, **Location** and **Form** fields. Click on ![](media/image776.png){width="0.5416666666666666in" height="0.25in"}, and a .doc file is downloaded and can be viewed independently. A sample view is given below:

![](media/image777.png){width="5.400614610673665in" height="3.4316404199475063in"}

## 23.2 Exporting indicator data

You can export indicator data as a comma-separated values (CSV) file. This feature facilitates exporting multiple indicators data for multiple locations in a single CSV file.

-   Select **Menu** \> **Export**. Click on the **Indicator Data** tab, and the screen below appears:

![](media/image778.png){width="5.973615485564305in" height="3.5611931321084866in"}

In the screenshot above, the **Locations** tab is highlighted as 1, the **Indicators** tab as 2 and the **Export Options** fields as 3.

To export the data as a CSV file, follow the steps below.

-   Select the required locations from the **Locations** tab (1), select the required indicators from the **Indicators** tab (2) and populate the **Export** **Options** fields as follows.

```{=html}
<!-- -->
```
-   Set **Aggregation Interval** as day, week, month or year, as appropriate. This will aggregate and download the data according to the selected interval.

-   Set **Target Location Selection** as **Children of type**. This enables you to select locations according to location type -- for example, to select all provinces of a country, you can select **Country** from the **Locations** tab (1) and select **Provinces** as the **Location type**.

-   Select the **Start date** and **End date** in the calendar to specify the date range for the data to be exported.

```{=html}
<!-- -->
```
-   **Aggregation interval:** Choose among day, week, month or year, as appropriate. It will aggregate and download the data as per the selected aggregation interval.

-   **Transpose options**: Set as on or off

-   Click on ![](media/image779.png){width="0.6654024496937883in" height="0.23484798775153107in"} to start export and the screen below appears:

    ![Graphical user interface, application, table Description automatically generated](media/image780.png){width="6.25in" height="1.5972222222222223in"}

The example CSV file column headings are **location, place code (PCODE)**, **path**, **Indicator 1**, **Indicator 2**, **Indicator 3** and so on.

The CSV file has a data row for each selected location. For example, if you selected three locations, the CSV file has three data rows.

-   **Or** click on the **Transpose** toggle icon to set as off, meaning that indicator data are summed up for each aggregation interval -- for example, aggregated data are presented for the state for the entire selected period.

-   Click on ![](media/image779.png){width="0.6654024496937883in" height="0.23484798775153107in"} to start export and the screen below appears:

![](media/image781.png){width="6.111111111111111in" height="2.875in"}

The example CSV column headings are **location, PCODE**, **path**, **Indicator**, **Interval 1, Interval 2**, **Interval 3** and so on.

The CSV file has a data row for each combination of the selected locations and indicators. For example, if you selected three locations and two indicators, the CSV file has six (3 x 2) data rows.

## 23.3 Exporting alerts data

Alerts data can be exported as a .zip file. You can export alerts data by selecting alarm, location and date period, and enabling/disabling report data.

-   ![](media/image782.png){width="6.898149606299213in" height="3.1041666666666665in"}Select **Menu** \> **Export**. Click on the **Alerts** tab, and the screen below appears:

-   Populate the **Start date**, **End date**, **Location** and **Alarm** fields.

At this point, you have two options to set the information you want to export.

-   **Either** set **Include report data** as **No**, and the exported CSV file does not include the reports that triggered the alert.

-   Click on ![](media/image779.png){width="0.6654024496937883in" height="0.23484798775153107in"}, and a .zip file is downloaded \> extract it.

The extracted .zip file folder has a file named **Alerts.csv**. This includes full information on each alert, along with alert actions and events specified by time duration and location; these can be located by alert electronic identification (EID).

Some of the columns of Alerts.csv file are shown below:

![](media/image783.png){width="6.791666666666667in" height="1.5564238845144356in"}

-   **Or** set **Include report data** as **Yes**, and the exported CSV file includes the reports that triggered the alert.

-   Click on ![](media/image779.png){width="0.6654024496937883in" height="0.23484798775153107in"}, and a .zip file is downloaded \> extract it.

The extracted .zip file folder has a CSV file that includes all the columns, as shown in the screenshot above, and all the reports and their data, which triggered this alert.

The screenshot below shows some of the columns contained in the files and their data, along with the alert data:

![](media/image784.png){width="5.875in" height="2.5729166666666665in"}

## 23.4 Exporting locations data

The locations in the system can be exported as a CSV file.

-   Select **Menu** \> **Export**. Click on the **Locations** tab.

-   Populate the **Location**, **Location type** and **Location status** fields. Click on ![](media/image779.png){width="0.6654024496937883in" height="0.23484798775153107in"}, and a CSV file is downloaded.

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** location type is optional. Select the type of location to export the related data. All child locations under the selected location are exported in the event of no selection under the location type.
  --------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The extracted CSV file has the following location data columns, including the universally unique identifier (UUID) generated by the system:

  -----------------------------------------------------------------------------------------
  UUID            name        PCODE           parent_id       lineage           Status
  --------------- ----------- --------------- --------------- ----------------- -----------
  geometry_type   groups      location_type   Uncategorized   Health Facility   Province

  Country                                                                       
  -----------------------------------------------------------------------------------------

## 23.5 Exporting user data

User data can be exported as a CSV file, based on users' creation date, status and role.

-   Select **Menu** \> **Export**. Click on the **Users** tab.

-   Populate the user **Start** date, **End date**, **Status** and **Role** fields. Click on ![](media/image779.png){width="0.6654024496937883in" height="0.23484798775153107in"}, and a CSV file is downloaded.

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** user status and role are optional. Select the relevant status (active or inactive user) and role (Reporting User, Geographical Administrator or Account Administrator) to export the related data. All users created in the date range are exported in the event of no selection of any particular user status and role.
  --------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The extracted CSV file has the following user data columns:

![](media/image785.png){width="6.342315179352581in" height="2.206597769028871in"}

The following chapter explores the Short Message Service (SMS) reporting and teams features. These allow you to send reports via the SMS function in environments where data connectivity is weak.

# Chapter 24. SMS reporting and teams

Short Message Service (SMS) reporting is a novel feature that allows Early Warning, Alert and Response System (EWARS) Reporting Users to send reports via the SMS function. This is useful if a 3G or 4G data connection is not available, and reports cannot be sent using the more typical data function of the mobile phone. This does not mean that Reporting Users have to type an SMS, as the name might seem to imply. Rather, EWARS automatically converts a regular report into an SMS for transmission. EWARS Web receives the report just like any other report sent via a data connection (Fig. 24.1).

Fig. 24.1. Overview of the SMS reporting workflow

![](media/image786.png){width="5.954870953630796in" height="4.18081583552056in"}

SMS reporting can be enabled for an entire country or a particular group of users, depending on the context and requirements. Enabling SMS reporting for a particular group of users is achieved using the teams feature. SMS reporting functions as an intermediary medium, facilitating reporting between EWARS Mobile and WHO EWARS. EWARS facilitates the creation of teams, and enables users to be added to them. A team is defined as a set of users that can be grouped based on a common goal and activity.

  ---------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![](media/image43.png){width="0.65625in" height="0.3541666666666667in"}   The teams feature is primarily used here for SMS reporting. For contexts where the data connection is too weak for regular mobile reporting, however, the teams feature is also used for other purposes.

  ---------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In environments such as remote areas, conflict-affected areas or areas with poor infrastructure support, the reporting users collect all the reporting data and submit reports via SMS, relayed via the SMS Gateway application (app) (Fig. 24.2).

Fig. 24.2. EWARS reporting using the SMS Gateway app

![Graphical user interface Description automatically generated with low confidence](media/image12.png){width="6.5in" height="1.1666666666666667in"}

For more information, refer to **Chapter 1. Overview of EWARS in a box**, topic **1.2 EWARS components and their deployment in various scenarios**.

## 24.1 Setting up SMS reporting

SMS reporting can be enabled for an entire country or a particular group of users (a team).

If SMS reporting is enabled for the **entire country**, you only need to set up a single SMS Gateway account, and all the SMS messages are relayed using that account. If SMS reporting is enabled for **specific teams**, you need to set up multiple SMS Gateway accounts: one per team. Multiple gateways are needed[, for instance, when high volumes are expected, and multiple phone numbers need to be used for receipt to spread the load.]{.mark}

Each of these scenarios is addressed below.

### 24.1.1 Setting up SMS reporting for the entire country

The process of setting up SMS reporting for the entire country can be best understood via the flowchart below (Fig. 24.3).

![](media/image787.png){width="3.8055555555555554in" height="6.048565179352581in"}Fig. 24.3. SMS reporting flowchart

As shown above, Country X wants to enable SMS reporting. For this, it needs an SMS Gateway account, which is, in practice, a mobile phone dedicated to performing this function. The SMS Gateway app is installed on that phone; it is placed in a safe location with good signal and kept plugged in so that it will not run out of charge or go to sleep. The phone's job is effectively to relay messages to WHO EWARS. All Reporting Users can submit reports via SMS.

### 24.1.2 Setting up SMS reporting for a team

The process of setting up SMS reporting for a team can be best understood via the flowchart below (Fig. 24.4).

Fig. 24.4. SMS reporting for a team flowchart

![](media/image788.png){width="3.8577252843394576in" height="7.683437226596675in"}

As shown above, you need to identify the team that needs SMS reporting enabled for an area with an unreliable internet connection. Assign an SMS Gateway number to a mobile phone with the SMS Gateway app installed for the team. The team can then submit reports via SMS.

  ---------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------
  ![](media/image43.png){width="0.65625in" height="0.3541666666666667in"}   If you have different mobile service providers in different areas, you may need different SMS Gateway accounts, depending on the provider.

  ---------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------

## 24.2 Setting up the SMS Gateway app

For EWARS to receive reports via SMS, an SMS Gateway account should be created. This is a dedicated Android phone with the EWARS SMS Gateway app activated. The phone must be placed in an environment with internet or Wi-Fi at all times. Ideally, it needs to be set up at the central surveillance office that receives reports. The SMS Gateway phone needs an activated SIM card from a telecommunication provider that has coverage in the area of concern, such as Vodafone, Digicel or Airtel. The phone, once activated, needs to be kept on charge at all times. If all these requirements are met, it will act as an SMS Gateway account to relay reports.

In summary, the SMS Gateway account is a mobile phone that is always on, to which SMS messages can be sent by EWARS users.

The SMS Gateway app receives reports submitted by Reporting Users via SMS and sends them to WHO EWARS over the internet connection.

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** you can have multiple SMS Gateway accounts to receive reports via different telecommunication providers. However, most emergency settings are covered by a limited number of providers, so you may be able to manage with just one or two SMS Gateway accounts.
  --------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To set up an SMS Gateway account, follow the steps below.

**Step 1** \[Mandatory\].

-   Assign an Android phone with operating system version 6.0 Marshmallow or higher to be the SMS Gateway phone.

-   Procure and insert a SIM card from an appropriate telecommunication provider (e.g. Digicel).

-   The phone must have an active internet data connection and an active SMS plan to receive SMSs. This phone should only be used as an SMS Gateway phone. No reporting should be performed using this phone.

-   The phone should be plugged into a power source to be charging at all times.

  ---------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![](media/image43.png){width="0.65625in" height="0.3541666666666667in"}   Choose the best mobile plan by considering factors like internet usage, SMS plans and network coverage. It is recommended to have 3G or 4G network coverage.

  ---------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------

**Step 2.** Download the SMS Gateway app on the mobile phone, using one of the following options.

-   **Either** open the following link in the mobile browser, and the app is downloaded: [[https://ewars.ws/static/apps/ewars-sms.apk]{.underline}](https://ewars.ws/static/apps/ewars-sms.apk)

-   **Or** download the SMS Gateway Android application package (APK), which is available in **EWARS Web**. To download it, go to **EWARS Web** \> select **Menu** \> **Downloads**, and the following screen appears:

![](media/image789.png){width="6.291666666666667in" height="2.1458333333333335in"}

-   Click on ewars.sms.apk and the APK is downloaded onto your laptop/desktop. Copy it to the **Downloads** folder of your mobile phone, as shown below:

> ![](media/image790.png){width="3.0108366141732286in" height="4.083903105861768in"}

**Step 3.** Allow installation of the app from an unknown source.

-   Navigate to your phone's **Settings** menu and then to **Security & Privacy** settings. Tap on **Install unknown apps**. Enable the toggle button for **Allow from this source**, as shown below:

![](media/image791.png){width="3.1875in" height="4.697916666666667in"}

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** the option to allow installation of an app from an unknown source may appear differently on your mobile phone, based on the operating system version and the model. Enable the relevant option, based on how and where it appears on your mobile phone.
  --------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Step 4.** Install the SMS Gateway app.

-   Tap the **file manager** ![](media/image792.png){width="0.2833333333333333in" height="0.2833333333333333in"} icon \> navigate to your **Downloads** folder \> tap the **SMS Gateway APK** file \> tap to **install** and follow the on-screen instructions. The app is installed and is available on the home screen, as shown below:

![](media/image793.png){width="2.3125in" height="5.0in"}

**Step 5.** Obtain credentials for logging in to the SMS Gateway app.

The SMS Gateway app is password protected, so you need to obtain credentials to allow you to log in to it.

-   Go to **EWARS Web**.

-   Select **Menu** \> **Administration** \> **Third Party Clients**, and the following screen appears:

![](media/image794.png){width="6.40833552055993in" height="1.8333333333333333in"}

-   Click on ![](media/image795.png){width="0.9166666666666666in" height="0.3in"}, and the following screen appears:

![](media/image796.png){width="6.135416666666667in" height="3.033112423447069in"}

-   Enter the **Name (**e.g. "Province A").

-   Enter your preferred **Username** for the SMS Gateway app (e.g. "province_a").

-   Enter a **Password** (minimum 8 characters and maximum 15 characters) (e.g. "Mcv63edx") \> **re-enter** the password for confirmation.

-   Keep **Status** as **Active**.

-   Set **API Types** as **SMS GATEWAY**.

-   Click on **Save Change(s)**.

The third-party client is created with the credentials provided, and the credentials are ready to use in the SMS Gateway app.

**Step 6.** Log in to the SMS Gateway app.

-   Start the SMS Gateway app by tapping the **SMS** ![](media/image797.png){width="0.36666666666666664in" height="0.3333333333333333in"} icon on your mobile phone.

-   When prompted, **allow access** to send and view SMSs.

-   When prompted, tap on **Set as Default** to set the SMS Gateway app as your default SMS app.

-   The app opens, and the login screen appears, as shown below:

![](media/image798.png){width="3.07250656167979in" height="4.239583333333333in"}

-   Enter your **USERNAME** and **PASSWORD** \> enter "tp-client-global" as the **CLIENT** \> enter [[https://ewars.ws](https://ewars.ws/) as]{.underline} the **Global URL**.

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** the client and global universal resource locator (URL) entered are standard for every SMS Gateway account.
  --------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-   Tap on **LOGIN**, and the following screen appears:

![](media/image799.png){width="3.3125in" height="4.34375in"}

You have now created an SMS Gateway account successfully under a mobile number. The following topics illustrate how to enable SMS reporting for an entire country or a team.

## 24.3 Enabling SMS reporting for an entire country

If SMS reporting is enabled for the entire country, you need only one SMS Gateway account that can be used by all users, and only one SMS Gateway number. When any Reporting User reports via SMS, that report will automatically go through the dedicated SMS Gateway number. This SMS Gateway number needs to be added to the account settings in EWARS Web, as set out below.

**Step 1.** Set up the SMS Gateway app for the entire country as explained in topic **24.1.1**.

**Step 2*. ***Add the SMS Gateway number in account settings, as shown below:

-   Click on the **settings** ![](media/image214.png){width="0.25in" height="0.275in"} icon at the top right-hand corner \> click on ![](media/image800.png){width="0.7916666666666666in" height="0.3333333333333333in"}, and the screen below appears:

![](media/image801.png){width="5.99166447944007in" height="3.2333333333333334in"}

-   Enter the mobile number of the **SMS Gateway** in the **SMS Phone Number** field \> click on **Save Change(s)**.

SMS reporting is now enabled, and any Reporting User in the country can switch to SMS reporting using the SMS Gateway number when data connectivity is poor.

## 24.4 Enabling SMS reporting for a team

The teams feature should be used if SMS reporting is required for a particular group of users. A team needs a dedicated SMS Gateway number. Therefore, you need to create a team, add Reporting Users who require SMS reporting and add the SMS Gateway number in the team configuration.

If there are multiple areas with poor internet connection that are covered by multiple telecommunication partners in your context, EWARS allows you to create multiple teams to fulfil the reporting needs (e.g. Province A reporting team with Airtel SMS, Province B reporting team with Vodacom SMS, and so on).

Follow the steps below to enable SMS reporting for Province A reporting team.

**Step 1.** Set up the SMS Gateway app for Province A reporting team.

**Step 2*. ***Create Province A reporting team.

-   Select **Menu** \> **Administration** \> **Teams Management**. Click on ![](media/image802.png){width="0.625in" height="0.3in"}, and the screen below appears:

![](media/image803.png){width="6.414846894138233in" height="2.6930686789151355in"}

-   Enter a unique **Name** for the team (e.g. "Province A reporting team").

-   Enter the **SMS Phone Number** (e.g. "+254 567 1435"). This is the phone number of the device on which the SMS Gateway app is running.

-   Enter a **Description for** the team.

-   Keep the **Status** set as **Active**.

**Step 3.** Add members to the team

-   Click on the **Team Members** tab at the left-hand side, and the screen below appears:

![](media/image804.png){width="6.189247594050744in" height="2.0021194225721786in"}

The **Select Member** drop-down menu contains all users under your account. Select the users who need the SMS reporting feature to form a team.

-   Select each Reporting User to be added as a team member from the **Select Member** drop-down menu.

-   Click on ![](media/image805.png){width="0.5083333333333333in" height="0.25833333333333336in"} \> click on **Save Change(s)**, and the team is created with the members.

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** if there are two different SMS phone numbers, wherein one is set up in the team configuration and another set up for the entire country, the number in the team configuration is used in preference for reporting. For example, a common Digicel number +111 234 5678 is set up for the whole country (under account settings), and Province A reporting team Digicel number +111 321 4567 is set up under the team configuration. When Province A reporting members submit reports via SMS, the former Digicel number +111 321 4567 is used.
  --------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ---------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![](media/image43.png){width="0.65625in" height="0.3541666666666667in"}   There is no requirement to key in the SMS Gateway number from the Reporting Users' phones. The selected SMS Gateway and its number are already configured when you create the team. The system will automatically know which SMS Gateway number to use for report submission.

  ---------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 24.5 Adding members to an existing team

Follow the steps below to add members to an existing team.

-   Select **Menu** \> **Administration** \> **Teams Management**, and a screen listing all existing teams (if any) appears, as shown below:

![](media/image806.png){width="6.363377077865267in" height="1.8233694225721784in"}

-   Click on the **edit** ![](media/image807.png){width="0.2833333333333333in" height="0.275in"} icon of the desired team (e.g. Province A reporting team) \> click on the **Team Members** tab at the left-hand side, and the screen below appears:

![](media/image808.png){width="6.33423665791776in" height="2.2448261154855644in"}

-   Select a user to be added as a team member from the **Select Member** drop-down menu.

-   Click on ![](media/image809.png){width="0.65in" height="0.31666666666666665in"} \> click on **Save Change(s)**, and the team member is added.

## 24.6 Removing a member from a team

To remove a members from a team, follow the steps below.

-   Select **Menu** \> **Administration** \> **Teams Management**. Click on the **edit** ![](media/image807.png){width="0.2833333333333333in" height="0.275in"} icon of the desired team (e.g. Province A reporting team). Click on the **Team Members** tab at the left-hand side \> click on the **delete** ![](media/image681.png){width="0.275in" height="0.2833333333333333in"} icon.

-   Click on **Save Change(s)**, and the team member is removed.

## 24.7 Deleting a team

-   Select **Menu** \> **Administration** \> **Teams Management** \> click on the **delete** ![](media/image681.png){width="0.275in" height="0.2833333333333333in"} icon. Click on **Confirm**, and a notification appears that the team is deleted.

## 24.8 SMS Gateway monitoring

The SMS Gateway app receives EWARS reports submitted via SMS and sends them to WHO EWARS over an internet connection as regular online reports.

The app monitors the number of reports **received** from Reporting Users and the number of reports **submitted** to the WHO EWARS server, as shown below:

> ![](media/image810.png){width="3.3125in" height="4.302083333333333in"}

The SMS Gateway app also show the number of **pending** reports. These are SMSs that have been received but have not yet been submitted to the WHO EWARS server. The number of reports held at the pending stage depends on the internet connection. The app will automatically process and send the SMSs to the WHO EWARS server when the data connection is available. The SMSs will remain pending until an internet connection is available.

After a specific interval, there is a need to clear the queued SMSs to optimize phone storage.

The total number of the SMSs received by the SMS Gateway app is calculated as follows:\
\
Total received SMSs = pending SMSs + submitted SMSs

All the other SMSs -- such as those from the telecom service provider and regular notifications -- remain pending and should all be deleted.

You can tap on any SMSs listed as pending, submitted or received to view the details.

-   Tap on **Submitted** and report details including **Status**, **Received From**, **Received Date**, **Submitted Date** and other **Data** appear, as shown below:

![](media/image811.png){width="3.316666666666667in" height="4.75in"}

-   To delete the reports, tap the **delete** ![](media/image812.png){width="0.275in" height="0.25in"} icon at the top left-hand corner, and a confirmation box appears. Tap **Yes**. Deleting SMSs listed under **Submitted** deletes all SMSs that have been submitted.

You can also delete SMSs listed as received or pending, depending on your requirements. Those SMSs that are redundant or that have been received from other SMS providers or other sources and are not relevant to WHO EWARS can be deleted.

[The following chapter explores the EWARS Stand-alone app, which helps you perform mobile reporting in difficult environments.]{.mark}

# Chapter 25. EWARS Stand-alone

The Early Warning, Alert and Response System (EWARS) Stand-alone application (app) facilitates mobile reporting in environments that are offline or lack access to reliable internet connections. It is set up on a dedicated laptop or desktop (with Windows operating system), ideally situated at a central surveillance office of the concerned area. The app helps capture the data from EWARS Mobile users in such environments and then synchronizes (syncs) it with WHO EWARS. In such instances, EWARS Stand-alone acts as the **receiver** and EWARS Mobile acts as a **sender**. EWARS Stand-alone is similar to EWARS Web in terms of the interface, but it is equipped with additional data collection and synchronization features. Through this, field data can be collected and reported seamlessly in difficult environments, facilitating uninterrupted analysis and monitoring/tracking.

EWARS Stand-alone functions as an intermediary medium, facilitating reporting between EWARS Mobile and WHO EWARS in environments that are offline or that lack access to reliable internet connections. Fig. 25.1 illustrates the process of data capture and submission to WHO EWARS via EWARS Stand-alone in such environments . Refer to **Chapter 1. Overview of EWARS in a box** for more scenarios.

Fig. 25.1. Data capture and submission using EWARS Stand-alone

![](media/image813.png){width="5.5625in" height="4.473178040244969in"}

EWARS Stand-alone allows Geographical Administrators and Account Administrators to work while they are not connected to the internet.

  ---------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![](media/image43.png){width="0.65625in" height="0.3541666666666667in"}   This app will not replace the interactive environment that normal EWARS provides. This chapter is written assuming you have an EWARS Country account that runs using reliable internet in other parts of the country. EWARS Stand-alone is used only in localized and remote areas with unreliable internet connectivity.

  ---------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The topics below set out how to set up EWARS Stand-alone. After the initial setup, it is mandatory to sync your account with WHO EWARS. During the synchronization, your account data and configurations are copied to the EWARS Stand-alone app storage, facilitating use of the app while you are offline.

## 25.1 Setting up EWARS Stand-alone

The setup process involves procuring a laptop or desktop, downloading the app and installing it on the machine.

**Step 1.** You need a dedicated laptop or desktop to run the EWARS Stand-alone app. Ideally, this should be a machine at a central surveillance office in the area where you want to set up the EWARS Stand-alone operation.

Minimum hardware requirements to set up EWARS Stand-alone are:

-   a processor operating at 2.0 GHz or more

-   8 GB or more RAM

-   40 GB or more available hard disk space

-   a Windows 8 32-bit/64-bit or more operating system

-   3G/4G network coverage (the app can work in 2G but 3G/4G is recommended for smooth running).

**Step 2.** Download the EWARS Stand-alone app onto your computer.

![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}**Note:** the following initial steps of installation need to be completed in an environment with an internet connection.

-   Type the link to access the setup file of the EWARS Stand-alone app into an internet browser:

[[https://ewars.ws/static/apps/ewars_setup.exe]{.underline}](https://ewars.ws/static/apps/ewars_setup.exe)

-   When you click on the link, the setup file should begin to download automatically. You can view the progress of the download at the bottom right-hand corner of the browser:

![Text Description automatically generated with medium confidence](media/image814.png){width="2.2552088801399823in" height="0.5833333333333334in"}

-   After the download is complete, the **ewars_setup.exe** file appears in the progress bar:

![](media/image815.png){width="2.3020833333333335in" height="0.4166666666666667in"}

**Step 3.** Install the EWARS Stand-alone app on your computer.

-   Double-click on the downloaded file. A dialogue box appears saying "Windows protected your PC", as shown below:

![Graphical user interface, application Description automatically generated](media/image816.png){width="4.7856649168853895in" height="2.7864588801399823in"}

-   Click on **More info**, and the screen below appears:

![Graphical user interface, text, application Description automatically generated](media/image817.png){width="4.776042213473316in" height="3.1695548993875766in"}

-   Click on **Run anyway**, and the app starts installation. Check the progress bar of the installation process:

> ![Graphical user interface Description automatically generated with medium confidence](media/image818.png){width="3.96875in" height="1.5729166666666667in"}

-   After installation, the desktop app opens automatically, as shown below:

> ![Graphical user interface, application Description automatically generated](media/image819.png){width="4.315259186351706in" height="2.1270680227471566in"}

You now have a working version of EWARS Stand-alone installed on your machine.

## 25.2 Syncing your account for the first time

Synchronization of an account is the process of fetching data such as forms, alarms, users and so on from WHO EWARS to your EWARS Stand-alone account and of sending submitted reports and triggered alerts from your EWARS Stand-alone app to the WHO EWARS server.

The sync feature is available only for users using EWARS Stand-alone and EWARS Mobile apps.

After installation, it is important to sync your account before using the EWARS Stand-alone account. When you sync your account for the first time, all the forms, alarms, users, dashboards, bulletins and similar of your account on the WHO EWARS server also become available in the EWARS Stand-alone app.

You can sync your account using one of the following two options (see Fig. 25.2).

-   You can sync directly with **WHO EWARS**. This requires a reliable internet connection.

-   You can sync with the **nearest hub**. This does not require an internet connection. The nearest hub is another EWARS Stand-alone account connected to the same network.

Fig 25.2. Syncing your account with WHO EWARS or the nearest hub

![](media/image820.jpg){width="6.552083333333333in" height="0.9964621609798775in"}

These options are detailed in the following sections.

### 25.2.1 Syncing with WHO EWARS

WHO EWARS is a WHO-controlled server accessible via the internet. To sync your data with it, you require an active data connection.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** if you are already a registered user, use your EWARS credentials. If you are not a registered user, you need to create an account or request an Account Administrator to create one for you.
  --------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Before you sync your account, ensure that your laptop/desktop is connected to the internet.

-   Click on the **EWARS** ![](media/image821.png){width="0.20833333333333334in" height="0.2604166666666667in"} icon on your desktop, and the screen below appears:

![Graphical user interface, application Description automatically generated](media/image819.png){width="5.163791557305337in" height="2.5447845581802273in"}

-   Enter your EWARS account details to sign in -- i.e. your **Email** (e.g. "countryxadmin@gmail.com") \> enter your **Password** (e.g. "afv52@127") \> click on **Login**. The **Sync Account** dialogue box appears, as shown below:

![Graphical user interface, text, application Description automatically generated](media/image822.png){width="3.7083333333333335in" height="1.1354166666666667in"}

-   Click on **Sync now**, and the following screen appears:

![](media/image823.png){width="5.583333333333333in" height="1.488888888888889in"}

-   Select **Global EWARS (ewars.ws)** from the **Syncing with** drop-down menu \> click on ![](media/image824.png){width="0.65625in" height="0.2604166666666667in"} in your account (Country X). The synchronization process starts, and the progress bar below appears:

![Graphical user interface, application Description automatically generated](media/image825.png){width="6.395833333333333in" height="2.078591426071741in"}

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** if the internet connection is lost during the synchronization process, a notification appears, as shown below:
  --------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](media/image826.png){width="3.5416666666666665in" height="1.0104166666666667in"}

Once the internet connection is re-established, you need to sync again.

-   Once the synchronization process is completed, a notification appears, and the account is synced. The country name appears in blue with a **last synced on** message, as shown below:

![](media/image827.png){width="6.00321084864392in" height="1.6633891076115486in"}

-   Click on the name of the account (e.g. Country X). You will be logged in to your EWARS Stand-alone account and should be able to view a screen like the one below:

![Treemap chart Description automatically generated with medium confidence](media/image828.png){width="6.40625in" height="3.2702055993000876in"}

### 25.2.2 Syncing with the nearest hub

A hub is another EWARS Stand-alone account. Your nearest hub may be an account managing data for the nearest province or district. Neighbouring hubs can sync data if the two Stand-alone accounts (i.e. laptops) are connected to the same Wi-Fi or the same local area network.

[To sync your EWARS Stand-alone app with the nearest hub, follow the steps]{.mark} below.

**Step 1.** Obtain the internet protocol (IP) address of the nearest hub.

-   Start the EWARS Stand-alone app by clicking on the **EWARS** ![](media/image821.png){width="0.20833333333333334in" height="0.2604166666666667in"} icon on the desktop of the nearest hub.

-   Click on the ![](media/image829.png){width="0.31063976377952757in" height="0.26357392825896764in"} icon on the dashboard screen and the **My IP Addresses** dialogue box below appears:

![Graphical user interface, text, application Description automatically generated](media/image830.png){width="6.427083333333333in" height="2.4843755468066493in"}

-   Note down the IP address in the screenshot as it will be needed for syncing.

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** an IP address is the unique number given to your computer when it is connected to a network. This can change each time you reconnect, so you should not omit this step of checking your IP address when syncing, to ensure that you have the correct up-to-date address.
  --------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Step 2.** Sync your account.

-   Click on the **EWARS** ![](media/image821.png){width="0.20833333333333334in" height="0.2604166666666667in"} icon on your desktop. The screen below appears:

![Graphical user interface, application Description automatically generated](media/image819.png){width="4.984375546806649in" height="2.4583573928258966in"}

-   Enter your **Email** \> enter your **Password** \> click on **Login**. The **Sync Account** dialogue box below appears:

![Graphical user interface, text, application Description automatically generated](media/image822.png){width="3.7083333333333335in" height="1.1354166666666667in"}

-   Click on **Sync now**, and your accounts are listed, as shown below:

![](media/image823.png){width="5.58333552055993in" height="1.488888888888889in"}

-   Select **Nearest Hub** from the **Syncing with** drop-down menu, as in the following screenshot:

![](media/image831.png){width="5.635416666666667in" height="2.3480905511811025in"}

-   Enter the IP address of the nearest hub in the textbox, as shown below:

![Graphical user interface, application Description automatically generated](media/image832.png){width="6.270833333333333in" height="1.7643700787401575in"}

-   Click on ![](media/image833.png){width="1.1717125984251968in" height="0.21054243219597552in"} and the following screen appears:

![](media/image834.png){width="5.850343394575678in" height="2.6570319335083115in"}

All the accounts available in the nearest hub are listed. You can now sync your account.

-   Click on ![](media/image824.png){width="0.65625in" height="0.2604166666666667in"} next to Country X, and the screen below appears:

![Graphical user interface, text, application, email Description automatically generated](media/image835.png){width="6.354166666666667in" height="2.369792213473316in"}

-   Once you click on ![](media/image824.png){width="0.65625in" height="0.2604166666666667in"}, a confirmation request is sent to the nearest hub.

![](media/image836.png){width="4.510416666666667in" height="1.6663484251968503in"}

If confirmation of the request is not received within 15 seconds, you will have to repeat the request and start the process again from the beginning.

-   Click on **Yes** and the account is synced with the nearest hub. The synchronization process starts, and a progress bar appears, as shown below:

![](media/image837.png){width="5.610726159230096in" height="2.8404297900262465in"}

-   Once the synchronization process is complete, a notification appears, confirming that the account is synced with the nearest hub.

## 25.3 Sending reports from one EWARS Mobile account to another 

After you have synced your EWARS Stand-alone account successfully, the next step is to receive reports from EWARS Mobile users. This data transfer does not require reliable internet connectivity: it can take place using a local hotspot created by the mobile phone, and the connection is established with the help of a quick response (QR) code.

In a context with no internet connectivity, the mobile phone may not even have a SIM card, but you should be able to share data from an EWARS Mobile to an EWARS Stand-alone account. The most convenient way to share EWARS Mobile data is to sync your data with another EWARS Mobile account, which acts as a data receiver. In field settings, a surveillance officer may travel to remote reporting centres with an EWARS Mobile account, where he/she can sync data from reporting centres to EWARS mobile. On return to the surveillance hub, the surveillance officer can sync the collected data with the Stand-alone account.

EWARS Mobile data transfer happens via a hotspot. For the hotspot to work, all equipment should be in close proximity to each other and on the same local area network.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** your mobile phone should be equipped with a camera in order to scan the QR code.
  --------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ---------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![](media/image43.png){width="0.65625in" height="0.3541666666666667in"}   Mobile users can report and save data (e.g. in a weekly forms) in EWARS Mobile and take the mobile phone to sync with the local hub at the surveillance office on a specified day of the week. Syncing via a hotspot takes only a few seconds. Alternatively, they can sync data with another EWARS Mobile account at the health facility. The second mobile phone will ultimately sync the data with the local hub.

  ---------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The steps below set out the process of submitting reports between EWARS Mobile accounts from both the **sender** perspective and the **receiver** perspective.

At the **sender's** end, follow the steps below.

-   Tap on the **sync** ![](media/image838.png){width="0.34375in" height="0.3020833333333333in"} icon at the top right-hand corner of the home screen on your EWARS Mobile app.

-   Tap on ![](media/image839.png){width="0.7395833333333334in" height="0.28125in"}.

-   Tap on ![](media/image840.png){width="1.3125in" height="0.34375in"}. A hotspot is created on your mobile phone and a QR code is generated (Fig. 25.2).

Fig. 25.2. Sending reports from one EWARS Mobile account to another

![](media/image841.png){width="6.4609448818897635in" height="7.119792213473316in"}

At the **receiver's** end, follow the steps below.

-   Tap on the **sync** ![](media/image838.png){width="0.34375in" height="0.3020833333333333in"} icon at the top right-hand corner of the home screen on your EWARS Mobile app.

```{=html}
<!-- -->
```
-   Tap on ![](media/image839.png){width="0.7395833333333334in" height="0.28125in"}.

-   Tap on ![](media/image842.png){width="1.5416666666666667in" height="0.3125in"} while your Wi-Fi service is enabled, and a QR code scanner is opened to scan the code.

-   Point the device's camera at the QR code so that it is clearly visible within your mobile phone's screen. The phone automatically scans the code (Fig. 25.3).

Fig. 25.3. Receiving reports in one EWARS Mobile account from another

![](media/image843.png){width="5.744792213473316in" height="6.30800634295713in"}

Once the scan is successful, the sender gets a notification confirming the data transfer. The sender confirms, and the data are transferred. The receiver can view the submitted report(s) in the queue.

## 25.4 Sending reports from EWARS Mobile to EWARS Stand-alone

This feature enables Reporting Users to share reports from EWARS Mobile to the EWARS Stand-alone app without internet connectivity. In this activity, EWARS Stand-alone acts as a **receiver** and EWARS Mobile acts as a **sender**. The data transfer takes place using a local hotspot created by the mobile phone, and the connection is established with the help of QR code.

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** your laptop/desktop needs to be equipped with a camera in order to scan the QR code.
  --------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The steps below set out the process of submitting reports, from both the EWARS Stand-alone (**receiver**) perspective and the EWARS Mobile (**sender**) perspective.

**Step 1.** Initiate the process of receiving reports on the EWARS Stand-alone app.

-   Start the EWARS Stand-alone app by clicking on the **EWARS** ![](media/image821.png){width="0.20833333333333334in" height="0.2604166666666667in"} icon on your desktop. The screen below appears:

![Graphical user interface, application, Word Description automatically generated](media/image844.png){width="6.40625in" height="2.369792213473316in"}

-   Click on the **receive reports** ![](media/image845.png){width="0.2604166666666667in" height="0.24706146106736657in"} icon highlighted in the screenshot above. The QR code scanner screen below appears:

![A picture containing shape Description automatically generated](media/image846.png){width="6.348958880139983in" height="3.5306397637795275in"}

The QR code reader/scanner is now online on EWARS Stand-alone.

**Step 2.** Send reports from the EWARS Mobile app.

-   Start the EWARS Mobile app by tapping on the **EWARS** ![](media/image847.png){width="0.3958333333333333in" height="0.40625in"} icon on the home screen of your Mobile phone.

-   Tap on the **sync** ![](media/image848.png){width="0.28125in" height="0.23958333333333334in"} icon visible at the top right-hand corner of the home screen.

![Table Description automatically generated](media/image849.png){width="3.1458333333333335in" height="3.2552088801399823in"}

-   The sync options screen appears, as shown below:

![Graphical user interface, text, application, chat or text message Description automatically generated](media/image850.png){width="2.9895833333333335in" height="3.088542213473316in"}

-   Tap on ![](media/image851.png){width="1.0499671916010498in" height="0.26016841644794403in"}, and the Local EWARS selection screen appears. Tap on ![](media/image852.png){width="2.2291666666666665in" height="0.21875in"}, as shown below:

![Graphical user interface, text, application Description automatically generated](media/image853.png){width="3.0416666666666665in" height="4.484375546806649in"}

-   A screen saying **Creating hotspot** appears. Stay on the screen for a few seconds and the EWARS Mobile app starts a mobile hotspot and generates a QR code, as shown below:

![Qr code Description automatically generated](media/image854.png){width="2.875in" height="3.776042213473316in"}

This QR code generated on EWARS Mobile needs to be scanned using a camera available on the laptop or desktop with the EWARS Stand-alone app installed.

**Step 3.** Scan the QR code via the EWARS Stand-alone app.

-   [Hold the mobile phone so that the QR code is clearly visible within the camera on your]{.mark} laptop or desktop[, as shown below:]{.mark}

![Qr code Description automatically generated](media/image855.png){width="6.317708880139983in" height="3.5208333333333335in"}

-   Once the QR code is scanned successfully, EWARS Stand-alone connects to an AndroidShare mobile hotspot that is created automatically by the system, as shown in the image below:

![A screenshot of a computer Description automatically generated with medium confidence](media/image856.png){width="6.385416666666667in" height="2.9531255468066493in"}

-   Once connected, the confirmation notification to sync data appears on EWARS Mobile. Tap on **Yes**, as shown below:

![Graphical user interface, text, application Description automatically generated](media/image857.png){width="2.5833333333333335in" height="3.03125in"}

-   The synchronization process starts, and a notification appears on the EWARS Stand-alone app. Once the account is synced, the following notification appears:

![Graphical user interface, application Description automatically generated](media/image858.png){width="3.7604166666666665in" height="1.0833333333333333in"}

All the collected reporting data are available under the Report manager menu in EWARS Stand-alone.

Once an internet connection is available, you can submit all the data from EWARS Stand-alone to the WHO EWARS server. The following topic addresses this in greater detail.

## 25.5 Subsequent syncing

Once the reports are received from EWARS Mobile, the next step is to submit the data from EWARS Stand-alone to WHO EWARS. This is achieved using subsequent syncing. Alongside submitting the data, subsequent syncing ensures that all the newly configured items (e.g. forms, bulletins and dashboards) on WHO EWARS are now also available in your EWARS Stand-alone app.

  ---------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![](media/image43.png){width="0.65625in" height="0.3541666666666667in"}   It is recommended that you sync your EWARS Stand-alone account with the WHO EWARS server from time to time, to send and receive the latest data generated in both apps.

  ---------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To sync your account, follow the steps below.

-   Start the EWARS Stand-alone app by clicking on the **EWARS** ![](media/image821.png){width="0.20833333333333334in" height="0.2604166666666667in"} icon on your desktop.

-   Click on the **sync** ![](media/image859.png){width="0.3645833333333333in" height="0.3229166666666667in"} icon at the top right-hand corner of your dashboard screen, and the screen below appears:

![](media/image860.png){width="5.489583333333333in" height="1.4753258967629046in"}

-   Select an appropriate option from the **Syncing with** drop-down menu. The options are:

```{=html}
<!-- -->
```
-   Global EWARS (dev.ewars.ws)

-   Nearest Hub.

For more information about these options, refer to topic **25.2 Synchronizing your account for the first time**.

-   Once the synchronization process is complete, a notification appears, and the account is synced. The country name appears in blue, and the **last synced on** message is shown below it.

When syncing the account, conflicts might arise if parallel edits are made in the same report across local installations. In such a scenario, you need to resolve the conflicts in order to sync successfully with the WHO EWARS server.

The following topic provides detailed information about identifying and resolving such conflicts.

### 25.5.1 Identifying conflicts

A conflict can occur when WHO EWARS has received an updated copy of a report and a user attempts to update an earlier version of the same report.

For demonstration purposes, this guide uses the following example of how a conflict might arise.

**Example 1.** Let's assume that two users -- User A and User B -- are assigned to submit using Report 1.

-   User A submits Report 1, as shown below:

![Graphical user interface, text, application Description automatically generated](media/image861.png){width="6.416666666666667in" height="2.2708081802274718in"}

-   User A syncs with the WHO EWARS server (refer to topic **25.2.1 Syncing with WHO EWARS** for more information).

-   User B syncs with the WHO EWARS server, and Report 1 is now available in the EWARS Stand-alone app, as shown below:

![Graphical user interface, text, application Description automatically generated](media/image862.png){width="5.947916666666667in" height="2.0350918635170605in"}

-   User A and User B both amend Report 1 from their EWARS Stand-alone apps simultaneously.

-   User B syncs the amended Report 1 with the WHO EWARS server. Once the synchronization is performed, the amended report is available in WHO EWARS.

-   When User A attempts to sync their amended Report 1 with the WHO EWARS server afterwards, a conflict is reported in the EWARS Stand-alone app.

User A sees the following screen on the EWARS Stand-alone app:

![](media/image863.png){width="6.450021872265967in" height="2.5934459755030623in"}

The conflict arises because User A is trying to submit an earlier version of Report 1 to the WHO EWARS server. WHO EWARS has an updated copy of the report, as a result of the synchronization performed by User B.

### 25.5.2 Resolving conflicts

Once the conflict is generated, it can be resolved as outlined below.

-   To view the conflict, click on **Go to Conflicts**, and the Report manager screen appears.

-   Click on ![](media/image864.png){width="1.0625in" height="0.3125in"} and the following screen appears:

![Graphical user interface, text, application Description automatically generated](media/image865.png){width="6.067708880139983in" height="1.857263779527559in"}

The conflict is listed at the right-hand side, as shown above.

-   To **resolve** the conflict, click on the **edit** ![](media/image866.png){width="0.21739173228346456in" height="0.20833333333333334in"} icon, and the following screen appears:

![Graphical user interface, application Description automatically generated](media/image867.png){width="5.578125546806649in" height="3.1174759405074366in"}

As seen in the screenshot above, the difference between the field values present in the EWARS Stand-alone app report version and the WHO EWARS server report version is identified. You can choose to keep the local changes made in your EWARS Stand-alone app or to keep the global changes available in the WHO EWARS server.

-   **Either** c**lick** on ![](media/image868.png){width="0.96875in" height="0.19791666666666666in"} to keep the local changes made in your EWARS Stand-alone app

-   **Or** click on ![](media/image869.png){width="1.1875in" height="0.19791666666666666in"} to keep the global changes.

```{=html}
<!-- -->
```
-   A confirmation box appears, as shown below:

![Graphical user interface, text, application Description automatically generated](media/image870.png){width="5.864583333333333in" height="3.119792213473316in"}

-   Click on **Confirm** to resolve the conflict.

## 25.6 Identifying online/offline features through icons

You can identify the online and offline features in the menu through green and grey dot icons. Online features can be accessed only if you have an active internet connection. Offline features can be accessed even if you do not have internet access. All the features are available to users with reliable internet connectivity. EWARS Stand-alone users can only access offline features due to unreliable internet connectivity.

-   Features with a green dot ![](media/image871.png){width="0.13541666666666666in" height="0.14583333333333334in"} can be accessed when you have an active data connection.

-   Features with a grey dot ![](media/image872.png){width="0.15625in" height="0.17708333333333334in"} can only be accessed without an active data connection.

You can identify which features are available online or offline as follows.

-   Start the EWARS Stand-alone app by clicking on the **EWARS** ![](media/image821.png){width="0.20833333333333334in" height="0.2604166666666667in"} icon on your desktop. Select **Menu**, and the screen below appears:

![](media/image873.png){width="6.308525809273841in" height="2.273698600174978in"}

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image14.png){width="0.28125in" height="0.28125in"}   **Note:** if you try to access a feature that is only available online without an active data connection, you will see the following notification:
  --------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](media/image874.png){width="3.75in" height="1.2916666666666667in"}

## 25.7 Viewing time left to sync the account

EWARS Stand-alone continuously displays the time (in days) left to sync at the top of your dashboard screen. If the account is not synced within the specified time frame, the [account is locked and you are redirected to the sync screen.]{.mark}

To view the time left to sync your account, follow the steps below.

-   Start the EWARS Stand-alone app by clicking on the **EWARS** ![](media/image821.png){width="0.20833333333333334in" height="0.2604166666666667in"} icon on your desktop, and the following screen appears:

![Graphical user interface, application Description automatically generated](media/image875.png){width="6.010416666666667in" height="2.151042213473316in"}

At the top of the dashboard screen, you can view the days left to sync your account.

-   Once the expiry time is reached, the account is locked. You are redirected to the sync screen, and the following dialogue box appears:

![](media/image876.png){width="3.71875in" height="1.0208333333333333in"}

## 25.8 Unsyncing an account from the EWARS Stand-alone app

When you unsync an account, it does not delete the data from the WHO EWARS server but only removes it from the EWARS Stand-alone app installed on your local desktop or laptop. Thus, an EWARS Stand-alone account can be removed from a machine with confidence that the data it handled have also been removed locally, but are still available in WHO EWARS.

  ---------------------------------------------------------------------------------- -------------------------------------------------------------
  ![](media/image43.png){width="0.65625in" height="0.3541666666666667in"}   When an account is no longer in use, you should unsync it.

  ---------------------------------------------------------------------------------- -------------------------------------------------------------

To unsync an EWARS Stand-alone account, follow the steps below.

-   Start the EWARS Stand-alone app by clicking on the **EWARS** ![](media/image821.png){width="0.20833333333333334in" height="0.2604166666666667in"} icon on your desktop \> click on the **sync** ![](media/image877.png){width="0.3229166666666667in" height="0.2604166666666667in"} icon, and the screen below appears:

![](media/image878.png){width="5.552083333333333in" height="2.220833333333333in"}

-   To unsync the Country X account, click on ![](media/image879.png){width="0.6979166666666666in" height="0.19791666666666666in"}, and a confirmation box appears.

-   Click on **Confirm**, and the account and its data are deleted.

## 25.9 Troubleshooting the EWARS Stand-alone app

If you experience either of the following scenarios, you can troubleshoot your EWARS Stand-alone app using the options below.

**Scenario 1.** New changes made in the EWARS Stand-alone app are not visible to you.

-   Click on **F5** -- this reloads the app page.

-   If the problem persists, log out of your EWARS Stand-alone app and log in again.

-   If the problem still persists, click on **Ctrl + F5** -- this forces the app to reload the latest version.

-   If the problem continues to persist, you can try uninstalling the EWARS Stand-alone app and reinstalling it.

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image211.png){width="0.41060695538057745in" height="0.3875in"}**WARNING:**   If you uninstall the app**,** all your data (synced and unsynced) are deleted from your EWARS Stand-alone account. (Unsynced data include the data available only in your EWARS Stand-alone app, which are yet to be submitted to WHO EWARS).
  --------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-   For any other technical problems, contact the Account Administrator or write to **<ewars@who.int>** for EWARS support.

**Scenario 2.** The app freezes, or you are getting error messages while using it.

-   Click on **Ctrl + F5** -- this forces the app to reload the latest version.

-   For any other technical problems, contact the Account Administrator or EWARS support.

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Icon Description automatically generated](media/image211.png){width="0.41060695538057745in" height="0.3875in"}**WARNING:**   If you click on **Ctrl + Shift + Z**, all your data (synced and unsynced) are deleted from your EWARS Stand-alone account. (Unsynced data include the data available only in your EWARS Stand-alone app, which are yet to be submitted to WHO EWARS).
  --------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Chapter 26. Glossary

This glossary provides definitions of key terms, abbreviations and concepts, familiarity with which will help you to make optimal use of the Early Warning, Alert and Response System (EWARS). The terms are listed in order of their appearance in this web user guide.

-   WHO's **Emergency Response Framework** (ERF) provides WHO staff with essential guidance on how the Organization manages assessment, grading and response to public health events and emergencies with health consequences, in support of Member States and affected communities. ERF is an important contribution towards improving the predictability, timeliness and effectiveness of WHO's response to emergencies.

-   **Outbreak** is a phase in which there is an increase in the sudden occurrence of any disease cases in a particular time and place. It can last for days or months, or even years.

-   **Humanitarian emergency** is an event or series of events that represents a critical threat to the health, safety, security or well-being of a community or other large group of people, usually over a wide area.

-   **SMS (Short Message Service) Gateway** is an account on a mobile phone with the SMS Gateway app activated. The SMS Gateway app receives the reports submitted via SMS by the Reporting Users and sends them to the WHO EWARS server once an internet connection becomes available.

-   **EWARS Stand-alone** is an application set up on a dedicated laptop or desktop (with a Windows operating system).

-   **Surveillance** is the process of close monitoring and observation of a particular person or group.

-   **Dissemination** is the act or process of distributing, spreading, broadcasting or dispersing widely.

-   **Alarms** are configured based on set criteria. When the reported forms match these criteria, alerts are triggered.

-   **Alert log** allows you to manage triggered alerts by following a standardized workflow.

-   **System-generated email address** is an email address ending in "@ewars.ws" that is automatically created by the system for a new user without their own email address. Users created using a system-generated email address do not receive notification emails from the system. This is a good way to create Reporting Users at health centres.

-   **PCODE** is an abbreviation of **place code**. PCODEs are unique identifiers for locations represented by combinations of letters and/or numbers to identify a specific location within a database. These codes provide a systematic means of linking data to an unambiguous location (e.g. PCODE NBT001 or NBT001HF001, and so on).

-   **UUID** stands for "universally unique identifier". This is a system-generated unique number, which consists of 36 characters.

-   **Widget** is a graphical user interface element designed to interact with an application or service.

-   **Tags** are identifiers that help you to find transferable items in the Configuration Transfer menu. You can add one or more tags to each transferable item.

-   **Submission electronic identification (EID) Prefix** is a prefix concatenated before the submission EID, which will help to identify a unique report on its submission.

-   **epi week** is an epidemiological week -- a standardized method to define a week as a period to group epidemiological events. Normally, the epi week starts on Sunday or Monday.

-   **Alert EID Prefix** is a prefix concatenated before the alert EID, which will help to identify a unique alert.

-   **Standard deviation (SD)** is a statistic that measures the dispersion of a dataset relative to its mean. It is calculated as the square root of the average squared difference from the mean.

-   **Percentile** is the value below which a percentage of data falls.

-   **Seasonality** is a periodic surge in disease incidence corresponding to seasons or other calendar periods, characterizing many infectious diseases of public health importance.

-   **Domain** of a website is the one under which EWARS is currently running -- in the case of WHO hosting the server, it is "ewars.ws".

-   **HTML** [(Hypertext Markup Language) is the most basic building block of the World Wide Web. It defines the meaning and structure of web content.]{.mark} You can find out more information about HTML on various websites (e.g. [developer.mozilla.org/en-US/docs/Web/HTML]{.mark}).

-   **URL** is an abbreviation that stands for "universal resource locator". This is the text you type into your internet browser when you want to visit a website. In its most common form, a URL starts with "http://" or "https://", followed by "www." and then the website name. This can be followed by the address of a specific page, or of a directory, followed by a specific page.

-   **OCHA** (the United Nations Office for the Coordination of Humanitarian Affairs) has designed some free icons that can be used in the response to complex emergencies and natural disasters.

-   **Choropleth** -- a choropleth map is a type of thematic map in which a set of predefined areas is coloured or patterned in proportion to a statistical variable that represents an aggregate summary of a geographical characteristic within each area.

-   **CSS** [(Cascading Style Sheets) is a stylesheet language used to describe the presentation of a document written in HTML. CSS describes how elements should be rendered on screen, on paper, in speech or in other media.]{.mark} You can find out more information about CSS on various websites (e.g. [developer.mozilla.org/en-US/docs/Web/CSS).]{.mark}

# Chapter 27. Help and support

**Who hosts, supports and manages Early Warning, Alert and Response System (EWARS) in a box?**

EWARS is managed by the Health Emergency Interventions Department in the WHO Health Emergencies Programme at WHO headquarters, Geneva, Switzerland. WHOs remit within the Health Emergencies Programme includes offering support to rapid detection of disease outbreaks in emergency, fragile and conflict settings.

**Who are the main users of EWARS?**

EWARS is aimed at emergency responders managing disease early warning in conflict, fragile and vulnerable settings. These may be epidemiologists, surveillance officers and public health officers of ministries of health, regional health authorities, United Nations agencies, nongovernmental organizations (NGOs) and other health partner organizations. The key users are front-line workers in the field, working with the ministry of health or NGO partners. EWARS has been primarily designed and built with the needs of these users in mind.

**Do I need to pay to use the application?**

No. The EWARS application is free to use for WHO and its partners. The application uses no proprietary or third-party software. But Countries are free to donate to EWARS Mobile for the development of new features

**Where are the data stored?**

The data are stored on cloud-based servers, so the system can be deployed rapidly in the field without the need for local servers to be configured and maintained. However, if server capacity is available, the system can be set up locally in the country.

**Can I use EWARS on my phone?**

Yes. A mobile version of EWARS is available on phones running Android operating system version 6.0 Marshmallow or higher.

**Who owns the data?**

The ministry of health, local authorities, local partners who manage, analyse and export the data into other formats as appropriate own the data. Other stakeholders can also be granted access to the data through a system of user permissions and privileges.

**Are the data secure?**

The servers where the data are stored are protected by Secure Sockets Layer (SSL) security. This means that all connections to the database are encrypted. In addition, if any individual patient data are collected, they are redacted when exported from the application or shared in other formats. As a result, privacy and confidentiality are protected.

**Can I use EWARS when I do not have access to the internet?**

Yes. In addition to the mobile version of EWARS, a desktop version can be downloaded and installed on your laptop. This allows data to be managed offline.

**Does the project offer training?**

Yes. EWARS Super Administrators collaborate with WHO regional and country offices to train staff to set up and manage EWARS in emergencies. We can also train partners working in emergencies in the field directly.

**How can I request EWARS to be implemented in my country/context during an emergency?**

Please write to the EWARS core team or Super Administrators, who would be happy to discuss your needs, at <ewars@who.int>. A final decision regarding use of EWARS in a country is made in consultation with emergency responders, the ministry of health and the WHO country and regional offices.

**If I decide to use EWARS, what will happen to my old data?**

In countries where an existing system is replaced by EWARS, the old data can be imported into the new database, ensuring continuity with previous data. During and/or after emergency, the data can be sent to the existing HIMS using API.

**Where can I get more information and support?**

Please write to [[ewars@who.int]{.underline}](mailto:ewars@who.int) or visit <https://www.who.int/emergencies/surveillance/early-warning-alert-and-response-system-ewars>

[^1]: Emergency response framework (‎ERF)‎, second edition. Geneva: World Health Organization; 2017 (https://apps.who.int/iris/handle/10665/258604, accessed 4 April 2022).
