---
title: "Embed the Innioasis Updater install guide - Innioasis Updater"
description: "Add the Innioasis Updater installation guide to another website with a responsive iframe embed and a copy-ready example."
language: "no"
source: "https://innioasis.app/innioasis-integration-snippet_no.html"
---

# Embed the Innioasis Updater install guide - Innioasis Updater

# 🚀 Innioasis Updater - Embeddable Install Guide

This is a complete, embeddable install guide widget that can be easily integrated into any website. It features a cool bottom-right corner popup CTA that opens a comprehensive installation guide for Windows, macOS, and Linux users.

### 🎨 Beautiful Design

Modern, responsive design that works on all devices with dark mode support

### 📱 Cross-Platform

Complete installation guides for Windows, macOS, and Linux with step-by-step instructions

### 🔧 Easy Integration

Just copy and paste the snippet - no dependencies or complex setup required

### 💾 Smart Storage

Remembers if users have closed the banner to avoid being intrusive

## 📋 Integration Instructions

To add the Innioasis Updater install guide to your website, simply copy and paste this code snippet into your HTML: <!-- Innioasis Updater Install Guide Widget --> <script> (function() { // Create and inject the widget const script = document.createElement('script'); script.src = 'https://your-domain.com/innioasis-embed.html'; script.async = true; // Alternative: Load from local file // script.src = './innioasis-embed.html'; document.head.appendChild(script); // Create iframe container const iframe = document.createElement('iframe'); iframe.src = 'https://your-domain.com/innioasis-embed.html'; iframe.style.cssText = ` position: fixed; bottom: 20px; right: 20px; width: 400px; height: 200px; border: none; z-index: 999999; pointer-events: none; `; // Make iframe interactive iframe.onload = function() { iframe.style.pointerEvents = 'auto'; }; document.body.appendChild(iframe); })(); </script> 📋 Copy Integration Code

## 🎯 Alternative: Direct Embed Method

For even simpler integration, you can directly embed the widget using an iframe: <!-- Direct iframe embed --> <iframe src="https://your-domain.com/innioasis-embed.html" width="400" height="200" frameborder="0" style="position: fixed; bottom: 20px; right: 20px; z-index: 999999; border-radius: 12px; box-shadow: 0 8px 32px rgba(0,0,0,0.3);" allowtransparency="true"> </iframe> 📋 Copy Iframe Code

## 🔧 Customization Options

You can customize the widget by modifying these parameters: // Customize the CTA banner window.InnioasisUpdater = { // Change banner text ctaTitle: "🚀 Get Innioasis Updater", ctaDescription: "Download the desktop app for your platform", ctaButtonText: "Get Started", // Change position position: "bottom-right", // or "bottom-left", "top-right", "top-left" // Auto-show delay (in milliseconds) showDelay: 3000, // Show after 3 seconds // Custom styling customCSS: ` .cta-banner { background: linear-gradient(135deg, #your-color1, #your-color2); } ` }; 

## 📱 Demo

Click the button below to see the widget in action:🎯 Show Demo Widget

## 📚 Features Included
  - Smart CTA Banner: Appears in bottom-right corner with smooth animations
  - Platform Detection: Automatically detects user's operating system
  - Step-by-Step Guides: Complete installation instructions for Windows, macOS, and Linux
  - Progress Tracking: Visual progress bars for multi-step installations
  - Download Integration: Direct download links for all required files
  - Responsive Design: Works perfectly on desktop, tablet, and mobile
  - Dark Mode Support: Automatically adapts to user's system preferences
  - User Preferences: Remembers if user has closed the banner
  - Accessibility: Keyboard navigation and screen reader friendly

## 🌐 Hosting Requirements

To use this widget on your website, you need to:
  - Upload the `innioasis-embed.html` file to your web server
  - Update the URLs in the integration snippet to point to your server
  - Ensure your server supports HTTPS (required for modern browsers)
  - Test the widget on your website to ensure it works correctly

## 🆘 Support

If you need help integrating this widget or have questions, please:
  - Check the browser console for any error messages
  - Ensure all files are properly uploaded to your server
  - Verify that the URLs in the integration code are correct
  - Test on different browsers and devices

 Made with ❤️ by the Innioasis team

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
