'use client'

import Image from 'next/image';
import { useState } from 'react';
import '../styles/hypermenu.css'
import {skills1, skills2, skills3, skills4, skills5} from '@/util/imports';
import '../styles/skillsdevelopmentSection.css'
import { AnimatePresence, motion } from 'motion/react';

export default function SkillsDevelopmentSection () {

    const skillsPanels = [
    {
        id: 1,
        title: "Skills Development Training",
        description: "Practical training programmes designed to build employee capabilities, strengthen workplace performance, and support meaningful skills development.",
        imgSrc: skills1
    },
    {
        id: 2,
        title: "Workplace Skills Planning",
        description: "Structured skills planning to help businesses identify development needs, align training with organisational goals, and meet applicable workplace skills requirements.",
        imgSrc: skills2
    },
    {
        id: 3,
        title: "Learnerships & Workplace Training",
        description: "Workplace-based learning and learnership solutions that combine structured training with practical experience to develop capable, work-ready individuals.",
        imgSrc: skills3
    },
    {
        id: 4,
        title: "Employee Development",
        description: "Targeted employee development programmes that strengthen skills, improve performance, and support long-term professional growth within your organisation.",
        imgSrc: skills4
    },
    {
        id: 5,
        title: "Skills Development Compliance",
        description: "Guidance to help businesses meet skills development requirements, maintain the necessary documentation, and align their training activities with compliance objectives.",
        imgSrc: skills5
    }
];

    const [activePanel, setActivePanel] = useState(skillsPanels[0])
    
        const updateActivePanel = (panelId: number) => {
            const panel = skillsPanels.find((panel) => panel.id === panelId);
    
            if (panel) {
                setActivePanel(panel);
            }
        }

    return (
        <section id="skills-development-section">
            <div className="skills-development-container">
                <div id="hypermenu">
                    <aside id="hypermenu-sidebar">
                        <div className="hypermenu-header">
                            <h1 className="hm-header-heading site-heading">
                                Turn Skills Development Into <span>Business Growth</span>
                            </h1>
                            <p className="hm-header-description site-body">
                                Develop a stronger, more capable workforce with practical Skills Development solutions designed around your business. Knowescape Consulting provides Skills Development Training, workplace skills planning, learnerships, employee development, and Skills Development compliance support to help organisations build talent, improve performance, meet regulatory requirements, and create sustainable opportunities for growth.
                            </p>
                        </div>
                        <ul id="hypermenu-options">
                            {skillsPanels.map((panel, idx) => (
                                <li className="hypermenu-option" key={idx} onMouseOver={(e) => updateActivePanel(panel.id)}>
                                    {panel.title}
                                </li>
                            ))}
                        </ul>
                    </aside>
                    <AnimatePresence mode="wait">
                        <motion.div
                            key={activePanel.id}
                            className="hypermenu-panel"
                            initial={{ opacity: 0, y: 20, filter: "blur(8px)" }}
                            animate={{ opacity: 1, y: 0, filter: "blur(0px)" }}
                            transition={{ duration: 0.4, ease: "easeOut" }}
                        >
                            <Image 
                                alt={activePanel.title}
                                src={activePanel.imgSrc}
                                fill
                                priority
                                className="hypermenu-backdrop"
                            />

                            <div className="content">
                                <h3 className="site-heading">
                                    {activePanel.title}
                                </h3>

                                <p className="site-body">
                                    {activePanel.description}
                                </p>

                                {/* Application intake is not ready yet.
                                <div className="actions">
                                    <div className="site-btn primary">
                                        Apply
                                    </div>
                                </div>
                                */}
                            </div>
                        </motion.div>
                    </AnimatePresence>
                </div>
            </div>
        </section>
    )
}
