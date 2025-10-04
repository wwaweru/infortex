# Infortex Solutions Limited - Website Development Prompt

## Project Overview
Build a modern, professional logistics website for **Infortex Solutions Limited** - a logistics and cargo services company operating in Kenya. The client has a very keen eye for design and expects a polished, contemporary website that rivals major logistics companies.

**Domain:** infortexsolutionsltd.co.ke  
**Launch Target:** As soon as viable (flexible timeline)  
**Design Inspiration:**
- https://www.kuehne-nagel.com/
- https://www.dhl.com/ke-en/home.html
- https://www.mitchellcottsgroup.com/

## Tech Stack
- **Framework:** Django
- **CMS:** Wagtail CMS
- **Database:** SQLite (for development/MVP)
- **Frontend:** Tailwind CSS
- **Server:** Gunicorn + Nginx
- **Python Version:** 3.10+
- **Django Version:** 4.2+ (LTS)

## Business Purpose
Create a website that provides:
- Brand visibility for logistics services
- Products and company policy details
- Contact and checkout functionality
- Cargo tracking for logistics services
- Integration possibilities with other service providers
- Platform for individual entrepreneurs and commercial service providers

## Core User Actions
Visitors should be able to:
1. Contact the company
2. Learn about services/products
3. View portfolio of past work
4. Make purchases/bookings
5. Track their cargo
6. Reserve or book logistics services

## Essential Pages (MVP)
1. **Home** - Hero section, services overview, CTA
2. **About** - Company information, mission, vision, team
3. **Services/Products** - Detailed service offerings
4. **Portfolio/Gallery** - Showcase of past projects/clients
5. **Contact** - Contact form, location map, business details
6. **FAQ** - Common questions and answers

## Must-Have Features

### Core Features
- ✅ Contact form with email notifications
- ✅ Phone/email display with click-to-call
- ✅ Social media links integration
- ✅ Image gallery/portfolio section
- ✅ Google Maps integration for office location
- ✅ SEO optimization (meta tags, sitemaps, robots.txt)
- ✅ Mobile-responsive design (mobile-first approach)
- ✅ Fast loading speeds and performance optimization

### Trust & Credibility
- Client testimonials/reviews section
- Case studies or success stories
- Industry certifications/accreditations display
- Partner logos showcase
- Years in business highlight

### Logistics-Specific Features
- Quote request form
- Services calculator (shipping cost estimates)
- Coverage area map (service regions)
- Fleet information display
- Warehouse/facility locations

### User Management
- ✅ Client registration system
- ✅ Client login/account area
- User dashboard for account management
- Order history tracking
- Profile management

### Communication Channels
- WhatsApp Business integration (click-to-chat)
- Live chat or chatbot for instant queries
- Multiple contact methods prominently displayed
- Business hours display

### Payment Integration
- ✅ M-Pesa payment gateway integration
- Secure checkout process
- Payment confirmation and receipts

### Legal & Compliance Pages
- Terms & Conditions
- Privacy Policy
- Shipping/Delivery Policy
- Refund/Claims Policy

### Security Features
- ✅ SSL Certificate ready (HTTPS)
- ✅ M-Pesa secure payment integration
- Data encryption for customer information
- CSRF protection (Django default)
- Secure user authentication

## Design Requirements

### Design Aesthetic
- **Style:** Professional, Minimal/Clean, Bold/Modern
- **Target Feel:** Premium logistics service provider
- **Color Scheme:** [To be provided with logo and branding]
- **Typography:** Clean, professional, highly readable
- **Layout:** Spacious, organized, easy navigation

### Design Principles
1. **Clean & Modern:** Contemporary design that builds trust
2. **User-Centric:** Intuitive navigation and clear CTAs
3. **Mobile-First:** Exceptional mobile experience
4. **Performance:** Fast loading, optimized images
5. **Accessibility:** WCAG 2.1 AA compliance where possible
6. **Visual Hierarchy:** Clear content organization
7. **Consistent Branding:** Unified look across all pages

### UI Components Needed
- Hero sections with compelling CTAs
- Service cards with icons
- Testimonial carousels
- Image galleries with lightbox
- Interactive forms with validation
- Loading states and animations
- Toast notifications for user feedback
- Breadcrumb navigation
- Footer with sitemap
- Mobile hamburger menu
- Search functionality (future)

## Technical Requirements

### Django/Wagtail Structure
```
infortex/
├── infortex/              # Project settings
├── home/                  # Home app (Wagtail)
├── services/              # Services pages
├── portfolio/             # Portfolio/Gallery
├── blog/                  # Future: Blog/News (optional)
├── accounts/              # User authentication
├── bookings/              # Booking/Orders system
├── payments/              # M-Pesa integration
├── static/                # Static files (CSS, JS, images)
├── media/                 # User uploaded content
├── templates/             # HTML templates
│   ├── base.html
│   ├── includes/
│   └── pages/
└── requirements.txt
```

### Wagtail Configuration
- StreamFields for flexible page content
- Custom page models for different page types
- Rich text editing capabilities
- Image management and optimization
- SEO fields for all pages
- Preview functionality
- Workflow/moderation (if needed)
- Multi-site support ready

### Frontend Setup
- Tailwind CSS via CDN or compiled
- Alpine.js for lightweight interactivity (optional)
- Responsive breakpoints (mobile, tablet, desktop)
- Custom Tailwind config for brand colors
- Icon library (Heroicons or similar)
- Image lazy loading
- Smooth scrolling and animations

### Forms & Validation
- Django Forms with Tailwind styling
- Client-side and server-side validation
- CSRF protection
- File upload handling
- Email notifications
- Success/error messages
- Honeypot spam protection

### M-Pesa Integration
- Daraja API integration (Safaricom)
- Or payment aggregator (Flutterwave/Pesapal/Intasend)
- Payment initiation and callback handling
- Transaction logging
- Payment status updates
- Receipt generation

### User Authentication
- Django's built-in auth system
- Email verification (optional for MVP)
- Password reset functionality
- User profile pages
- Session management
- Social auth (future consideration)

### SEO Requirements
- Wagtail SEO fields
- Meta titles and descriptions
- Open Graph tags
- Twitter Card tags
- Sitemap.xml generation
- Robots.txt configuration
- Structured data (JSON-LD) for business
- Analytics ready (Google Analytics/Tag Manager)
- Clean URL structure

### Performance Optimization
- Image optimization (WebP format)
- Lazy loading for images
- Minified CSS/JS
- Browser caching headers
- Gzip compression
- Database query optimization
- CDN ready for static files

### Deployment Configuration
- Gunicorn WSGI server
- Nginx reverse proxy
- Static files serving via Nginx
- Environment variables (.env file)
- Requirements.txt with pinned versions
- Production settings separation
- Database migrations handling
- Logging configuration

## Content Status
⚠️ **Not Yet Available:**
- Written content for all pages (needs to be created)
- 5-10 professional images minimum (needs to be provided)
- Brand colors specification (will be provided with logo)

✅ **Available:**
- Logo/Business name
- Contact information
- Social media links
- Domain name (infortexsolutionsltd.co.ke)

## Post-MVP Features (Phase 2)
To be implemented after initial launch:
- Enhanced Google Maps with detailed directions
- Expanded photos/gallery section
- Full checkout and tracking system
- Real-time cargo tracking
- Admin dashboard with analytics
- Email marketing integration
- Multi-language support (English/Swahili)
- Blog/News section
- Advanced search functionality

## Development Approach
1. **Setup & Configuration**
   - Initialize Django project with Wagtail
   - Configure Tailwind CSS
   - Set up basic project structure
   - Create base templates

2. **Core Pages Development**
   - Build responsive base template
   - Create Wagtail page models
   - Develop homepage with hero section
   - Build other essential pages

3. **Features Implementation**
   - User authentication system
   - Contact forms and email handling
   - M-Pesa payment integration
   - Gallery/portfolio functionality

4. **Polish & Optimization**
   - SEO optimization
   - Performance tuning
   - Mobile responsiveness testing
   - Security hardening

5. **Content Integration**
   - Add client content when available
   - Integrate branding and logo
   - Upload images and media

6. **Testing & Deployment**
   - Cross-browser testing
   - Mobile device testing
   - Load testing
   - Deploy to production server

## Success Criteria
- ✅ Modern, professional design that impresses the client
- ✅ Fully responsive across all devices
- ✅ Fast loading times (< 3 seconds)
- ✅ All must-have features implemented
- ✅ Easy content management via Wagtail admin
- ✅ Secure user authentication and payments
- ✅ SEO optimized for search engines
- ✅ Clean, maintainable code
- ✅ Production-ready deployment configuration

## Additional Notes
- Client has a keen eye for design - prioritize aesthetics and UX
- Inspiration sites are industry leaders - match that quality
- Design should work for Kenyan market (M-Pesa, local context)
- Plan for future scalability and feature additions
- Code should be well-documented for future maintenance
- Wagtail admin should be simplified for non-technical client use

## Deliverables
1. Fully functional Django/Wagtail website
2. Responsive frontend with Tailwind CSS
3. User authentication system
4. M-Pesa payment integration
5. Contact forms and email notifications
6. SEO optimization
7. Deployment configuration (Gunicorn + Nginx)
8. README with setup instructions
9. Requirements.txt with dependencies
10. Admin documentation for client

---

**Important:** This is an MVP focused on getting the core website live quickly. The design must be modern and professional to meet client expectations. Post-MVP features will be added iteratively based on client feedback and business needs.