'use client';

import { Badge } from './ui/badge'
import '../styles/contactSection.css'
import { toast } from "@/components/ui/toast"
import { TextAnimate } from './ui/text-animate'
import {ArrowUpRight, BadgeCheck} from "lucide-react"
import { useState } from 'react';

export default function ContactSection () {

    const [sending, setSending] = useState(false)

    const submitContact: React.SubmitEventHandler<HTMLFormElement> = async (e) => {
        e.preventDefault();
        setSending(prev => !prev)

        const form = e.currentTarget;
        const formData = new FormData(form);

        const data = {
            first_name: formData.get("first_name"),
            last_name: formData.get("last_name"),
            email: formData.get("email"),
            phone: formData.get("phone_number"),
            company: formData.get("company"),
            service: formData.get("service"),
            message: formData.get("message"),
        };

        try {
            const response = await fetch(
                `${process.env.NEXT_PUBLIC_API_URL}/contact/`,
                {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(data),
                }
            );

            const result = await response.json();

            if (!response.ok) {
                toast.add({
                    title: "Couldn't send form",
                    type: "error",
                    description: "We couldn't submit your request. Try again or wait a few minutes and try again",
                })
                return;
            }

            toast.add({
                    title: "Form Submitted",
                    type: "success",
                    id: "toast",
                    description: result.message,
                })
        } catch (error) {
            console.error(error);
        }

        setSending(prev => !prev)
    };

    return (
        <section id="contact-section">
            <div className="contact-container">
                <div className="content">
                    <div className="content-header">
                        <Badge variant="outline" className='site-badge'>
                            <BadgeCheck data-icon="inline-start" />
                            Contact Us
                        </Badge>
                        <h2 className="site-heading">
                            Don't put your business on hold
                            <span>Talk to our experts.</span>
                        </h2>
                        <TextAnimate by='word' as='p' className='site-body' animation='blurInUp'>
                            Whether you need Skills Development, Enterprise 
                            & Supplier Development support, or guidance on 
                            growing your business, our team is ready to help. 
                            Get in touch with Knowescape Consulting and let's 
                            build your next opportunity.
                        </TextAnimate>
                    </div>
                    <div className="content-footer">
                        <div className="contact-column">
                            <h4 className="site-heading">Contact Details</h4>
                            <ul className='site-body'>
                                <li>+27 82 703 4852</li>
                                <li>info@knowescape.co.za</li>
                            </ul>
                        </div>
                        <div className="contact-column">
                            <h4 className="site-heading">Address</h4>
                            <ul className='site-body'>
                                <li>First Floor, Offices 3 & 5</li>
                                <li>Elgin Mall, Cnr Olienhout & Elgin Roads</li>
                                <li>Kempton Park, Gauteng</li>
                            </ul>
                        </div>
                    </div>
                </div>
                <form id="contact" onSubmit={submitContact}>
                    <div className="form-block">
                        <label htmlFor="first_name">First Name:</label>
                        <input type="text" name="first_name" required id="first_name" placeholder='First Name'/>
                    </div>
                    <div className="form-block">
                        <label htmlFor="last_name">Last Name:</label>
                        <input type="text" name="last_name" required id="last_name" placeholder='Last Name'/>
                    </div>
                    <div className="form-block">
                        <label htmlFor="email">Email:</label>
                        <input type="email" name="email" maxLength={320} required id="email" placeholder='Email'/>
                    </div>
                    <div className="form-block">
                        <label htmlFor="phone">
                            Phone: <span>optional</span>
                        </label>
                        <input type="phone" name="phone" maxLength={10} required id="phone" placeholder='Phone'/>
                    </div>
                    <div className="form-block">
                        <label htmlFor="id_company">Company:</label>
                        <input type="text" name="company" id="id_company" placeholder='Company'/>
                    </div>
                    <div className="form-block">
                        <label htmlFor="service">Service Inquiry:</label>
                        <select name="service" id="service">
                            <option value="startup-support">Startup Support</option>
                            <option value="tender-support">Tender Support</option>
                            <option value="skills-development">Skills Development</option>
                            <option value="enterprise-supplier-development">Enterprise & Supplier Development</option>
                        </select>
                    </div>
                    <div className="form-block contact-block">
                        <label htmlFor="message">Message:</label>
                        <textarea name="message" rows={10} required id="message" placeholder='Any Extra Info?'/>
                    </div>
                    <div className="form-block submit-block">
                        <button className="site-btn" type="submit">
                            {sending ? "sending..." : "send"}
                        </button>                         
                    </div>
        
                </form>
            </div>
        </section>
    )
}