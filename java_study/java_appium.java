package booxdevice;

import java.net.MalformedURLException;
import java.net.URL;
import java.time.Duration;

import org.openqa.selenium.By;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.support.ui.Sleeper;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

import io.appium.java_client.MobileElement;
import io.appium.java_client.TouchAction;
import io.appium.java_client.android.AndroidDriver;
import io.appium.java_client.android.AndroidElement;
import io.appium.java_client.android.nativekey.AndroidKey;
import io.appium.java_client.android.nativekey.KeyEvent;
import io.appium.java_client.touch.WaitOptions;
import io.appium.java_client.touch.offset.PointOption;

public class booxauto {
	
		static AndroidDriver<AndroidElement> driver;
		@BeforeClass
		public static void setUp() throws MalformedURLException {
			DesiredCapabilities des =new DesiredCapabilities();
			des.setCapability("platformName", "ANDROID");
			des.setCapability("platformVersion", "10");
			des.setCapability("deviceName", "1a5097ee");
			des.setCapability("appPackage","com.onyx");
			des.setCapability("appActivity","com.onyx.reader.main.ui.MainActivity");
			des.setCapability("unicodeKeyboard", true);
			des.setCapability("resetKeyboard", true);
			URL url=new URL("http://127.0.0.1:4723/wd/hub");
			driver = new AndroidDriver<AndroidElement>(url,des);
		}
		@AfterClass		
		public void tearDown() {
			driver.quit();
		}

		@Test
		public static void libry() throws InterruptedException  {
			Thread.sleep(5000);
			TouchAction action = new TouchAction(driver);
			action.press(PointOption.point(320, 490)).release().perform();
			Thread.sleep(3000);
		}
		@Test
		public static void reader() throws InterruptedException {
			KeyEvent key=new KeyEvent();
			Thread.sleep(2000);
			driver.pressKey(key.withKey(AndroidKey.MENU));		 
			//分屏
			MobileElement el1 = (MobileElement) driver.findElementByXPath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.LinearLayout[5]/android.widget.ImageView");
			el1.click();

			//双开当前文档
																		   //hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.ImageView
			MobileElement el2 = (MobileElement) driver.findElementByXPath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.ImageView");
			el2.click();
			Thread.sleep(2000);
			driver.navigate().back();		 
		    Thread.sleep(2000);
		    
		    driver.pressKey(key.withKey(AndroidKey.MENU));		 	
		    el1.click();
		    //双开笔记
		    MobileElement el3 = (MobileElement) driver.findElementByXPath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.ImageView");
		    el3.click();
		    Thread.sleep(2000);
		    TouchAction action = new TouchAction(driver);
		    Thread.sleep(2000);
			action.press(PointOption.point(1660,860)).release().perform();
			driver.navigate().back();		 
		    Thread.sleep(2000);
		    
		    driver.pressKey(key.withKey(AndroidKey.MENU));		 	
		    el1.click();
			//双开翻译
		    MobileElement el4 = (MobileElement) driver.findElementByXPath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[4]/android.widget.ImageView");
		    el4.click();
		    Thread.sleep(2000);
			driver.navigate().back();		 
		    Thread.sleep(2000);
		    
		    driver.pressKey(key.withKey(AndroidKey.MENU));		 	
		    el1.click();
			//双开不同文档
		    MobileElement el5 = (MobileElement) driver.findElementByXPath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.ImageView");
		    el5.click();
		    MobileElement el6 = (MobileElement) driver.findElementByXPath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.TextView");
		    el6.click();
		    Thread.sleep(2000);
			driver.navigate().back();		 
		    Thread.sleep(2000);
		    
			
		

		}
//		public static void main(String[] args) throws MalformedURLException, InterruptedException{
//		//	driver.quit();
//			setUp();
//			libry();
//			int n=300,m=300;
//			while(m<=300) {
//				reader();
//				m++;
//			}
//			driver.quit();
//			
//			
//		}

	}


