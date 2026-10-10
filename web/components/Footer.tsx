import Image from "next/image"
import '../styles/footer.css'
import Link from "next/link";

import {ArrowUpRight} from "lucide-react"
import { FaFacebook, FaTwitter, FaLinkedin, FaInstagram } from "react-icons/fa";

const dateObj = new Date()
const year = dateObj.getFullYear()

export default function Footer () {

    return (
        <footer id="footer">
            <div className="footer-container">
                <Link href="/" className="footer-brand">
                    <Image src="/text_logo_slim.png" alt="Knowescape Consulting" fill />
                </Link>
                <div className="footer-links">
                    <div className="column-block links">
                        <ul className="footer-column">
                            <h5>Get Around</h5>
                            <Link href="{% url 'home' %}">Home</Link>
                            <Link href="#cta">About Us</Link>
                            <Link href="#services">Our Services</Link>
                            <Link href="#services">Our Faculty</Link>
                            <Link href="/contact">Contact</Link>
                        </ul>
                        <ul className="footer-column">
                            <h5>Our Services</h5>
                            <Link href="{% url 'startup_support' %}">Start-Up Support</Link>
                            <Link href="{% url 'skills_development' %}">Skills Development</Link>
                            <Link href="{% url 'esd' %}">Enterprise & Supplier Development</Link>
                        </ul>
                    </div>
                    <div className="column-block contacts">
                        <ul className="footer-column">
                            <h5>Contact</h5>

                            <Link href={'tel:+27827034852'} target="blank">
                                +27 82 703 4852
                            </Link>
                            <Link href={'mailto:info@knowescape.co.za'} target="blank">
                                info@knowescape.co.za
                            </Link>
                        </ul>
                        <ul className="footer-column">
                            <h5>Physical Address</h5>
                            <li>
                                First Floor, Offices 3 & 5
                            </li>
                            <li>
                                Elgin Mall, Cnr Olienhout & Elgin Roads
                            </li>
                            <li>
                                Kempton Park, Gauteng
                            </li>
                            <Link href="https://maps.app.goo.gl/fUqb4BKKZK1NVS9Y8" target="blank" className="map-link">
                                Open in maps
                                <ArrowUpRight />
                            </Link>
                        </ul>
                    </div>
                </div>
            </div>
            <div className="copyrights">
                <p className="copyright site-body">© KnowEscape Consulting {year}. All Rights Reserved</p>
                <Link href='https://rhulanikgosimogotsi.vercel.app' className="developer site-body" target="blank">
                    Designed and Developed by  
                    <span> Ethernode Tech</span>
                </Link>
                <ul className="social-links">
                    <Link href="https://www.facebook.com/profile.php?id=61565728498754" target="blank">
                        <FaFacebook />
                    </Link>
                    <Link href="https://x.com/knowescapecons" target="blank">
                        <FaTwitter />
                    </Link>
                    <Link href="">
                        <FaLinkedin />
                    </Link>
                    <Link href="https://www.instagram.com/knowescapecons" target="blank">
                        <FaInstagram />
                    </Link>
                </ul>
            </div>
        </footer>
    )
}