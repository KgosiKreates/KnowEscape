import '../styles/landing.css'
import Image from 'next/image';
import Link from 'next/link';
import Hypermenu from '@/components/Hypermenu';
import LandingFAQ from '@/components/LandingFAQ';
import ContactSection from '@/components/ContactSection';
import OnboardingHero from '@/components/OnboardingHero'

import Accreditations from '@/components/Accreditations';
import { BlurFade } from "@/components/ui/blur-fade"
import { TextAnimate } from "@/components/ui/text-animate"

import {ArrowUpRight} from "lucide-react"
import BBBEESection from '@/components/BBBEE-Landing';
import SkillsDevelopmentSection from '@/components/SkillsDevelopment-Section';

export default function Landing() {
	return (
		<>
			<header id="landing">

				<div className="content">
					<TextAnimate
						animation="blurInUp"
						by="word"
						as="h1"
						// Target the last animated word element using Tailwind's [&_*:last-child] modifier
						className="site-heading"
						>
						Development Through Empowerment
					</TextAnimate>
					<div className="description">
						<TextAnimate
							delay={.5}
							animation="blurInUp"
							by="word"
							as="p"
							// Target the last animated word element using Tailwind's [&_*:last-child] modifier
							className="site-body"
							>
							Business is built on the right strategy, the right compliance, and the right opportunities. 
							Through Skills Development training and Enterprise & Supplier Development solutions,
						</TextAnimate>
						<TextAnimate
							delay={.5}
							animation="blurInUp"
							by="word"
							as="p"
							// Target the last animated word element using Tailwind's [&_*:last-child] modifier
							className="site-body span"
							>
							we help you put all three in place.
						</TextAnimate>
					</div>
					<BlurFade className="actions" inView inViewMargin='0px' direction='up'>
						<Link href='/' className="site-btn primary">
							Apply
						</Link>
						<Link className="site-link primary" href={'/'}>
							Book a Call
							<ArrowUpRight />
						</Link>
					</BlurFade>
				</div>
				<div className="header-backdrop">
					<Image
						alt='Knowescape Consulting'
						src='/logo-textless.png'
						fill
						priority
					/>
				</div>
			</header>
			<Accreditations />
			<OnboardingHero />
			<SkillsDevelopmentSection />
			<BBBEESection />
			<LandingFAQ />
			<ContactSection />
		</>
	);
}
