import Image from 'next/image'
import Link from 'next/link'
import { ArrowDown, ArrowUpRight } from 'lucide-react'
import type { servicePages } from '@/util/servicePages'
import FAQ from './FAQ'
import '../styles/servicePage.css'

type ServiceContent = (typeof servicePages)[keyof typeof servicePages]

export default function ServiceCategoryPage({ service }: { service: ServiceContent }) {
    return (
        <main className="service-page">
            <header className="service-hero">
                <div className="service-hero__copy">
                    <p className="service-eyebrow">{service.eyebrow}</p>
                    <h1 className="site-heading">{service.title}</h1>
                    <p className="site-body">{service.introduction}</p>
                    <div className="service-hero__actions">
                        <Link href="/#contact-section" className="site-btn primary">
                            Talk to our team <ArrowUpRight aria-hidden="true" />
                        </Link>
                        <a className="service-scroll-link" href="#service-offerings">
                            Explore services <ArrowDown aria-hidden="true" />
                        </a>
                    </div>
                </div>
                <div className="service-hero__visual">
                    <Image
                        src={service.image}
                        alt={service.imageAlt}
                        fill
                        priority
                        sizes="(max-width: 760px) 100vw, 48vw"
                    />
                    <div className="service-hero__image-shade" />
                    <span className="service-hero__index">01 / {String(service.subcategories.length).padStart(2, '0')}</span>
                </div>
            </header>

            <section className="service-offerings" id="service-offerings" aria-labelledby="service-offerings-title">
                <div className="service-offerings__intro">
                    <p className="service-eyebrow">What we do</p>
                    <h2 className="site-heading" id="service-offerings-title">Support for every next step.</h2>
                    <p className="site-body">
                        Explore the ways Knowescape can help your organisation move forward.
                    </p>
                </div>
                <div className="service-offerings__list">
                    {service.subcategories.map((subcategory, index) => (
                        <article className="service-offering" id={subcategory.id} key={subcategory.id}>
                            <span className="service-offering__number">{String(index + 1).padStart(2, '0')}</span>
                            <div className="service-offering__copy">
                                <h3 className="site-heading">{subcategory.title}</h3>
                                <p className="site-body">{subcategory.description}</p>
                            </div>
                            <Link
                                href="/#contact-section"
                                className="service-offering__link"
                                aria-label={`Enquire about ${subcategory.title}`}
                            >
                                <ArrowUpRight aria-hidden="true" />
                            </Link>
                        </article>
                    ))}
                </div>
            </section>

            <div className="service-faq">
                <FAQ faqs={[...service.faqs]} />
            </div>

            <section className="service-cta" aria-labelledby="service-cta-title">
                <p className="service-eyebrow">Let's build what's next</p>
                <h2 className="site-heading" id="service-cta-title">Ready to make progress?</h2>
                <p className="site-body">Tell us where you are and what you want to achieve. We'll help you find a practical next step.</p>
                <Link href="/#contact-section" className="site-btn primary">
                    Start a conversation <ArrowUpRight aria-hidden="true" />
                </Link>
            </section>
        </main>
    )
}
