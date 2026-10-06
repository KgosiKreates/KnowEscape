import '../styles/bbbee.css'
import { Badge } from './ui/badge'
import { Blocks, ListChecks, BadgeCheck, ChartNoAxesCombined, Handshake } from 'lucide-react'
import { BentoGrid, BentoCard } from './ui/bento-grid'
import { ShineBorder } from './ui/shine-border'


const features = [
    {
        Icon: Blocks,
        name: "Strategy & Planning",
        description:
            "Develop a practical B-BBEE strategy aligned with your business objectives, transformation priorities, and applicable compliance requirements.",
        href: "#",
        cta: "Learn More",
        className: "bento-card",
        background: (<>
            <ShineBorder shineColor={'#FF7400'} duration={14}/>
        </>),
    },
    {
        Icon: ListChecks,
        name: "Assessment & Readiness",
        description:
            "Evaluate your current B-BBEE position, identify gaps, and establish a clear roadmap to improve your readiness for verification.",
        href: "#",
        cta: "Learn More",
        className: "bento-card",
        background: (<>
            <ShineBorder shineColor={'#FF7400'} duration={14}/>
        </>),
    },
    {
        Icon: BadgeCheck,
        name: "Compliance Support",
        description:
            "Get practical guidance on meeting B-BBEE requirements, maintaining supporting documentation, and implementing compliant transformation initiatives.",
        href: "#",
        cta: "Learn More",
        className: "bento-card",
        background: (<>
            <ShineBorder shineColor={'#FF7400'} duration={14}/>
        </>),
    },
    {
        Icon: ChartNoAxesCombined,
        name: "Scorecard Support",
        description:
            "Understand your B-BBEE scorecard requirements and identify opportunities to improve performance across the relevant B-BBEE elements.",
        href: "#",
        cta: "Learn More",
        className: "bento-card",
        background: (<>
            <ShineBorder shineColor={'#FF7400'} duration={14}/>
        </>),
    },
    {
        Icon: Handshake,
        name: "Transformation Advisory",
        description:
            "Turn B-BBEE requirements into meaningful transformation initiatives that strengthen your business while creating opportunities for employees, suppliers, and beneficiaries.",
        href: "#",
        cta: "Learn More",
        className: "bento-card",
        background: (<>
            <ShineBorder shineColor={'#FF7400'} duration={14}/>
        </>),
    },
]

export default function BBBEESection () {

    return (
        <section id="bbbee">
            <div className="bbbee-container">
                <Badge variant="outline" className='site-badge'>
                    <BadgeCheck data-icon="inline-start" />
                    BBB-EE Advisory
                </Badge>
                <h2 className="site-heading">
                    How we make <span>B-BBEE</span> work for you
                </h2>
                <p className="site-body">
                    Knowescape Consulting provides practical B-BBEE advisory services 
                    to help businesses understand their B-BBEE requirements, identify 
                    compliance gaps, improve their B-BBEE performance, and develop 
                    strategies aligned with their business goals. Contact our team 
                    for professional B-BBEE advisory and transformation support tailored 
                    to your business.
                </p>
                <BentoGrid id='bbbee-bento'>
                    {features.map((feature, idx) => (
                        <BentoCard key={idx} id={`bento-${idx+1}`} {...feature} />
                    ))}
                </BentoGrid>
            </div>
        </section>
    )
}