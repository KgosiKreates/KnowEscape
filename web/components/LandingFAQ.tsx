import FAQ from "./FAQ"
import '../styles/landingfaq.css'

const faqs = [
    {
        question: "What services does Knowescape Consulting offer?",
        answer: "Knowescape Consulting provides business support across B-BBEE Advisory, Enterprise & Supplier Development, Skills Development, and Startup Support. Our services are designed to help businesses strengthen compliance, develop their people, improve business capabilities, and create opportunities for sustainable growth."
    },
    {
        question: "What is B-BBEE Advisory?",
        answer: "Our B-BBEE Advisory services help businesses understand their B-BBEE requirements, assess their current position, identify gaps, and develop practical strategies to improve their B-BBEE performance. We also provide guidance on documentation, transformation initiatives, and verification readiness."
    },
    {
        question: "Can Knowescape help my business improve its B-BBEE score?",
        answer: "Yes. We can assess your current B-BBEE position, identify areas where improvement may be possible, and help develop a practical transformation strategy aligned with your business activities and applicable B-BBEE requirements."
    },
    {
        question: "What does Enterprise & Supplier Development involve?",
        answer: "Enterprise & Supplier Development focuses on supporting the growth and development of qualifying businesses within the broader business ecosystem. Our services can include enterprise development, supplier development, business growth support, and guidance on structuring development initiatives."
    },
    {
        question: "What Skills Development services do you provide?",
        answer: "Our Skills Development services include skills development training, workplace skills planning, learnerships and workplace training, employee development, and Skills Development compliance support. These services help organisations develop their workforce while aligning training initiatives with applicable requirements."
    },
    {
        question: "Can Knowescape assist with learnerships and workplace training?",
        answer: "Yes. We provide support for learnership and workplace training initiatives, helping businesses structure practical learning opportunities that combine training with workplace experience and contribute to meaningful skills development."
    },
    {
        question: "What is Workplace Skills Planning?",
        answer: "Workplace Skills Planning involves identifying the skills an organisation currently has, determining development needs, and planning appropriate training and development activities. Effective planning helps businesses align workforce development with operational and organisational objectives."
    },
    {
        question: "Does Knowescape provide Skills Development compliance support?",
        answer: "Yes. We help businesses understand applicable Skills Development requirements, organise supporting documentation, and align their training and development activities with their compliance objectives."
    },
    {
        question: "What Startup Support does Knowescape provide?",
        answer: "Our Startup Support services can assist entrepreneurs and new businesses with business planning, business registration and setup, startup strategy, business mentorship, and growth and market readiness."
    },
    {
        question: "Can Knowescape help me start a business from scratch?",
        answer: "Yes. We can provide structured support through the early stages of establishing a business, from developing a business plan and defining your strategy to preparing the business for growth and entering the market."
    },
    {
        question: "Can established businesses also use Knowescape's services?",
        answer: "Yes. Our services are relevant to both established businesses and growing enterprises. Support can be tailored to your organisation's current needs, whether you are addressing B-BBEE requirements, developing employees, strengthening suppliers, or preparing for growth."
    },
    {
        question: "How do I get started with Knowescape Consulting?",
        answer: "Start by contacting our team and telling us about your business, your objectives, and the support you are looking for. We can then help identify the appropriate service and discuss the next steps."
    },
]

export default function LandingFAQ () {

    return (
        <section id="landing-faq">
            <div className="landing-faq-container">
                <FAQ faqs={faqs} />
            </div>
        </section>
    )
}