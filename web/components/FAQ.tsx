'use client'

import {
    Accordion,
    AccordionContent,
    AccordionItem,
    AccordionTrigger,
} from "@/components/ui/accordion"

import '../styles/FAQ.css'

type FAQItem = {
    question: string;
    answer: string;
}

type FAQProps = {
    faqs: FAQItem[];
}

export default function FAQ({faqs}: FAQProps) {
    return (
        <section id="faq">
            <div className="faq-container">
                <div className="faq-header">
                    <h2 className="site-heading">
                        Frequently Asked <span>Questions</span>
                    </h2>

                    <p className="site-body">
                        Find answers to common questions about Knowescape
                        Consulting, our business support services, B-BBEE
                        advisory, Skills Development, Enterprise & Supplier
                        Development, and Startup Support.
                    </p>
                </div>

                <Accordion
                    className="faq-accordion"
                >
                    {faqs.map((faq, index) => (
                        <AccordionItem
                            key={index}
                            value={`item-${index + 1}`}
                        >
                            <AccordionTrigger>
                                {faq.question}
                            </AccordionTrigger>

                            <AccordionContent>
                                {faq.answer}
                            </AccordionContent>
                        </AccordionItem>
                    ))}
                </Accordion>
            </div>
        </section>
    )
}