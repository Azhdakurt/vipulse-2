
# 💎 VIPulse 2.0

**VIP Player Management and Retention Review System**

VIPulse 2.0 is a full-stack web application developed to help iGaming customer support, VIP management and retention teams organise player information, assess player risk levels and document retention recommendations.

Built using Django and PostgreSQL, the application provides a centralised workspace where authorised users can manage VIP player profiles, create and update player reviews, monitor retention scores and access key operational statistics through a dashboard.

The project focuses on structured record management, clear navigation, responsive design and practical workflows for internal operational teams.

**[Live Application](https://vipulse-2-27dcf5edfa12.herokuapp.com/)** | **[GitHub Repository](https://github.com/Azhdakurt/vipulse-2)**

![VIPulse 2.0 Responsive Mockup](docs/vipulse-responsive-mockup.png)

*VIPulse 2.0 responsive presentation illustrating the application's desktop and mobile layouts.*

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Project Goals](#project-goals)
3. [Target Audience](#target-audience)
4. [User Stories and MoSCoW Prioritisation](#user-stories-and-moscow-prioritisation)
5. [Agile Methodology](#agile-methodology)
   - [GitHub Projects Kanban Board](#github-projects-kanban-board)
6. [UX Design](#ux-design)
   - [Design Approach](#design-approach)
   - [Wireframes](#wireframes)
   - [Colour Scheme and Typography](#colour-scheme-and-typography)
7. [Features](#features)
   - [Authentication and Access Control](#authentication-and-access-control)
   - [Dashboard](#dashboard)
   - [Player Management](#player-management)
   - [Player Profiles](#player-profiles)
   - [Review Management](#review-management)
   - [Forms and Validation](#forms-and-validation)
8. [Database Design](#database-design)
   - [Entity Relationship Diagram](#entity-relationship-diagram)
   - [Database Models](#database-models)
9. [Technologies Used](#technologies-used)
10. [Testing and Validation](#testing-and-validation)
11. [Deployment](#deployment)
    - [Local Deployment](#local-deployment)
    - [Heroku Deployment](#heroku-deployment)
12. [Bugs and Known Issues](#bugs-and-known-issues)
13. [Credits and Acknowledgements](#credits-and-acknowledgements)
14. [AI Assistance](#ai-assistance)

---

## Project Overview

VIP and retention teams often need to manage player records, review risk indicators and track recommended actions across multiple accounts. Without a structured system, this information can become difficult to organise, retrieve and maintain consistently.

VIPulse 2.0 addresses this challenge by providing a single application for player management and review tracking.

The application allows authenticated staff to:

- Create, view, update and delete VIP player records.
- Search for players using their username or Player ID.
- Filter player records by VIP tier.
- Create, edit and delete player reviews.
- Record risk levels, retention scores, notes and recommended actions.
- Filter reviews by risk level and retention score range.
- View individual player profiles and review histories.
- Monitor player and review statistics through a central dashboard.

VIPulse 2.0 is an internal staff-facing application. Authentication is required to access the dashboard, player records and review management features. Public self-registration is not available.

The application is designed as a portfolio project demonstrating full-stack development, relational database modelling, CRUD functionality, authentication, responsive user interfaces and software testing.

## Project Goals

The primary goals of VIPulse 2.0 are to:

1. Provide a centralised system for managing VIP player information.
2. Support consistent recording and review of player risk and retention assessments.
3. Make player records and review histories easy to search and access.
4. Present key operational information through a clear dashboard.
5. Protect internal application features through user authentication.
6. Deliver a responsive interface that works across different screen sizes.
7. Demonstrate full-stack development using Django and a relational database.

## Target Audience

VIPulse 2.0 is designed for internal operational teams working in the iGaming industry, including:

- **VIP Managers:** To review player profiles, VIP tiers and retention assessments.
- **Customer Support Teams:** To access structured player information and review histories.
- **Retention Teams:** To document retention scores, observations and recommended actions.
- **Team Leaders and Operations Managers:** To monitor player and review activity through the dashboard.

The application is a demonstration system rather than a production gambling platform. It does not process bets, payments or real-money transactions.
